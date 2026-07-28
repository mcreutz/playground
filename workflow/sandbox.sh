#!/usr/bin/env bash
set -euo pipefail

# Manage agent worktree sandboxes.
# Usage: sandbox.sh <create|connect|remove|list> [worktree-name]

REPO_ROOT="$(dirname "$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null)")" || {
  echo "Error: not inside a git repository. cd into a repo first."
  exit 1
}

usage() {
  echo "Usage: $0 <create|connect|remove|list> [worktree-name]"
  echo ""
  echo "Commands:"
  echo "  create <name>   Create a new sandbox (worktree + container)"
  echo "  connect <name>  Shell into an existing sandbox"
  echo "  remove <name>   Remove a sandbox and its container"
  echo "  list            List all sandboxes and their status"
  exit 1
}

require_name() {
  if [ -z "${1:-}" ]; then
    echo "Error: worktree name is required."
    usage
  fi
}

preflight_docker() {
  if ! docker info &>/dev/null; then
    echo "Error: Docker is not running."
    exit 1
  fi
}

require_commands() {
  local missing=()
  for cmd in "$@"; do
    if ! command -v "$cmd" &>/dev/null; then
      missing+=("$cmd")
    fi
  done
  if [ ${#missing[@]} -gt 0 ]; then
    echo "Error: missing required tools: ${missing[*]}"
    exit 1
  fi
}

find_workspace_file() {
  local files=("${REPO_ROOT}"/*.code-workspace)
  if [ -f "${files[0]:-}" ]; then
    echo "${files[0]}"
  fi
}

# --- create ---

cmd_create() {
  local WORKTREE_NAME="$1"
  local WORKTREE_DIR="${REPO_ROOT}/.worktrees/${WORKTREE_NAME}"
  local AGENT_LABEL="agent=${WORKTREE_NAME}"

  if [ ! -f "${REPO_ROOT}/.devcontainer/devcontainer.json" ]; then
    echo "Error: no .devcontainer/devcontainer.json found in $(basename "$REPO_ROOT")."
    exit 1
  fi

  if [ -d "$WORKTREE_DIR" ]; then
    echo "Error: Sandbox already exists. To shell in: $0 connect ${WORKTREE_NAME}"
    exit 1
  fi

  local DEFAULT_BRANCH
  DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/@@') || DEFAULT_BRANCH="origin/main"

  echo "Creating worktree at $WORKTREE_DIR ..."
  git worktree add --detach "$WORKTREE_DIR" "$DEFAULT_BRANCH"

  # add worktree to VS Code workspace
  local WORKSPACE_FILE
  WORKSPACE_FILE=$(find_workspace_file)
  local WORKTREE_REL_PATH=".worktrees/${WORKTREE_NAME}"
  if [ -n "$WORKSPACE_FILE" ]; then
    if ! jq -e --arg p "$WORKTREE_REL_PATH" '.folders[] | select(.path == $p)' "$WORKSPACE_FILE" &>/dev/null; then
      echo "Adding worktree to VS Code workspace ..."
      jq --arg p "$WORKTREE_REL_PATH" '.folders += [{"path": $p}]' "$WORKSPACE_FILE" > "${WORKSPACE_FILE}.tmp" \
        && mv "${WORKSPACE_FILE}.tmp" "$WORKSPACE_FILE"
    fi
  fi

  # copy .env if present
  if [ -f "${REPO_ROOT}/.env" ]; then
    echo "Copying .env into worktree ..."
    cp "${REPO_ROOT}/.env" "${WORKTREE_DIR}/.env"
  fi

  # start container — rebuild if devcontainer config changed
  local DEVCONTAINER_DIR="${REPO_ROOT}/.devcontainer"
  local HASH_FILE="${DEVCONTAINER_DIR}/.config-hash"
  local CURRENT_HASH
  CURRENT_HASH=$(cat "${DEVCONTAINER_DIR}/Dockerfile" "${DEVCONTAINER_DIR}/devcontainer.json" | shasum | cut -d' ' -f1)

  local BUILD_ARGS=()
  if [ ! -f "$HASH_FILE" ] || [ "$(cat "$HASH_FILE")" != "$CURRENT_HASH" ]; then
    echo "Devcontainer config changed — rebuilding image ..."
    BUILD_ARGS=(--build-no-cache)
  fi

  echo "Starting devcontainer for ${WORKTREE_NAME} ..."
  devcontainer up --workspace-folder "$REPO_ROOT" --id-label "$AGENT_LABEL" ${BUILD_ARGS[@]+"${BUILD_ARGS[@]}"}

  echo "$CURRENT_HASH" > "$HASH_FILE"

  echo "Sandbox created. To shell in: $0 connect ${WORKTREE_NAME}"
}

# --- connect ---

cmd_connect() {
  local WORKTREE_NAME="$1"
  local WORKTREE_DIR="${REPO_ROOT}/.worktrees/${WORKTREE_NAME}"
  local AGENT_LABEL="agent=${WORKTREE_NAME}"

  if [ ! -d "$WORKTREE_DIR" ]; then
    echo "Error: Sandbox does not exist. Create it first: $0 create ${WORKTREE_NAME}"
    exit 1
  fi

  RUNNING_ID=$(docker container ls -q --filter "label=${AGENT_LABEL}")
  if [ -z "$RUNNING_ID" ]; then
    echo "Error: Container is not running."
    echo "Remove and recreate: $0 remove ${WORKTREE_NAME} && $0 create ${WORKTREE_NAME}"
    exit 1
  fi

  local GIT_USER GIT_EMAIL
  GIT_USER=$(git config user.name) || { echo "Error: git user.name not configured."; exit 1; }
  GIT_EMAIL=$(git config user.email) || { echo "Error: git user.email not configured."; exit 1; }

  echo "Connecting to sandbox ${WORKTREE_NAME} ..."
  devcontainer exec --workspace-folder "$REPO_ROOT" --id-label "$AGENT_LABEL" bash -c "
    cd '${WORKTREE_DIR}'
    [ -f '${WORKTREE_DIR}/.env' ] && set -a && source '${WORKTREE_DIR}/.env' && set +a
    # Default to Opus when using CLAUDE_CODE_OAUTH_TOKEN (upstream bug https://github.com/anthropics/claude-code/issues/8938
    # causes it to show 'Claude API' mode and default to Sonnet).
    export ANTHROPIC_MODEL=opus
    git config user.name '${GIT_USER}'
    git config user.email '${GIT_EMAIL}'
    if [ -n \"\${GH_TOKEN:-}\" ]; then
      git config credential.helper '!f() { echo username=x-access-token; echo password='\"\${GH_TOKEN}\"'; }; f'
    fi
    echo 'Sandbox ready. Worktree: ${WORKTREE_DIR}'
    exec bash
  "
}

# --- remove ---

cmd_remove() {
  local WORKTREE_NAME="$1"
  local WORKTREE_DIR="${REPO_ROOT}/.worktrees/${WORKTREE_NAME}"
  local AGENT_LABEL="agent=${WORKTREE_NAME}"

  if [ ! -d "$WORKTREE_DIR" ]; then
    echo "Error: Worktree does not exist at $WORKTREE_DIR"
    exit 1
  fi

  # stop and remove container
  CONTAINER_ID=$(docker container ls -aq --filter "label=${AGENT_LABEL}")
  if [ -n "$CONTAINER_ID" ]; then
    echo "Removing sandbox container ..."
    docker rm -f "$CONTAINER_ID"
  fi

  # remove worktree
  echo "Removing worktree ${WORKTREE_NAME} ..."
  if ! git worktree remove "$WORKTREE_DIR" 2>/dev/null; then
    echo "Worktree has uncommitted or untracked changes."
    read -r -p "Force remove? [y/N] " confirm
    if [[ "$confirm" =~ ^[Yy]$ ]]; then
      git worktree remove --force "$WORKTREE_DIR"
    else
      echo "Aborted."
      exit 1
    fi
  fi

  # remove from VS Code workspace
  local WORKSPACE_FILE
  WORKSPACE_FILE=$(find_workspace_file)
  local WORKTREE_REL_PATH=".worktrees/${WORKTREE_NAME}"
  if [ -n "$WORKSPACE_FILE" ]; then
    if jq -e --arg p "$WORKTREE_REL_PATH" '.folders[] | select(.path == $p)' "$WORKSPACE_FILE" &>/dev/null; then
      echo "Removing worktree from VS Code workspace ..."
      jq --arg p "$WORKTREE_REL_PATH" '.folders |= map(select(.path != $p))' "$WORKSPACE_FILE" > "${WORKSPACE_FILE}.tmp" \
        && mv "${WORKSPACE_FILE}.tmp" "$WORKSPACE_FILE"
    fi
  fi

  echo "Done."
}

# --- list ---

cmd_list() {
  local WORKTREE_BASE="${REPO_ROOT}/.worktrees"
  if [ ! -d "$WORKTREE_BASE" ] || [ -z "$(ls -A "$WORKTREE_BASE" 2>/dev/null)" ]; then
    echo "No sandboxes found."
    return
  fi

  printf "%-20s  %s\n" "NAME" "CONTAINER"
  for dir in "$WORKTREE_BASE"/*/; do
    [ -d "$dir" ] || continue
    local name
    name=$(basename "$dir")
    local label="agent=${name}"
    local status
    RUNNING_ID=$(docker container ls -q --filter "label=${label}")
    STOPPED_ID=$(docker container ls -aq --filter "label=${label}")
    if [ -n "$RUNNING_ID" ]; then
      status="running"
    elif [ -n "$STOPPED_ID" ]; then
      status="stopped"
    else
      status="no container"
    fi
    printf "%-20s  %s\n" "$name" "$status"
  done
}

# --- main ---

require_commands docker devcontainer jq shasum
preflight_docker

COMMAND="${1:-}"
shift || true

case "$COMMAND" in
  create)
    require_name "${1:-}"
    cmd_create "$1"
    ;;
  connect)
    require_name "${1:-}"
    cmd_connect "$1"
    ;;
  remove)
    require_name "${1:-}"
    cmd_remove "$1"
    ;;
  list)
    cmd_list
    ;;
  *)
    usage
    ;;
esac

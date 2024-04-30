# Git
## Setup
```bash
# User data
git config --global user.name "Mona Lisa"
git config --global user.name
> Mona Lisa
git config --global user.email "email@example.com"
git config --global user.email
> email@example.com

# Store credentials in an unencrypted file at ~/.git-credentials
git config credential.helper store

# Use MacOS Keychain
git config --global credential.helper osxkeychain
```

## Repo initialization
```bash
# Initialize git in current directory
git init

# Clone remote repository to local drive
git clone <url> [<local_path>]
```

## Staging and comitting modifications
```bash
# Show modifications
git diff <file>

# Add file [or single changes within them] to stage/index
git add [-p] <file>

# Show modified and staged/indexed files
git status

# Remove file from stage/index but keep changes locally, use `--hard` to remove changes from working directory as well
git reset <file>

# Commit staged/indexed changes
git commit [-m <message>]
```

## Undoing/removing from version control
```bash
# Remove a file from version control but keep it in the filesystem
git rm --cached <file>

# Delete local commits and keep local changes if it was not pushed to a remote repo ('--hard' to remove changes from working directory as well)
git reset HEAD~1  # remove last commit, HEAD~2 for the last 2, etc.
git reset <commit-hash>  # remove all commits up to the specified commit

# Undo a commit that was already pushed to a remote repo (commits an inverse commit)
git revert <commit-hash>
```

## Navigating commits
```bash
# List existing commits
git log

# Show the content of a commit
git show <commit-hash>

# Move the working directory to the state of an existing commit
git checkout <commit-hash>

# Move the working directory back to the latest commit
git checkout <current-branch-name>
```

## Remotes
```bash
# Push local commits of the active branch to the remote repo
git push

# Push local commits of a specific branch to the remote repo
git push <branch-name>

# Push local commits of new branch to remote repo
git push --set-upstream <remote-name> <branch-name>

# Pull new commits from remote repo into local workspace
git pull

# Fetch new commits from remote repo into local repo, but do not update local workspace
git fetch

# Get URL of remote
git remote get-url <remote-name>
```

## Branching
```bash
# List branches
git branch

# Create new branch
git branch <name>

# Switch to other branch
git switch <name> [-c to create and switch]
# deprecated: git checkout <name>

# Rename branch
git branch -m new-name

# Delete a local branch
git branch -d <name>

# Delete a remote branch
git push remote_name -d remote_branch_name
```

## Merging
```bash
# Merge another branch into the current one
git merge <name>

# Merge two branches
git merge <destination> <source>

# Abort a conflicted merge
git merge --abort
```

## Rebasing
```bash
# Integrate all commits of another branch into the current one. This modifies the git history, so only use on local commits and never on commits that were already pushed to a remote repo.
git rebase <name>
```

## Stashing
```bash
# List stashes
git stash list

# Stash the changes in the working directory in a new stash
git stash push
git stash  # same as `git stash push`
git stash -u  # include untracked files
git stash push <file>  # stash a single file
# deprecated: git stash save  # same as `git stash push`

# Export a stash to a patch file
git stash show -p stash@{n} > patch.diff

# show details of a stash
git stash show stash@{n}

# Apply a stash
git stash apply  # apply the last stash
git stash apply stash@{n}  # apply a specific stash
git stash pop  # apply the last stash and delete it

# Apply a stash from a patch file
git apply patch.diff  # without `stash` command

# Delete a stash
git stash drop  # remove the last stash
git stash drop stash@{n}  # Remove a specific stash
```


## Nice reference
https://education.github.com/git-cheat-sheet-education.pdf

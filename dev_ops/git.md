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

## Committing
```bash
# Delete commits (from the end of commit history)
git reset --hard HEAD~1  # use `HEAD~n` for the last n commits
git reset --hard <commit-hash>  # remove all commits up to the specified commit
git push -f  # force push to remote repo
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
git branch -d <branch_name>
git branch -D <branch_name>  # force delete, if branch has unmerged changes

# Delete a remote branch
git push -d <remote_name> <branch_name>
```

## Merging
```bash
# Merge another branch into the current one
git merge <name>

# Merge two branches
git merge <destination> <source>
```

Preview the conflicts of a merge
```bash
git branch temp
git switch temp
git merge <branch-to-merge> --no-ff --no-commit

# Abort a conflicted merge
git merge --abort
```

## Rebasing
```bash
# Integrate all commits of another branch into the current one. This modifies the git history, so only use on local commits and never on commits that were already pushed to a remote repo.
git rebase <name>
```

## Stashing
Stash the changes in the working directory in a new stash
```bash
git stash push
git stash  # same as `git stash push`
git stash -u  # include untracked files
git stash push <file>  # stash a single file
# deprecated: git stash save  # same as `git stash push`
```

List stashes
```bash
git stash list
```

Show the content of a stash
```bash
git stash show  # show an overview of the last stash
git stash show stash@{<number>}  # show an overview of a specific stash
git stash show -p stash@{<number>}  # show the actual changes of a specific stash
```

Apply the last stash
```bash
git stash apply
```

Apply a specific stash
```bash
git stash apply stash@{<number>}
```

git stash pop  # apply the last stash and delete it


Remove the last stash
```bash
git stash drop
```

Remove a specific stash
```bash
git stash drop stash@{<number>}
```

Export a stash as a patch file
```bash
git stash show -p stash@{<number>} > <file>
```

Import a patch file as a stash
```bash
git apply <file>
```


## Tagging
```bash
# List tags
git tag

# Create a tag
git tag <tag-name>

# Create an annotated tag
git tag -a <tag-name> -m <message>

# Push a tag to a remote repo
git push <remote-name> <tag-name>

# Push all tags to a remote repo (don't do this unless you know what you're doing)
git push <remote-name> --tags

# Delete a tag locally
git tag -d <tag-name>

# Delete a tag on a remote repo
git push -d <remote-name> <tag-name>


## ToDo
- fast-forward merge
- interative rebase
- squashing commits
- git cherry-pick
- difference between local and remote branches
- git reflog
- git bisect
- git blame
- git tag
- git describe
- workdirs
- git hooks
- git config

## Nice reference
https://education.github.com/git-cheat-sheet-education.pdf

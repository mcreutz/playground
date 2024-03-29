# Git
## Setup
User data
```bash
git config --global user.name "Mona Lisa"
git config --global user.name
> Mona Lisa
git config --global user.email "email@example.com"
git config --global user.email
> email@example.com
```

### Store credentials
Unencrypted file at ~/.git-credentials
```bash
git config credential.helper store
```

MacOS Keychain
```bash
git config --global credential.helper osxkeychain
```

## Repo initialization
Initialize git in current directory
```bash
git init
```

Clone remote repository to local drive
```bash
git clone <url> [<local_path>]
```

## Staging and comitting modifications
Show modifications
```bash
git diff <file>
```

Add file [or single changes within them] to stage/index
```bash
git add [-p] <file>
```

Show modified and staged/indexed files
```bash
git status
```

Remove file from stage/index but keep changes locally, use `--hard` to remove changes from working directory as well
```bash
git reset <file>
```

Commit staged/indexed changes
```bash
git commit [-m <message>]
```

## Undoing/removing from version control
Remove a file from version control but keep it in the filesystem
```bash
git rm --cached <file>
```

Undo last commit and keep local changes if it was not pushed to a remote repo (--hard to remove changes from working directory as well)
```bash
git reset HEAD~1
```

Undo a commit that was already pushed to a remote repo (commits an inverse commit)
```bash
git revert <commit-hash>
```

## Navigating commits
List existing commits
```bash
git log
```

Show the content of a commit
```bash
git show <commit-hash>
```

Move the working directory to the state of an existing commit
```bash
git checkout <commit-hash>
```

Move the working directory back to the latest commit
```bash
git checkout <current-branch-name>
```

## Remotes
Push local commits of the active branch to the remote repo
```bash
git push
```

Push local commits of a specific branch to the remote repo
```bash
git push <branch-name>
```

Push local commits of new branch to remote repo
```bash
git push --set-upstream <remote-name> <branch-name>
```

Pull new commits from remote repo into local workspace
```bash
git pull
```

Fetch new commits from remote repo into local repo, but do not update local workspace
```bash
git fetch
```

Get URL of remote
```bash
git remote get-url <remote-name>
```

## Branching
List branches
```bash
git branch
```

Create new branch
```bash
git branch <name>
```

Switch to other branch
```bash
git switch <name> [-c to create and switch]
# deprecated: git checkout <name>
```

Rename branch
```bash
git branch -m new-name
```

Delete a local branch
```bash
git branch -d <name>
```

Delete a remote branch
```bash
git push remote_name -d remote_branch_name
```

## Merging
Merge another branch into the current one
```bash
git merge <name>
```

Merge two branches
```bash
git merge <destination> <source>
```

Abort a conflicted merge
```bash
git merge --abort
```

## Rebasing
Integrate all commits of another branch into the current one. This modifies the git history, so only use on local commits and never on commits that were already pushed to a remote repo.
```bash
git rebase <name>
```

## Nice reference
https://education.github.com/git-cheat-sheet-education.pdf

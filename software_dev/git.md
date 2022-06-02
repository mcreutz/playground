## Setup
### User
`$ git config --global user.name "Mona Lisa"`

`$ git config --global user.name`

`> Mona Lisa`

`$ git config --global user.email "email@example.com"`

`$ git config --global user.email`

`> email@example.com`
### Store credentials
#### Unencrypted file at ~/.git-credentials
`$ git config credential.helper store`

#### MacOS Keychain
`$ git config --global credential.helper osxkeychain`

---
## Initialization
### Initialize git in current directory
`$ git init`

### Clone remote repository to local drive
`$ git clone <url> [<local_path>]`

---
## Comitting modifications
### Add file [single changes] to stage/index
`$ git add [-p] <file>` 

### Show modifications
`$ git diff <file>`

### Show modified and staged/indexed files
`$ git status`

### Remove file from stage/index but keep changes locally
`$ git reset <file>`

### Commit staged/indexed changes
`$ git commit [-m <message>]`

### Remove file from version control but keep it in the filesystem
`$ git rm --cached <file>`

---
## Branching
### List branches
`$ git branch`

### Create new branch
`$ git branch <name>`

### Switch to other branch
`$ git switch <name>` [-c to create and switch]

(old: `$ git checkout <name>`)

### Rename branch
`$ git branch -m new-name`

### Merge another branch into the current one
`$ git merge <name>`

### Merge two branches
`$ git merge <destination> <source>`

### Abort a conflicted merge
`$ git merge --abort`

### Delete local branch
`$ git branch -d <name>`

### Delete remote branch
`$ git push remote_name -d remote_branch_name`

### Integrate all commits of another branch into the current one. This modifies the git history, so only use on local commits and never on commits that were already pushed to a remote repo.
`$ git rebase <name>`

---
## Remotes
### Get URL of remote named origin
`$ git remote get-url origin`

---
## Nice reference
https://education.github.com/git-cheat-sheet-education.pdf

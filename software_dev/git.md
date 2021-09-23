## Initialization
### Initialize git in current directory
`git init`

### Clone remote repository to local drive
`git clone <url> [<local_path>]`

---
## Comitting modifications
### Add file to stage/index
`git add <file>`

### Remove file from stage/index but keep changes locally
`git reset <file>`

### Show modified and staged/indexed files
`git status`

### Commit staged/indexed changes
`git commit [-m <message>]`

### Remove file from version control but keep it in the filesystem
`git rm --cached <file>`

---
## Branching
### List branches
`git branch`

### Create new branch
`git branch <name>`

### Switch to other branch
`git checkout <name>`

### Merge another branch into the current one
`git merge <name>`

---
## Nice reference
https://education.github.com/git-cheat-sheet-education.pdf
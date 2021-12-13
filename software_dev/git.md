## Initialization
### Initialize git in current directory
`git init`

### Clone remote repository to local drive
`git clone <url> [<local_path>]`

---
## Comitting modifications
### Add file [single changes] to stage/index
`git add [-p] <file>` 

### Show modifications
`git diff <file>`

### Show modified and staged/indexed files
`git status`

### Remove file from stage/index but keep changes locally
`git reset <file>`

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
`git switch <name>` [-c to create and switch]

(old: `git checkout <name>`)

### Merge another branch into the current one
`git merge <name>`

### Abort a conflicted merge
`git merge --abort`

### Delete local branch
`git branch -d <name>`

### Integrate all commits of another branch into the current one. This modifies the git history, so only use on local commits and never on commits that were already pushed to a remote repo.
`git rebase <name>`

---
## Nice reference
https://education.github.com/git-cheat-sheet-education.pdf
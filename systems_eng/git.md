## Setup
### User
```console
$ git config --global user.name "Mona Lisa"`
$ git config --global user.name
> Mona Lisa
```
```console
$ git config --global user.email "email@example.com"
$ git config --global user.email
> email@example.com
```

### Store credentials
#### Unencrypted file at ~/.git-credentials
```console
$ git config credential.helper store
```

#### MacOS Keychain
```console
$ git config --global credential.helper osxkeychain
```

---
## Initialization
### Initialize git in current directory
```console
$ git init
```

### Clone remote repository to local drive
```console
$ git clone <url> [<local_path>]
```

---
## Comitting modifications
### Add file [single changes] to stage/index
```console
$ git add [-p] <file>
```

### Show modifications
```console
$ git diff <file>
```

### Show modified and staged/indexed files
```console
$ git status
```

### Remove file from stage/index but keep changes locally
```console
$ git reset <file>
```

### Commit staged/indexed changes
```console
$ git commit [-m <message>]
```

### Remove file from version control but keep it in the filesystem
```console
$ git rm --cached <file>
```

---
## Branching
### List branches
```console
$ git branch
```

### Create new branch
```console
$ git branch <name>
```

### Switch to other branch
```console
$ git switch <name> [-c to create and switch]
```

```console
$ git checkout <name> (deprecated)
```

### Rename branch
```console
$ git branch -m new-name
```

### Merge another branch into the current one
```console
$ git merge <name>
```

### Merge two branches
```console
$ git merge <destination> <source>
```

### Abort a conflicted merge
```console
$ git merge --abort
```

### Delete local branch
```console
$ git branch -d <name>
```

### Delete remote branch
```console
$ git push remote_name -d remote_branch_name
```

### Integrate all commits of another branch into the current one. This modifies the git history, so only use on local commits and never on commits that were already pushed to a remote repo.
```console
$ git rebase <name>
```

---
## Remotes
### Get URL of remote
```console
$ git remote get-url <remote-name>
```

### Push local commits of active branch to remote repo
```console
$ git push
```

### Push local commits of specific branch to remote repo
```console
$ git push <branch-name>
```

### Push local commits of new branch to remote repo
```console
$ git push --set-upstream <remote-name> <branch-name>
```

---
## Nice reference
https://education.github.com/git-cheat-sheet-education.pdf

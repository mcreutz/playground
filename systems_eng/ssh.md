# SSH client
## Example for ~/.ssh/config
```
Host <name>
  HostName <hostname_or_ip>
  User <remote_user>
  LocalForward 3000 localhost:3000
  LocalForward 3001 localhost:3001

Match host=<name1>
   IdentitiesOnly yes
   IdentityFile ~/.ssh/id_rsa_IDENTITY1

Match host=<name2>,<name3>
   IdentitiesOnly yes
   IdentityFile ~/.ssh/id_ed25519_IDENTITY2
```

## Create SSH key
```
ssh-keygen -C "<comment>"
```

## Copy SSH key to remote server
```
ssh-copy-id <user>@<host> [<-i keyfile> if different from ~/.ssh/id_rsa.pub]
```

## Copy SSH key to remote server (Windows Powershell client)
```
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh <user>@<host> "cat >> .ssh/authorized_keys"
```
# OpenSSH

## Generate new SSH key pair
```
ssh-keygen [-f <keyfile>] [-t <algorithm>] -b <bits> -N <passphrase> -C "<comment>"
```
Options
- -f `<keyfile>`: prompted if not specified, defaults to `~/.ssh/id_rsa`
- -N `<passphrase>`: additionally encrypts the private key, prompted if not specified, defaults to none
- -t `<algorithm>`: [`dsa` | `ecdsa` | `ecdsa-sk` | `ed25519` | `ed25519-sk` | `rsa` (default)]
- -b `<bits>`: [
   - `rsa`: Minimum `1024`, default `3072` 
   - `dsa`: `1024`, no other option possible
   - `ecdsa`: Determines the key length by selecting from one of three elliptic curve sizes: `256`, `384` or `521` bits
   - `ecdsa-sk`, `ed25519` and `ed25519-sk`: Fixed length, will be ignored if specified
]
- -C "`<comment>`": email address is frequently used here to identify the key's owner, defaults to none

## Copy SSH key to remote server
### Linux / MacOS
```shell
ssh-copy-id [<user>@]<host>
```
Options
- -i `<keyfile>`: defaults to `~/.ssh/id_rsa.pub`
- -p `<port>`: defaults to `22`
- `<user>` defaults to current local user

### Windows Powershell
```shell
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh <user>@<host> "cat >> .ssh/authorized_keys"
```

## Connect to remote server
```shell
ssh [<user>@]<host>
```
Options
- -i `<keyfile>`: defaults to `~/.ssh/id_rsa`
- -p `<port>`: defaults to `22`
- `<user>` defaults to current local user

## SSH Agent
Can be used to store private keys in memory, so that they don't have to be entered every time they are used.
### Start SSH Agent
```shell
eval `ssh-agent`
```
### Add key to SSH Agent
```shell
ssh-add [<keyfile>]
```
Options
- `<keyfile>`: defaults to `~/.ssh/id_rsa`

## SSH Tunneling
### Local port forwarding
Local port forwarding allows you to forward traffic on a port of the local machine to a port on the remote machine.
```shell
ssh -L <local_port>:<remote_host>:<remote_port> <user>@<host>
```
Options
- -L `<local_port>:<remote_host>:<remote_port>`: forwards connections from `<local_port>` on the local machine to `<remote_host>:<remote_port>` on the remote machine
- `<user>` defaults to current local user
- `<host>` defaults to `localhost`
- `<remote_port>` defaults to `<local_port>`
- `<remote_host>` defaults to `localhost`

### Remote port forwarding
Remote port forwarding allows you to forward traffic on a port of the remote machine to a port on the local machine.
```shell
ssh -R <remote_port>:<local_host>:<local_port> <user>@<host>
```
Options
- -R `<remote_port>:<local_host>:<local_port>`: forwards connections from `<remote_port>` on the remote machine to `<local_host>:<local_port>` on the local machine
- `<user>` defaults to current local user
- `<host>` defaults to `localhost`
- `<local_port>` defaults to `<remote_port>`
- `<local_host>` defaults to `localhost`

### Dynamic port forwarding
Dynamic port forwarding allows you to create a SOCKS proxy on the local machine which tunnels requests to the remote machine.
```shell
ssh -D <local_port> <user>@<host>
```
Options
- -D `<local_port>`: creates a SOCKS proxy on `<local_port>` on the local machine which tunnels requests to `<host>` on `<local_port>`
- `<user>` defaults to current local user
- `<host>` defaults to `localhost`

## SSH client config file
- located at `~/.ssh/config`
- create with `touch ~/.ssh/config && chmod 600 ~/.ssh/config`
### Eample
```
Host <name>
   HostName <hostname_or_ip>
   User <remote_user>  # defaults to current local user
   Port <port>  # defaults to 22
   IdentityFile <file>  # defaults to ~/.ssh/id_rsa
   LocalForward 3000 localhost:3000  # optional port forwardings
   LocalForward 3001 localhost:3001

Host *  # string with wildcards (*?!) can be used to match multiple hosts
   LogLevel ERROR  # suppresses all messages except errors
```
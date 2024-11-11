# Manage certificate-based SSH connections
## Create a key pair on the client
```bash
ssh-keygen -t ED25519 -C "your_email@example.com" -f ~/.ssh/id_ed25519_something
```
- "-t" ED25519 is the type of key
- "-C" is a comment to help identify the key
- "~/.ssh/id_ed25519" is the default location for the private key
- "~/.ssh/id_ed25519.pub" is the default location for the public key
- will prompt for a filename if none is provided
- will prompt for a passphrase

If you copied over a key pair (with a non-default name) that was created on another machine, you need to add it to the ssh-agent:
```bash
ssh-add ~/.ssh/id_ed25519_something
```

## Copy the public key to the remote server
```bash
ssh-copy-id -i ~/.ssh/id_ed25519_something.pub user@remote_host
```
This will copy (append) the content of the public key file to the file ~/.ssh/authorized_keys on the remote host

## Configure the SSH server on the remote host
```bash
sudo nano /etc/ssh/sshd_config
```
Uncommment and change the following settings
- PasswordAuthentication no
- PubkeyAuthentication yes
- AuthorizedKeysFile .ssh/authorized_keys

## Restart the SSH server
```bash
sudo service ssh restart
```

## Edit the clients SSH configuration file
```bash
cat <<EOF >> ~/.ssh/config
Host my_remote_host
  HostName <remote host ip>
  User <user>
  IdentityFile ~/.ssh/id_ed25519_something

EOF
```

## Connect to the remote host
```bash
ssh my_remote_host
```

## Add the host keys to the clients known_hosts file
When connecting to a remote host for the first time, you will be prompted if you want to add the host key to the known_hosts file.
If you want to add the host key manually, you can use the following command:
```bash
ssh-keyscan -H <remote_host> >> ~/.ssh/known_hosts
```
This will copy (append) the host keys from `/etc/ssh` on the <remote_host> to the known_hosts file on the client. The most secure way to do this (preventing MITM attacks) is to copy the host keys manually from the remote host to the client.

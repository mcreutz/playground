# Cloud-Init VMs with Proxmox

## Setup the Cloud-Init Template in Proxmox
Add your SSH key to the key store of Proxmox
```sh
ssh-copy-id -i ~/.ssh/id_ed25519_martin.pub root@192.168.0.10
```
Copy the SSH key file to the Proxmox host
```sh
scp ~/.ssh/id_ed25519_martin.pub root@192.168.0.10:/root/.ssh/id_ed25519_martin.pub
```


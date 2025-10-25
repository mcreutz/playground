# Cloud-Init VMs with Proxmox

## Prerequisites
Add your SSH key to the key store of Proxmox
```sh
ssh-copy-id -i ~/.ssh/id_ed25519_martin.pub root@192.168.0.10
```
Copy key file to root folder to make it available for cloud-init
```sh
scp ~/.ssh/id_ed25519_martin.pub root@192.168.0.10:/root/.ssh/id_ed25519_martin.pub
```

## Setup the Cloud-Init Template in Proxmox
Copy the cloud-init script file to the Proxmox server
```sh
scp create_cloud_init_template.sh root@server01:/root/
```
Login to the Proxmox server
```sh
ssh root@server01
```
Run the cloud-init template script
```sh
bash ./create_cloud_init_template.sh
```

## Create a new Cloud-Init VM
In the Proxmox web interface create a new VM based on the cloud-init template.
- Set the vm name and select "Full Clone" in the first step
- Set CPU, Memory and Disk(s) size as needed.
- Start the VM
- The default user is "ubuntu" with password "ChangeMe!". Change the password with `passwd` command after first login.
- Get the IP address of the VM with `hostname -I` to setup your SSH accress. SSH key is already installed for user "ubuntu".
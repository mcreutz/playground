# setup nfs server
```bash
# install nfs server
sudo apt install nfs-kernel-server

# create shared directory
sudo mkdir -p /srv/my_shared_dir

# set permissions for shared directory
sudo chown nobody:nogroup /srv/my_shared_dir  # nobody:nogroup means all users
sudo chmod 777 /srv/my_shared_dir  # allow all users to read, write and execute

# add shared directory to /etc/exports
echo "/srv/my_shared_dir <clients>(rw,sync,no_subtree_check)" | sudo tee -a /etc/exports
# <clients> can be a hostname, a single ip address or a subnet
# options:
#   rw: read-write
#   ro: read-only
#   sync: the server will wait for the data to be written to disk before replying to the client
#   async: the server will reply to the client before the data is written to disk
#   no_subtree_check: disable subtree checking, use this where possible
#   subtree_check: enable subtree checking
#   root_squash (default): map root user to nobody
#   no_root_squash: allow root user to access the shared directory as root
#   all_squash: map all users to nobody
#   secure: allow clients to access ports < 1024
#   insecure: allow clients to access ports > 1024
#   anonuid=<uid>: map all users to a specific user
#   anongid=<gid>: map all users to a specific group

# open firewall
sudo ufw allow from <clients> to any port nfs  # clients can access nfs port 2049

# export shared directory
sudo exportfs -a

# start nfs server
sudo systemctl restart nfs-kernel-server
sudo systemctl status nfs-kernel-server
```


# setup nfs client
```bash
# install nfs client
sudo apt install nfs-common

# list shared directories of a host
showmount --exports <host>

# mount shared directory
sudo mount -t nfs <host>:/srv/my_shared_dir /mnt/my_shared_dir

# unmount shared directory
sudo umount /mnt/my_shared_dir

# mount shared directory automatically on boot
echo "<host>:/srv/my_shared_dir /mnt/my_shared_dir nfs defaults 0 0" | sudo tee -a /etc/fstab
```
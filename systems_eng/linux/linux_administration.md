# NMAP
## ping for network devices
- nmap -sn 192.168.0.0/24

## Portscan
- nmap <url>
- nmap 192.168.0.1-10
- nmap 192.168.0.1/13
- nmap –p80 192.168.0.1
- nmap –p1-200 192.168.0.1
- nmap –F 192.168.0.1  # Scan (Fast) the most common ports
- nmap –p– 192.168.0.1  # scan all ports (1 – 65535)

# Find process listening on port
- netstat -anv | grep <port>  # gets the PID
- ps -A | grep <pid>

# Process management
- kill <pid>
- pkill <pname>
- killall
- ps
- top / htop
- pstree
- pgrep
- pmap
- lsof
- nice

# Gaining root user privileges
- sudo <command>  # Execute the command with admin privileges, if current user is granted sudo rights. User password is prompted. Some distros also change to a safe PATH, see '/etc/sudoers'.
- su <username>  # Switch to other user, but with existing environment. Switches to root, if no username is given. New user's password is prompted. 'exit' or Ctrl-D to exit.
- su -  # Switch to root with root environment. '-' is short for '-l', switching environment. Root user password is prompted
- sudo su -  # Switch to root with root environment. User password is prompted

# User management
- whoami  # show current user
- who  # show logged-in users
- useradd -m <username>  # -m to create home folder
- passwd <username> # change password
- usermod -aG sudo <username>  # add user to sudo group

# Disk management
- df -H  # show disk usage
- du
- fdisk -l  # list disks
- mount  # show mounted disks
- umount  # unmount disk
- parted  # partition editor
- mkfs  # create filesystem
- fsck  # check filesystem
- lsblk  # list block devices

# Memory
- free  # show memeory usage

# Network
- ip
- ifconfig  # list all network interfaces
- netstat  # show network traffic
- nslookup <domain>  # get domain information
- curl / wget

# Firewall
- iptables
- nftables

# Archiving
- tar -xf <file>  # extract archive

# Ignore aliases
- command <command>  # execute command, ignoring aliases

# Other
* `head`- 
* `tail`- 
* `date`- 
* `less`- 
* `history`- 
* `ps`- 
* `gzip`-  \ gunzip \ tar
* `awk`- 
* `tr` - replace characters in output: echo "$PATH" | tr ':' '\n'
* `watch`- periodically run a command and show output
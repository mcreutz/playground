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

# Useful commands and programs
* `awk`- 
* curl / wget  # download/upload files from the network/internet. Can also be used to send HTTP requests. 
* `date`- 
* grep  # filter lines for text or regex
* `gzip`-  \ gunzip \ tar
* `head` / `tail`- 
* `history`- command history
* jq / yq # JSON processor / YAML processor
* `less` `more` - view text files
* mount | column -t  # column formatted table of active mounts
* passwd  # change password of local user accounts
* `ps`- 
* pushd / popd  # Push current directory to stack and change to given directory / Pop directory from stack and change to it
* pwd  # print working directory
* sed  # stream editor
* tail -f  # open textfile and stream file updates
* tar  # create and extract archives
* tee  # write to file and print to stdout
* test  # testing file existence and properties. Also strings and integers.
* `tr` - replace characters in output: echo "$PATH" | tr ':' '\n'
* truncate -s 0 filename  # Remove content of file up to given size is reached. Good to clear a file without deleting it.* 
* `watch`- periodically run a command and show output

# shortcuts
!nnn  # Run command no nnn from command history
!!  # Last command
-  # Previous directory
.  # Current directory
..  # Parent directory
~  # Current users home directory
Esc, Esc  # Re-run last command with sudo, zsh only
$?  # Exit code of last command
$_  # Last argument of last command
$!  # PID of last background command
# NMAP
## ping for network devices
- nmap -sn 192.168.0.0/24

## Portscan
- nmap <host>  # Scan the most common ports
- nmap 192.168.0.1-10  # a range of hosts
- nmap 192.168.0.1/13  # a range of hosts in CIDR notation
- nmap –p80 <host>  # Scan a specific port
- nmap –p1-200 <host>  # Scan a range of ports
- nmap –F <host>  # Scan (Fast) the most common ports
- nmap –p– <host>  # scan all ports (1 – 65535)

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
- passwd <username> # change password of local user accounts
- usermod -aG sudo <username>  # add user to sudo group

# Disk management
- df -H  # show disk usage
- du
- fdisk -l  # list disks
- mount  # show mounted disks
* mount | column -t  # column formatted table of active mounts
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
- curl / wget  # download/upload files from the network/internet. Can also be used to send HTTP requests. 

# Firewall
- iptables
- nftables

# Archiving
- tar -xf <file>  # extract archive
- gzip <file>  # compress archive
- gzip -d <file>  # decompress archive
- gunzip <file>  # decompress archive

# Aliases
- alias  # show aliases
- alias <alias>="<command>"  # create alias
- command <command>  # execute command, ignoring aliases

# Kernel Modules
* `lsmod` - list loaded kernel modules
* `modinfo` - show information about a kernel module
* `modprobe` - load a kernel module
* `rmmod` - unload a kernel module

# Logs
* `dmesg` - show kernel messages
* `journalctl` - show systemd logs
* `tail -f /var/log/syslog` - show syslog messages

# Package management
* `apt list --installed` - list installed packages

# Navigating directories
cd /path/to/directory  # Change directory
cd ..  # Change to parent directory
cd -  # Change to previous directory
cd /  # Change to root directory
cd ~  # Change to home directory
pwd  # Print current working directory
pushd /path/to/directory  # Change directory and push current directory to stack
popd  # Pop directory from stack and change to it
dirs  # Print directory stack
dirs -c  # Clear directory stack

# Command history
history  # show command history
!!  # Run the last command
!-1  # Run the last command
!-2  # Run the second last command
!n  # Run the nth command
HISTTIMEFORMAT="%F %T "  # set history timestamp format, %F is date, %T is time. Bash only.
HISTSIZE=1000  # set history size
HISTFILESIZE=1000  # set history file size
history -i  # show timestamps in history, zsh only
history -c  # clear history
 date  # type a space in front of the command to prevent it from being saved in history


# Useful commands and programs
* `awk` - text processing
* `date` - 
* `grep` - filter lines for text or regex
* `head` / `tail`- 
* `jq` /  - JSON processor
* `yq` - YAML processor
* `less` `more` - view text files
* tail -f  # open textfile and stream file updates
* tee  # write to file and print to stdout
* test  # testing file existence and properties. Also strings and integers.
* `tr` - replace characters in output: echo "$PATH" | tr ':' '\n'
* truncate -s 0 filename  # Remove content of file up to given size is reached. Good to clear a file without deleting it.* 
* `watch`- periodically run a command and show output
* find /path/to/dir -name "filaname.*" -exec rm -rf {} \;  # find and delete files
# fstab and crypt eqivalent
# cat filesystems
# cryptutility
* tmux  # terminal multiplexer
* <command> | column -t  # change output to column formatted table


# shortcuts
-  # Previous directory
.  # Current directory
..  # Parent directory
~  # Current users home directory
Esc, Esc  # Re-run last command with sudo, zsh only
$?  # Exit code of last command
$_  # Last argument of last command
$!  # PID of last background command
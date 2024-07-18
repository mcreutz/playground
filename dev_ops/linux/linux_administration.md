# System
## System information
uname -a : Displays all system information.
hostnamectl : Shows current hostname and related details.
lscpu : Lists CPU architecture information.
timedatectl status : Shows system time.

## System monitoring and management
top : Displays real-time system processes.
htop : An interactive process viewer (needs installation).
df -h : Shows disk usage in a human-readable format.
free -m : Displays free and used memory in MB.
kill <process id> : Terminates a process.

## Kernel Modules
* `lsmod` - list loaded kernel modules
* `modinfo` - show information about a kernel module
* `modprobe` - load a kernel module
* `rmmod` - unload a kernel module

## Logs
* `dmesg` - show kernel messages
* `journalctl` - show systemd logs
* `tail -f /var/log/syslog` - show syslog messages

## Process management
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

## Memory
- free  # show memeory usage

## Package management (APT)
sudo apt install -f –reinstall <package> : Reinstalls a broken package.
apt search <package> : Searches for APT packages.
apt-cache policy <package> : Lists available package versions.
sudo apt purge <package> : Removes a package and all its configuration files.
* `apt list --installed` - list installed packages

## Package management (Snap)
snap find <package> : Search for Snap packages.
sudo snap refresh : Updates all installed Snap packages.
snap info <snap_name> : Displays information about a Snap package.

## Cron jobs and scheduling
crontab -e : Edits cron jobs for the current user.
crontab -l : Lists cron jobs for the current user.

## Service management
sudo systemctl start <service> : Starts a service.
sudo systemctl stop <service> : Stops a service
sudo systemctl status <service> : Checks the status of a service.
sudo systemctl reload <service> : Reloads a service’s configuration without
interrupting its operation.
journalctl -f : Follows the journal, showing new log messages in real time.
journalctl -u <unit_name> : Displays logs for a specific systemd unit.

## Kernel Modules
* `lsmod` - list loaded kernel modules
* `modinfo` - show information about a kernel module
* `modprobe` - load a kernel module
* `rmmod` - unload a kernel module

## Logs
* `dmesg` - show kernel messages
* `journalctl` - show systemd logs
* `tail -f /var/log/syslog` - show syslog messages

# Networking
## Basics
- ip
- ifconfig  # list all network interfaces
- netstat  # show network traffic
- nslookup <domain>  # get domain information
- curl / wget
ip addr show : Displays network interfaces and IP addresses.
ip -s link : Shows network statistics.
ss -l : Shows listening sockets.

## Firewall
- iptables
- nftables
sudo ufw status : Displays the status of the firewall.
sudo ufw enable : Enables the firewall.
sudo ufw disable : Disables the firewall.
sudo ufw allow <port/service> : Allows traffic on a specific port or service.
sudo ufw deny <port/service> : Denies traffic on a specific port or service.
sudo ufw delete allow/deny <port/service> : Deletes an existing rule.

## Netplan configuration (read more at netplan.io)
cat /etc/netplan/*.yaml : Displays the current Netplan configuration.
sudo netplan try : Tests a new configuration for a set period of time.
sudo netplan apply : Applies the current Netplan configuration.

## NMAP
### ping for network devices
- nmap -sn 192.168.0.0/24

### Portscan
- nmap <host>  # Scan the most common ports
- nmap 192.168.0.1-10  # a range of hosts
- nmap 192.168.0.1/13  # a range of hosts in CIDR notation
- nmap –p80 <host>  # Scan a specific port
- nmap –p1-200 <host>  # Scan a range of ports
- nmap –F <host>  # Scan (Fast) the most common ports
- nmap –p– <host>  # scan all ports (1 – 65535)

## Find process listening on port
- netstat -anv | grep <port>  # gets the PID
- ps -A | grep <pid>

# User management
- whoami  # show current user
- who  # show logged-in users
- `cat /etc/passwd`  # show all users
- useradd -m <username>  # -m to create home folder
- passwd <username> # change password of local user accounts
- usermod -aG sudo <username>  # add user to sudo group
w : Shows which users are logged in.
sudo adduser <username> : Creates a new user.
sudo deluser <username> : Deletes a user.
sudo passwd <username> : Sets or changes the password for a user.
su <username> : Switches user.
sudo passwd -l <username> : Locks a user account.
sudo passwd -u <username> : Unlocks a user password.
Sudo change <username> : Sets user password expiration date.

## Group management
id [username] : Displays user and group IDs.
groups [username] : Shows the groups a user belongs to.
sudo addgroup <groupname> : Creates a new group.
sudo delgroup <groupname> : Deletes a group.

## Gaining root user privileges
- sudo <command>  # Execute the command with admin privileges, if current user is granted sudo rights. User password is prompted. Some distros also change to a safe PATH, see '/etc/sudoers'.
- su <username>  # Switch to other user, but with existing environment. Switches to root, if no username is given. New user's password is prompted. 'exit' or Ctrl-D to exit.
- su -  # Switch to root with root environment. '-' is short for '-l', switching environment. Root user password is prompted
- sudo su -  # Switch to root with root environment. User password is prompted

# User management
- whoami  # show current user
- who  # show logged-in users
- `cat /etc/passwd`  # show all users
- useradd -m <username>  # -m to create home folder
- passwd <username> # change password
- usermod -aG sudo <username>  # add user to sudo group
w : Shows which users are logged in.
sudo adduser <username> : Creates a new user.
sudo deluser <username> : Deletes a user.
sudo passwd <username> : Sets or changes the password for a user.
su <username> : Switches user.
sudo passwd -l <username> : Locks a user account.
sudo passwd -u <username> : Unlocks a user password.
Sudo change <username> : Sets user password expiration date.

## Group management
id [username] : Displays user and group IDs.
groups [username] : Shows the groups a user belongs to.
sudo addgroup <groupname> : Creates a new group.
sudo delgroup <groupname> : Deletes a group.

## Gaining root user privileges
- sudo <command>  # Execute the command with admin privileges, if current user is granted sudo rights. User password is prompted. Some distros also change to a safe PATH, see '/etc/sudoers'.
- su <username>  # Switch to other user, but with existing environment. Switches to root, if no username is given. New user's password is prompted. 'exit' or Ctrl-D to exit.
- su -  # Switch to root with root environment. '-' is short for '-l', switching environment. Root user password is prompted
- sudo su -  # Switch to root with root environment. User password is prompted

# Persistence
## Disk management
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

## File searching and finding
find [directory] -name <search_pattern> : Finds files and directories.
grep <search_pattern> <file> : Searches for a pattern in files.

## Archiving and compression
* `gzip` -  / `gunzip` / `gunzip -c` unzips to stdout / `tar`
* zip [-r] <archive.zip> <file>  # create zip archive
* unzip <archive.zip> [-d destination-path] # extract zip archive
tar -czvf <name.tar.gz> [files] : Compresses files into a tar.gz archive.
tar -xvf <name.tar.[gz|bz|xz]> [destination] : Extracts a compressed tar archive.
- tar -xf <file>  # extract archive
- gzip <file>  # compress archive
- gzip -d <file>  # decompress archive
- gunzip <file>  # decompress archive

# Usage
## Running commands
[command] & : Runs command in the background.
jobs : Displays background commands.
fg <command number> : Brings command to the foreground.

## Aliases
- alias  # show aliases
- alias <alias>="<command>"  # create alias
- command <command>  # execute command, ignoring aliases

## Navigating directories
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

## Command history
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
* tail -f  # open textfile and stream file updates
* `jq` /  - JSON processor
* `yq` - YAML processor
* `less` `more` - view text files
* tee  # write to file and print to stdout
* test  # testing file existence and properties. Also strings and integers.
* `tr` - replace characters in output: echo "$PATH" | tr ':' '\n'
* truncate -s 0 filename  # Remove content of file up to given size is reached. Good to clear a file without deleting it.* 
* `watch`- periodically run a command and show output
* find /path/to/dir -name "filaname.*" -exec rm -rf {} \;  # find and delete files
* `find /path/to/dir -type f -name "*.log" | wc -l`  # count files in dir including subdirs
* `wc`  # word count
* `wc -l`  # line count
* `xargs` - build and execute command lines from standard input
# fstab and crypt eqivalent
# cat filesystems
# cryptutility
* tmux  # terminal multiplexer
* <command> | column -t  # change output to column formatted table
* stat <file>  # show stats, like size, permissions, access timestamps etc.


# shortcuts
-  # Previous directory
.  # Current directory
..  # Parent directory
~  # Current users home directory
Esc, Esc  # Re-run last command with sudo, zsh only
$?  # Exit code of last command
$_  # Last argument of last command
$!  # PID of last background command

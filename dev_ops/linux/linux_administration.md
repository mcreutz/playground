# System
## System information
- `uname -a` Displays all system information
- `hostnamectl` Shows current hostname and related details
- `hostnamectl set-hostname <new_hostname>` Sets the system hostname
- `lscpu` Lists CPU architecture information
- `timedatectl status` Shows system time

## System monitoring and management
- `top` Displays real-time system processes
- `htop` An interactive process viewer (needs installation)
- `df -h` Shows disk usage in a human-readable format
- `free -m` Displays free and used memory in MB
- `kill <process id>` Terminates a process

## Kernel Modules
- `lsmod` List loaded kernel modules
- `modinfo` Show information about a kernel module
- `modprobe` Load a kernel module
- `rmmod` Unload a kernel module

## Logs
- `dmesg` Show kernel messages
- `journalctl` Show systemd logs
- `tail -f /var/log/syslog` Show syslog messages

## Process management
- `kill <pid>` Kill process by ID
- `pkill <pname>` Kill process by name
- `killall` Kill all processes by name
- `ps` Show processes
- `top` / `htop` Process viewer
- `pstree` Show process tree
- `pgrep` Get process ID by name
- `pmap` Show memory map of process
- `lsof` List open files
- `nice` Run program with modified scheduling priority

## Memory
- `free` Show memory usage

## Package management (APT)
- `sudo apt install -f --reinstall <package>` Reinstalls a broken package
- `apt search <package>` Searches for APT packages
- `apt-cache policy <package>` Lists available package versions
- `sudo apt purge <package>` Removes a package and all its configuration files
- `apt list --installed` List installed packages

## Package management (Snap)
- `snap find <package>` Search for Snap packages
- `sudo snap refresh` Updates all installed Snap packages
- `snap info <snap_name>` Displays information about a Snap package
- `snap changes` Shows recent Snap changes
- `snap list` Lists installed Snap packages
- `sudo snap set system refresh.hold=<snap_name>` Prevents a Snap package from being updated

## Cron jobs and scheduling
- `crontab -e` Edits cron jobs for the current user
- `crontab -l` Lists cron jobs for the current user

## Service management
- `sudo systemctl start <service>` Starts a service
- `sudo systemctl stop <service>` Stops a service
- `sudo systemctl status <service>` Checks the status of a service
- `sudo systemctl reload <service>` Reloads a service's configuration
- `journalctl -f` Follows the journal in real time
- `journalctl -u <unit_name>` Displays logs for a specific systemd unit

## Keyboard Layout
- `loadkeys de` Load the German keyboard layout
- `setxkbmap` Set the keyboard layout
- `localectl` Control the system locale and keyboard layout settings

# Networking
## Basics
- `ip` Show/manipulate routing, devices, policy routing and tunnels
- `ifconfig` List all network interfaces
- `netstat` Show network traffic
- `nslookup <domain>` Get domain information
- `curl` / `wget` Transfer data from/to servers
- `ip addr show` Displays network interfaces and IP addresses
- `ip -s link` Shows network statistics
- `ss -l` Shows listening sockets
- `ip route show` Displays routing table


## Firewall
- `iptables` IP packet filter administration
- `nftables` Netfilter packet filtering framework
- `sudo ufw status` Displays the status of the firewall
- `sudo ufw enable` Enables the firewall
- `sudo ufw disable` Disables the firewall
- `sudo ufw allow <port/service>` Allows traffic on a specific port
- `sudo ufw deny <port/service>` Denies traffic on a specific port
- `sudo ufw delete allow/deny <port/service>` Deletes an existing rule

## Netplan configuration
- `cat /etc/netplan/*.yaml` Displays the current Netplan configuration
- `sudo netplan try` Tests a new configuration
- `sudo netplan apply` Applies the current Netplan configuration

## NMAP
### ping for network devices
- `nmap -sn 192.168.0.0/24` Scan network for devices

### Portscan
- `nmap <host>` Scan the most common ports
- `nmap 192.168.0.1-10` Scan a range of hosts
- `nmap 192.168.0.1/13` Scan a range of hosts in CIDR notation
- `nmap -p80 <host>` Scan a specific port
- `nmap -p1-200 <host>` Scan a range of ports
- `nmap -F <host>` Scan (Fast) the most common ports
- `nmap -p- <host>` Scan all ports (1-65535)

## Find process listening on port
- `netstat -anv | grep <port>` Gets the PID
- `ps -A | grep <pid>` Show process details

# User management
- `whoami` Show current user
- `who` Show logged-in users
- `cat /etc/passwd` Show all users
- `useradd -m <username>` Create user with home folder
- `passwd <username>` Change password of local user accounts
- `usermod -aG sudo <username>` Add user to sudo group
- `w` Shows which users are logged in
- `who -aH` Shows who is logged in
- `sudo adduser <username>` Creates a new user
- `sudo deluser <username>` Deletes a user
- `sudo passwd <username>` Sets or changes the password for a user
- `su <username>` Switches user
- `sudo passwd -l <username>` Locks a user account
- `sudo passwd -u <username>` Unlocks a user password
- `sudo chage <username>` Sets user password expiration date

## Group management
- `id [username]` Displays user and group IDs
- `groups [username]` Shows the groups a user belongs to
- `sudo addgroup <groupname>` Creates a new group
- `sudo delgroup <groupname>` Deletes a group

## Gaining root user privileges
- `sudo <command>` Execute command with admin privileges
- `su <username>` Switch to other user with existing environment
- `su -` Switch to root with root environment
- `sudo su -` Switch to root with root environment

# Persistence
## Disk management
- `df -H` Show disk usage
- `du` Show directory space usage
- `fdisk -l` List disks
- `mount` Show mounted disks
- `mount | column -t` Column formatted table of active mounts
- `umount` Unmount disk
- `parted` Partition editor
- `mkfs` Create filesystem
- `fsck` Check filesystem
- `lsblk` List block devices

## File searching and finding
- `find [directory] -name <search_pattern>` Finds files and directories
- `grep <search_pattern> <file>` Searches for a pattern in files

## Archiving and compression
- `gzip` / `gunzip` / `gunzip -c` Compress/decompress files
- `zip [-r] <archive.zip> <file>` Create zip archive
- `unzip <archive.zip> [-d destination-path]` Extract zip archive
- `tar -czvf <name.tar.gz> [files]` Compresses files into archive
- `tar -xvf <name.tar.[gz|bz|xz]>` Extracts compressed archive
- `tar -xf <file>` Extract archive
- `gzip <file>` Compress archive
- `gzip -d <file>` Decompress archive
- `gunzip <file>` Decompress archive

# Usage
## Running commands
- `[command] &` Runs command in the background
- `jobs` Displays background commands
- `fg <command number>` Brings command to the foreground

## Aliases
- `alias` Show aliases
- `alias <alias>="<command>"` Create alias
- `command <command>` Execute command ignoring aliases
## Navigating directories
- `cd /path/to/directory` Change directory
- `cd ..` Change to parent directory
- `cd -` Change to previous directory
- `cd /` Change to root directory
- `cd ~` Change to home directory
- `pwd` Print current working directory
- `pushd /path/to/directory` Change directory and push current directory to stack
- `popd` Pop directory from stack and change to it
- `dirs` Print directory stack
- `dirs -c` Clear directory stack

## Command history
- `history` Show command history
- `!!` Run the last command
- `!-1` Run the last command
- `!-2` Run the second last command
- `!n` Run the nth command
- `HISTTIMEFORMAT="%F %T "` Set history timestamp format, %F is date, %T is time (Bash only)
- `HISTSIZE=1000` Set history size
- `HISTFILESIZE=1000` Set history file size
- `history -i` Show timestamps in history (zsh only)
- `history -c` Clear history
- ` date` Type a space in front of the command to prevent it from being saved in history

## Useful commands and programs
- `awk` Text processing
- `date` Show or set system date and time
- `grep` Filter lines for text or regex
- `head` / `tail` View beginning/end of files
- `tail -f` Open textfile and stream file updates
- `jq` JSON processor
- `yq` YAML processor
- `less` / `more` View text files
- `tee` Write to file and print to stdout
- `test` Testing file existence and properties, strings and integers
- `tr` Replace characters in output
- `truncate -s 0 filename` Remove content of file up to given size
- `watch` Periodically run a command and show output
- `find /path/to/dir -name "filename.*" -exec rm -rf {} \;` Find and delete files
- `find /path/to/dir -type f -name "*.log" | wc -l` Count files in dir including subdirs
- `wc` Word count
- `wc -l` Line count
- `xargs` Build and execute command lines from standard input
- fstab and crypt eqivalent
- `cat /etc/fstab` Shows configured filesystem mounts
- `cryptsetup` Manage LUKS encrypted volumes and devices
- `tmux` Terminal multiplexer for multiple virtual consoles
- `command | column -t` Change output to column formatted table
- `stat <file>` Show stats, like size, permissions, access timestamps
- `sort` Sort lines of text
- `uniq` Remove or show duplicate lines
- `cut` Remove sections from each line of files

## Shortcuts
- `-` Previous directory
- `.` Current directory
- `..` Parent directory
- `~` Current users home directory
- `Esc, Esc` Re-run last command with sudo (zsh only)
- `$?` Exit code of last command
- `$_` Last argument of last command
- `$!` PID of last background command
- `Ctrl + A` Move to beginning of line
- `Ctrl + E` Move to end of line
- `Ctrl + U` Delete from cursor to beginning of line
- `Ctrl + K` Delete from cursor to end of line
- `Ctrl + W` Delete word before cursor
- `Ctrl + Y` Paste deleted text
- `Ctrl + L` Clear screen
- `Ctrl + R` Search command history
- `Ctrl + C` Kill current process
- `Ctrl + Z` Suspend current process
- `Ctrl + D` Exit shell or send EOF
- `reset` Reset terminal
- `clear` Clear terminal screen
- Send to background: `Ctrl + Z`, `bg`, `disown -h`
- return to foreground: `fg`
- `!!` Repeat last command
- `!$` Repeat last argument of last command
- `!^` Repeat first argument of last command
- `!n` Repeat nth command in history
- `!-n` Repeat nth last command in history
- `!string` Repeat last command starting with string
- `!string:p` Print last command starting with string
- `!string:s/old/new` Replace old with new in last command starting with string
- `!string:gs/old/new` Replace all occurrences of old with new in last command starting with string

## File permissions
- `chmod` Change file permissions
- `chown` Change file owner and group
- `chgrp` Change file group
- `ls -l` List files with permissions
- `ls -a` List all files including hidden files
- `ls -lh` List files with human-readable sizes
- `ls -ld` List directory permissions
- `umask` Set default file permissions

## File operations
- `touch` Create an empty file
- `cp` Copy files and directories
- `mv` Move or rename files and directories
- `rm` Remove files and directories
- `ln` Create hard or symbolic links
- `find` Find files and directories
- `locate` Find files and directories by name
- `file` Determine file type
- `diff` Compare files line by line
- `patch` Apply a diff file to an original
- `rsync` Remote file sync

## Text processing
- `cat` Concatenate and display files
- `more` Display files one screen at a time
- `less` Display files one screen at a time
- `head` Display the beginning of a file
- `tail` Display the end of a file
- `grep` Search for text in files
- `sed` Stream editor for filtering and transforming text
- `awk` Pattern scanning and processing language
- `cut` Remove sections from each line of files
- `sort` Sort lines of text
- `uniq` Report or omit repeated lines
- `wc` Print newline, word, and byte counts for each file
- `tee` Read from standard input and write to standard output and files
- `tr` Translate or delete characters
- `fmt` Reformat paragraph text
- `pr` Convert text files for printing
- `fold` Wrap each input line to fit in specified width
- `join` Join lines of two files on a common field
- `comm` Compare two sorted files line by line

## Network
- `ping` Send ICMP ECHO_REQUEST to network hosts
- `traceroute` Print the route packets trace to network host
- `mtr` Network diagnostic tool
- `netstat` Print network connections, routing tables, interface statistics
- `ss` Utility to investigate sockets
- `dig` DNS lookup utility
- `host` DNS lookup utility
- `whois` Lookup domain registration information
- `wget` Non-interactive network downloader
- `curl` Transfer data from or to a server
- `scp` Secure copy files between hosts on a network

## System information
- `uname` Print system information
- `hostname` Print or set system name
- `lscpu` Display information about the CPU architecture
- `lsblk` List block devices
- `lshw` List hardware
- `lspci` List all PCI devices
- `lsusb` List all USB devices
- `lsmod` Show the status of loaded kernel modules
- `uptime` Show how long the system has been running
- `who` Show who is logged on
- `w` Show who is logged on and what they are doing
- `last` Show the last users logged on
- `date` Show the current date and time
- `cal` Show this month's calendar
- `df` Show disk usage
- `free` Show memory and swap usage
- `whereis` Locate the binary, source, and manual page files for a command
- `which` Locate a command
- `man` Display a command's manual page
- `info` Display a command's info entry
- `whatis` Display one-line manual page descriptions
- `apropos` Display a list of appropriate commands

## System control
- `shutdown` Shutdown or restart the system
- `reboot` Reboot the system
- `halt` Stop the system
- `poweroff` Stop the system
- `systemctl` Control the systemd system and service manager
- `journalctl` Query the systemd journal
- `timedatectl` Control the system time and date

## System control (systemd)
- `systemctl start service` Start a service
- `systemctl stop service` Stop a service
- `systemctl restart service` Restart a service
- `systemctl reload service` Reload a service
- `systemctl status service` Show the status of a service
- `systemctl enable service` Enable a service to start on boot
- `systemctl disable service` Disable a service to start on boot
- `systemctl list-units --type service` List all active services
- `systemctl list-unit-files --type service` List all services

# Todo
- filesystem links: file, ln, mount, umount
- systemd
- cron
- awk
- sort
- locate, find
- uname, hostname
- time
- systemctl
- watch
- jobs
- wget, curl
- rsync
- ip, netstat, traceroute, ss, nslookup, dig, whois, ifconfig, ping
- cd, ls, pwd, mkdir, rmdir, rm, cp, mv, touch, cat, less, more, head, tail, grep, sed, awk, cut, sort, uniq, wc, tee, tr, fmt, pr, fold, join, comm
- history, !!, !$, !^, !n, !-n, !string, !string:p, !string:s/old/new, !string:gs/old/new
- alias, unalias, command, which, whereis, whatis, apropos
- chmod, chown, chgrp, umask
- grep
- uniq
- diff
- wc
- ps, top, htop, pstree, pgrep, pmap, lsof, nice, kill, killall, pkill
- vmstat, iostat, sar, mpstat, pidstat, dstat, free
- df, du, fdisk, mount, umount, parted, mkfs, fsck, lsblk
- tar, gzip, gunzip, zip, unzip
- find, locate
- date, time, cal
- apt, dpkg, snap, apt-get, apt-cache, aptitude, pacman, yum, dnf, zypper, flatpak, appimage
- useradd, usermod, userdel, usermod, passwd, su, sudo, chage, groups, id, who, w, whoami
- groupadd, groupmod, groupdel
- shutdown, reboot, halt, poweroff
- systemctl, journalctl, timedatectl
- netplan
- ufw, iptables, nftables
- lscpu, lsusb, lspci, lsmod, lsblk, lshw
- demsg, journalctl, syslog
- service
- xargs
- bg
- tcpdump
- nc
- strace

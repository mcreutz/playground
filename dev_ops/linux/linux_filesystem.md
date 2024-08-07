- /bin: It contains common system commands that can be executed by any users.

- /boot: It saves files related to system startup, such as kernel files and bootloader (grub) files, etc.

- /dev: It contains the device files for every hardware device attached to the system. These are not device drivers, rather they are files that represent each device on the computer and facilitate access to those devices.

- /etc: It contains the local system configuration files for the host computer, such as user information, service startup scripts, configuration files for common services, etc. It's similar to Windows Registry.

- /home: It's the default location to log in and save user data. Each user has a subdirectory in /home.

- /lib: It contains shared library files that are required to boot the system.

- /media: It's the place used to mount external removable media devices such as floppy disks, CDs, and USB thumb drives that may be connected to the host.

- /mnt: It's the traditional mountpoint for regular hard drive partitions (file systems). But most people like to mount hard drives under /home

- /misc: It's the place used to mount the shared directory of the NFS service.

- /opt: It's the place used to place and install other software.

- /usr: Its full name is Unix Software Resource. It is the default installation location of the software and similar to the complex of "C:\Windows\ + C:\Program files\" in the Windows system.

- /root: It is the home directory for the root user. It's the default location to log in and save root user data.

- /sbin: It saves commands related to system environment settings. Only root can use these commands, but there are also commands that allow ordinary users to view. Also see 'single user mode'.

- /srv: It contains data for services. After some system services are started, they can call out or save necessary data in this directory.

- /tmp: It is a place where the system stores temporary files, under which all users can access and write.

- /lost+found: When the system crashes unexpectedly or shuts down unexpectedly, some file fragments will be stored here. During system startup, the fsck tool will check this directory and repair the damaged file system. Please note this directory only appears in each partition (file system).

- /proc: The data in this directory is not saved on the hard disk, but in the memory. It mainly saves the system's kernel, process, external device status and network status, etc.

- /sys: It's similar to the /proc directory and the data in this directory is stored in memory, but it mainly stores information related to the kernel.

- /var: It is used to store dynamic data, such as caches, log files, and files generated during software operation.


Futher reding: https://www.pathname.com/fhs/pub/fhs-2.3.html
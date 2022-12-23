#!/bin/bash

# set env variables
SAMBA_WORKGROUP=${SAMBA_WORKGROUP:-WORKGROUP}
SAMBA_SERVER_STRING=${SAMBA_SERVER_STRING:-Docker Samba Server}
SAMBA_LOG_LEVEL=${SAMBA_LOG_LEVEL:-0}
SAMBA_MIN_PROTOCOL_VERSION=${SAMBA_MIN_PROTOCOL_VERSION:-NT1}
SAMBA_MAX_PROTOCOL_VERSION=${SAMBA_MAX_PROTOCOL_VERSION:-SMB3_11}
USERNAME=${USERNAME:-testuser}
USERGROUP=${USERGROUP:-testgroup}
PASSWORD=${PASSWORD:-Secret}
SHARENAME=${SHARENAME:-TEST-SHARE}
SHAREPATH=${SHAREPATH:-'/shared_directory'}


echo "Initializing files and folders"
mkdir -p /data/cache /data/lib
if [ -z "$(ls -A /data/lib)" ]; then
  cp -r /var/lib/samba/* /data/lib/
fi
rm -rf /var/lib/cache /var/lib/samba
ln -sf /data/cache /var/cache/samba
ln -sf /data/lib /var/lib/samba


echo "Creating config file"
  cat > /etc/samba/smb.conf <<EOL
[global]
workgroup = ${SAMBA_WORKGROUP}
server string = ${SAMBA_SERVER_STRING}
server role = standalone server
server services = -dns, -nbt
server signing = default
server multi channel support = yes
log level = ${SAMBA_LOG_LEVEL}
security = user
guest account = nobody
pam password change = yes
map to guest = bad user
usershare allow guests = yes
create mask = 0664
force create mode = 0664
directory mask = 0775
force directory mode = 0775
follow symlinks = no
unix extensions = no
printing = bsd
printcap name = /dev/null
disable spoolss = yes
disable netbios = yes
smb ports = 445
client ipc min protocol = default
client ipc max protocol = default
dns proxy = no
socket options = TCP_NODELAY
strict locking = no
local master = no
winbind scan trusted domains = yes
vfs objects = fruit streams_xattr
server min protocol = ${SAMBA_MIN_PROTOCOL_VERSION}
server max protocol = ${SAMBA_MAX_PROTOCOL_VERSION}
[${SHARENAME}]
path = ${SHAREPATH}
comment = shared directory for tests
writeable = no
browseable = yes
guest ok = no
EOL

echo "Adding user"
addgroup -g 1000 -S ${USERGROUP}
adduser -u 1000 -G ${USERGROUP} ${USERNAME} -SHD
echo -e "${PASSWORD}\n${PASSWORD}" | smbpasswd -a -s ${USERNAME}
unset password

echo "Testing configuration"
testparm -s

echo "Starting samba service"
exec "$@"

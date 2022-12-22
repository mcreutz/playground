#!/bin/bash

SAMBA_WORKGROUP=${SAMBA_WORKGROUP:-WORKGROUP}
SAMBA_SERVER_STRING=${SAMBA_SERVER_STRING:-Docker Samba Server}
SAMBA_SMB_PORT=${SAMBA_SMB_PORT:-445}
SAMBA_LOG_LEVEL=${SAMBA_LOG_LEVEL:-0}
SAMBA_MIN_PROTOCOL_VERSION=${SAMBA_MIN_PROTOCOL_VERSION:-NT1}
SAMBA_MAX_PROTOCOL_VERSION=${SAMBA_MAX_PROTOCOL_VERSION:-SMB3_11}

echo "Initializing files and folders"
mkdir -p /data/cache /data/lib
if [ -z "$(ls -A /data/lib)" ]; then
  cp -r /var/lib/samba/* /data/lib/
fi
rm -rf /var/lib/cache /var/lib/samba
ln -sf /data/cache /var/cache/samba
ln -sf /data/lib /var/lib/samba

echo "Setting global configuration"
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
smb ports = ${SAMBA_SMB_PORT}
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
EOL

# auth
if [[ "$(yq --output-format=json e '(.. | select(tag == "!!str")) |= envsubst' /data/config.yml 2>/dev/null | jq '.auth')" != "null" ]]; then
  for auth in $(yq -j e '(.. | select(tag == "!!str")) |= envsubst' /data/config.yml 2>/dev/null | jq -r '.auth[] | @base64'); do
    _jq() {
      echo "${auth}" | base64 --decode | jq -r "${1}"
    }
    password=$(_jq '.password')
    if [[ "$password" = "null" ]] && [[ -f "$(_jq '.password_file')" ]]; then
      password=$(cat "$(_jq '.password_file')")
    fi
    echo "Creating user $(_jq '.user')/$(_jq '.group') ($(_jq '.uid'):$(_jq '.gid'))"
    id -g "$(_jq '.gid')" &>/dev/null || id -gn "$(_jq '.group')" &>/dev/null || addgroup -g "$(_jq '.gid')" -S "$(_jq '.group')"
    id -u "$(_jq '.uid')" &>/dev/null || id -un "$(_jq '.user')" &>/dev/null || adduser -u "$(_jq '.uid')" -G "$(_jq '.group')" "$(_jq '.user')" -SHD
    echo -e "$password\n$password" | smbpasswd -a -s "$(_jq '.user')"
    unset password
  done
fi

# share
if [[ "$(yq --output-format=json e '(.. | select(tag == "!!str")) |= envsubst' /data/config.yml 2>/dev/null | jq '.share')" != "null" ]]; then
  for share in $(yq --output-format=json e '(.. | select(tag == "!!str")) |= envsubst' /data/config.yml 2>/dev/null | jq -r '.share[] | @base64'); do
    _jq() {
      echo "${share}" | base64 --decode | jq -r "${1}"
    }
    echo "Creating share $(_jq '.name')"
    if [[ "$(_jq '.name')" = "null" ]] || [[ -z "$(_jq '.name')" ]]; then
      >&2 echo "ERROR: Name required"
      exit 1
    fi
    echo -e "\n[$(_jq '.name')]" >> /etc/samba/smb.conf
    if [[ "$(_jq '.path')" = "null" ]] || [[ -z "$(_jq '.path')" ]]; then
      >&2 echo "ERROR: Path required"
      exit 1
    fi
    echo "path = $(_jq '.path')" >> /etc/samba/smb.conf
    if [[ "$(_jq '.comment')" != "null" ]] && [[ -n "$(_jq '.comment')" ]]; then
      echo "comment = $(_jq '.comment')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.browsable')" = "null" ]] || [[ -z "$(_jq '.browsable')" ]]; then
      echo "browsable = yes" >> /etc/samba/smb.conf
    else
      echo "browsable = $(_jq '.browsable')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.readonly')" = "null" ]] || [[ -z "$(_jq '.readonly')" ]]; then
      echo "read only = yes" >> /etc/samba/smb.conf
    else
      echo "read only = $(_jq '.readonly')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.guestok')" = "null" ]] || [[ -z "$(_jq '.guestok')" ]]; then
      echo "guest ok = yes" >> /etc/samba/smb.conf
    else
      echo "guest ok = $(_jq '.guestok')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.validusers')" != "null" ]] && [[ -n "$(_jq '.validusers')" ]]; then
      echo "valid users = $(_jq '.validusers')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.adminusers')" != "null" ]] && [[ -n "$(_jq '.adminusers')" ]]; then
      echo "admin users = $(_jq '.adminusers')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.writelist')" != "null" ]] && [[ -n "$(_jq '.writelist')" ]]; then
      echo "write list = $(_jq '.writelist')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.veto')" != "null" ]] && [[ "$(_jq '.veto')" = "no" ]]; then
      echo "veto files = /._*/.apdisk/.AppleDouble/.DS_Store/.TemporaryItems/.Trashes/desktop.ini/ehthumbs.db/Network Trash Folder/Temporary Items/Thumbs.db/" >> /etc/samba/smb.conf
      echo "delete veto files = yes" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.hidefiles')" != "null" ]] && [[ -n "$(_jq '.hidefiles')" ]]; then
      echo "hide files = $(_jq '.hidefiles')" >> /etc/samba/smb.conf
    fi
    if [[ "$(_jq '.recycle')" != "null" ]] && [[ -n "$(_jq '.recycle')" ]]; then
      echo "vfs objects = recycle" >> /etc/samba/smb.conf
      echo "recycle:repository = .recycle" >> /etc/samba/smb.conf
      echo "recycle:keeptree = yes" >> /etc/samba/smb.conf
      echo "recycle:versions = yes" >> /etc/samba/smb.conf
    fi
  done
fi

testparm -s

exec "$@"

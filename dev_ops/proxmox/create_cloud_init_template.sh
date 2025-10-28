#!/bin/bash

set -e

#------------------------------------------------------------------------------
# CONFIGURATION
#------------------------------------------------------------------------------

UBUNTU_VERSION="24.04"
CI_USER="ubuntu"
CI_PASSWORD="ChangeMe!"
SSH_KEY_PATH="~/.ssh/id_ed25519_martin.pub"

#------------------------------------------------------------------------------
# Script Logic
#------------------------------------------------------------------------------

# Download Ubuntu cloud image
IMAGE_URL="https://cloud-images.ubuntu.com/releases/${UBUNTU_VERSION}/release/ubuntu-${UBUNTU_VERSION}-server-cloudimg-amd64.img"
IMAGE_FILE="ubuntu-${UBUNTU_VERSION}-server-cloudimg-amd64.img"
wget "${IMAGE_URL}"

# Create VM
VM_ID="900"
VM_NAME="ubuntu-${UBUNTU_VERSION}-template"
VM_MEMORY="2048"
NETWORK_BRIDGE="vmbr0"
qm create ${VM_ID} --memory ${VM_MEMORY} --net0 virtio,bridge=${NETWORK_BRIDGE} --scsihw virtio-scsi-pci --name "${VM_NAME}"

# Import disk to storage
STORAGE="local-lvm"
qm importdisk ${VM_ID} ${IMAGE_FILE} ${STORAGE}

# Attach disk to VM
qm set ${VM_ID} --scsi0 ${STORAGE}:vm-${VM_ID}-disk-0

# Add cloud-init drive
qm set ${VM_ID} --ide2 ${STORAGE}:cloudinit

# Set boot order
qm set ${VM_ID} --boot c --bootdisk scsi0

# Enable QEMU guest agent
qm set ${VM_ID} --agent enabled=1

# Setup keyboard configuration
SNIPPETS_DIR="/var/lib/vz/snippets"
KEYBOARD_SNIPPET="mac-german-keyboard.yaml"
KEYBOARD_LAYOUT="de"
KEYBOARD_VARIANT="mac"
KEYBOARD_MODEL="macintosh"
LOCALE="de_DE.UTF-8"
mkdir -p ${SNIPPETS_DIR}
cat << EOF > ${SNIPPETS_DIR}/${KEYBOARD_SNIPPET}
#cloud-config
keyboard:
  layout: ${KEYBOARD_LAYOUT}
  variant: ${KEYBOARD_VARIANT}
  model: ${KEYBOARD_MODEL}
locale: ${LOCALE}
runcmd:
  - localectl set-keymap ${KEYBOARD_LAYOUT}-${KEYBOARD_VARIANT}
  - dpkg-reconfigure -f noninteractive keyboard-configuration
  - apt update
  - apt install -y qemu-guest-agent
  - systemctl start qemu-guest-agent
EOF
qm set ${VM_ID} --cicustom "vendor=local:snippets/${KEYBOARD_SNIPPET}"

# Set user and password
qm set ${VM_ID} --ciuser ${CI_USER} --cipassword "${CI_PASSWORD}"

# Setup IP address
IP_CONFIG="ip=dhcp"
qm set ${VM_ID} --ipconfig0 ${IP_CONFIG}

# Copy SSH key
if [ ! -f ${SSH_KEY_PATH} ]; then
    echo "Error: SSH key ${SSH_KEY_PATH} not found"
    exit 1
fi
qm set ${VM_ID} --sshkeys ${SSH_KEY_PATH}

# Convert to template
qm template ${VM_ID}

# Clean up
rm ${IMAGE_FILE}

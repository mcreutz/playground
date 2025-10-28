#!/bin/bash

################################################################################
# Proxmox VM New Disk Setup Script
#
# This script partitions, formats, and mounts a new disk in a Proxmox VM.
# It creates a single partition using the entire disk, formats it with ext4,
# mounts it, and adds an entry to /etc/fstab for automatic mounting on boot.
#
# Usage: Run as root after modifying the configuration variables below
#        sudo ./setup_new_disk.sh
################################################################################

set -e  # Exit on any error
set -u  # Exit on undefined variable

#------------------------------------------------------------------------------
# CONFIGURATION - Modify these variables for your environment
#------------------------------------------------------------------------------

# The disk device (e.g., /dev/sdb, /dev/sdc, /dev/vdb)
# WARNING: Double-check this value! All data on this disk will be lost!
DISK_DEVICE="/dev/sdb"

# Mount point where the disk will be mounted
MOUNT_POINT="/mnt/data"

# Filesystem type
FILESYSTEM="ext4"

# Filesystem label (optional, can be empty)
FS_LABEL="data"

#------------------------------------------------------------------------------
# Script Logic - No need to modify below this line
#------------------------------------------------------------------------------

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "ERROR: This script must be run as root (use sudo)"
   exit 1
fi

# Verify the disk exists
if [[ ! -b "$DISK_DEVICE" ]]; then
    echo "ERROR: Disk ${DISK_DEVICE} does not exist!"
    exit 1
fi

# Check if disk is already mounted
if mount | grep -q "^${DISK_DEVICE}"; then
    echo "ERROR: Disk ${DISK_DEVICE} or its partitions are currently mounted!"
    exit 1
fi

# Check if disk has any existing partitions
EXISTING_PARTITIONS=$(lsblk -ln -o NAME "${DISK_DEVICE}" | tail -n +2)
if [[ -n "$EXISTING_PARTITIONS" ]]; then
    echo "ERROR: Disk ${DISK_DEVICE} already has partitions!"
    echo "This script only works with unpartitioned disks."
    echo "To wipe this disk, run: wipefs -a ${DISK_DEVICE}"
    exit 1
fi

# Partition the disk with GPT
echo "Creating GPT partition table..."
parted -s "${DISK_DEVICE}" mklabel gpt

echo "Creating partition..."
parted -s "${DISK_DEVICE}" mkpart primary "${FILESYSTEM}" 0% 100%

# Wait for the partition to be recognized by the kernel
sleep 2
partprobe "${DISK_DEVICE}"
sleep 2

# Determine the partition device name
# Handle both /dev/sdX1 and /dev/nvmeXn1p1 naming schemes
if [[ "${DISK_DEVICE}" =~ nvme ]]; then
    PARTITION="${DISK_DEVICE}p1"
else
    PARTITION="${DISK_DEVICE}1"
fi

# Verify partition was created
if [[ ! -b "$PARTITION" ]]; then
    echo "ERROR: Partition ${PARTITION} was not created successfully!"
    exit 1
fi

# Format the partition
echo "Formatting ${PARTITION}..."
if [[ -n "$FS_LABEL" ]]; then
    mkfs.${FILESYSTEM} -L "${FS_LABEL}" "${PARTITION}" > /dev/null 2>&1
else
    mkfs.${FILESYSTEM} "${PARTITION}" > /dev/null 2>&1
fi

# Get the UUID of the new partition
PARTITION_UUID=$(blkid -s UUID -o value "${PARTITION}")

# Create mount point if it doesn't exist
if [[ ! -d "$MOUNT_POINT" ]]; then
    mkdir -p "${MOUNT_POINT}"
fi

# Mount the partition
echo "Mounting ${PARTITION} to ${MOUNT_POINT}..."
mount "${PARTITION}" "${MOUNT_POINT}"

# Verify mount was successful
if ! mount | grep -q "${MOUNT_POINT}"; then
    echo "ERROR: Failed to mount partition!"
    exit 1
fi

# Add entry to /etc/fstab for automatic mounting on boot
if ! grep -q "${PARTITION_UUID}" /etc/fstab; then
    cp /etc/fstab /etc/fstab.backup.$(date +%Y%m%d_%H%M%S)
    echo "" >> /etc/fstab
    echo "# ${PARTITION} - Added by setup_new_disk.sh on $(date)" >> /etc/fstab
    echo "UUID=${PARTITION_UUID}  ${MOUNT_POINT}  ${FILESYSTEM}  defaults,nofail  0  2" >> /etc/fstab
    echo "Updated /etc/fstab"
fi

# Verify fstab entry works
umount "${MOUNT_POINT}"
mount -a

if ! mount | grep -q "${MOUNT_POINT}"; then
    echo "ERROR: Failed to mount using fstab entry!"
    exit 1
fi

echo "Done. Disk mounted at ${MOUNT_POINT}"

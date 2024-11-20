# Linux Logical Volume Manager (LVM)

## Overview
LVM provides flexible disk space management by creating abstractions of physical storage:
- **PV (Physical Volume)**: Physical disks or partitions that form the storage foundation
- **VG (Volume Group)**: Groups of PVs that form a storage pool, always spans one or more complete PVs
- **LV (Logical Volume)**: Virtual partitions created from VGs that can be formatted with a filesystem

### Key relationships between components:
Physical disk : partition -> 1 : N
- A physical disk can have one or more partitions. Partitions can only be part of one physical disk.

Physical disk/partition : Physical Volume -> 1 : 1  
- A PV is a single physical disk or partition.

Physical Volume : Volume Group -> N : 1
- A VG can span over one or more complete PVs. A PV can only be part of one VG.

Volume Group : Logical Volume -> 1 : N
- A VG can have one or more LVs. An LV can only be part of one VG.


## Physical Volumes (PV)
```bash
# List all PVs
pvs

# Create PV from disk or partition
pvcreate /dev/sdb  # Create PV from disk
pvcreate /dev/sdc1  # Create PV from partition

# Show PV info
pvs /dev/sdb  # Brief info
pvdisplay /dev/sdb  # Detailed info

# Remove PV
pvremove /dev/sdb

# Rename PV
pvrename /dev/sdb /dev/sdX

# Display PV UUID
blkid /dev/sdb
```

## Volume Groups (VG)
```bash
# List all VGs
vgs

# Create new VG from PV[s]
vgcreate vg_name /dev/sdb [/dev/sdc1]

# Add PV to existing VG
vgextend vg_name /dev/sdc1

# Show VG info
vgs vg_name  # Brief info
vgdisplay vg_name  # Detailed info

# Remove PV from VG (requires unmounting)
vgreduce vg_name /dev/sdb

# Remove VG
vgremove vg_name

# Rename VG
vgrename old_name new_name
```

## Logical Volumes (LV) 
```bash
# List all LVs
lvs

# Create LV with specific size
lvcreate -L 10G -n lv_name vg_name

# Create LV using all available space
lvcreate -l 100%FREE -n lv_name vg_name

# Show LV info
lvs /dev/vg_name/lv_name  # Brief info
lvdisplay /dev/vg_name/lv_name  # Detailed info

# Resize LV
lvextend -L +1G /dev/vg_name/lv_name  # Extend by 1GB
lvreduce -L -1G /dev/vg_name/lv_name  # Reduce by 1GB (requires unmounting)
lvextend -l +100%FREE /dev/vg_name/lv_name  # Extend to use all available space
lvextend -l +100%FREE /dev/vg_name/lv_name --resizefs  # Include filesystem resize
resize2fs /dev/vg_name/lv_name  # Extend ext4 fs, might be `/dev/mapper/...`
xfs_growfs /dev/vg_name/lv_name  # Extend xfs fs (only growing)

# Remove LV
lvremove /dev/vg_name/lv_name

# Rename LV
lvrename /dev/vg_name/old_name new_name
```

## Example Usage
### Create and Mount New LV
```bash
pvcreate /dev/sdb  # Create PV
vgcreate vg_data /dev/sdb  # Create VG
lvcreate -L 10G -n lv_data vg_data  # Create LV
mkfs.ext4 /dev/vg_data/lv_data  # Format LV with filesystem
mkdir /mnt/data
mount /dev/vg_data/lv_data /mnt/data  # Mount LV
```

### Remove LV, VG and PV
```bash
umount /mnt/data  # Unmount
lvremove /dev/vg_data/lv_data  # Remove LV
vgremove vg_data  # Remove VG
pvremove /dev/sdb  # Remove PV
```

## Additional Tips and Best Practices:
- Always leave free space in Volume Groups for future expansion or emergencies
- Always backup data before resizing
- Monitor free space with `vgs` and `lvs`
- LV paths are typically in `/dev/vg_name/lv_name`
- Use `lsblk` to see block device hierarchy
- Database servers: Separate LV for database files
- Web servers: Separate LV for web content
- Backup servers: Large LV for backup storage

### Directories that often get their own LV:
- / (root filesystem)
- /home (user data)
- /var (variable data, logs, mail spools)
- /var/log (system logs)
- /var/lib/mysql (database files)
- /opt (third-party applications)
- /usr/local (locally installed software)
- /tmp (temporary files)
- swap

## LV Snapshots and Backups
Snapshots are point-in-time copies of Logical Volumes using copy-on-write:
- Great for consistent backups and testing changes
- Temporary by nature - not a backup by itself
- Performance impact increases as snapshot fills up
- Size based on expected changes during snapshot lifetime

### Creating and Managing Snapshots
```bash
# Create 1GB snapshot of a LV
lvcreate -L 1G -s -n <snap_mountpath> /dev/<vg_name>/<lv_mountpath>

# Create snapshot with size relative to origin 
lvcreate -l 20%ORIGIN -s -n <snap_var> /dev/<vg_name>/<lv_var>

# View snapshots and usage
lvs -o +lv_size,lv_name,snap_percent

# Detailed snapshot info
lvdisplay /dev/vg_system/snap_root

# Merge snapshot back to original (revert to snapshot state)
lvconvert --merge /dev/vg_system/snap_root
# Note: Requires unmounting or reboot depending on LV

# Remove snapshot when done
lvremove /dev/<vg_name>/<snap_mountpath>

# Remove all snapshots of an LV
lvremove /dev/vg_system/lv_root -S
```

### Using Snapshots to Test Changes
```bash
# Create snapshot before major change
lvcreate -L 1G -s -n snap_test /dev/vg_system/lv_data

# If something goes wrong, revert to snapshot
lvconvert --merge /dev/vg_system/snap_test

# If all good, remove snapshot
lvremove /dev/vg_system/snap_test
```

### Snapshot monitoring
```bash
# Watch snapshot usage
watch -n 10 'lvs -o +snap_percent'

# Alert if snapshot nearly full
if [ $(lvs -o snap_percent --noheadings snap_root) -gt 80 ]; then
    echo "Warning: Snapshot nearly full"
fi
```

### Snapshot Sizing Guidelines
- Size based on expected changes during snapshot lifetime
- Too small = snapshot fails if it fills up
- Typical sizes: 10-20% of original LV
- Monitor usage with lvs command

### Snapshot Performance Impact
- Reads are fast, writes are slower
- Performance impact increases as snapshot fills up
- Monitor with iostat or vmstat commands

### Creating Backups from Snapshots and Restoring
```bash
# Create backup from snapshot
mkdir /mnt/snapshot  # Create mount point for snapshot
mount -o ro /dev/vg_system/snap_root /mnt/snapshot  # Mount snapshot read-only
tar czf /backup/data.tar.gz /mnt/backup/  # Create backup tarball
umount /mnt/backup  # Unmount snapshot
rmdir /mnt/backup  # Remove mount point

# Restore data from backup
mkdir /mnt/snapshot  # Create mount point for snapshot
tar xzf /backup/data.tar.gz -C /mnt/snapshot  # Extract backup tarball
rsync -av /mnt/snapshot/ /mnt/original/  # Restore data to LV
rmdir /mnt/snapshot  # Remove mount point
```

### Best Practices for Snapshots and Backups
- Size snapshots appropriately
- Keep snapshots temporary (hours/days, not weeks)
- Monitor snapshot usage
- Mount read-only unless changes needed
- Remove snapshots when no longer needed
- Don't use as backup replacement
- Consider performance impact

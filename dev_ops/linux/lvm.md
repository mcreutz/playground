# Linux Logical Volume Management (LVM) Cheatsheet

## Overview
LVM provides flexible disk space management by creating abstractions of physical storage:
- **PV (Physical Volume)**: Physical disks or partitions that form the storage foundation
- **VG (Volume Group)**: Groups of PVs that form a storage pool, always spans one or more complete PVs
- **LV (Logical Volume)**: Virtual partitions created from VGs that can be formatted with a filesystem

Key relationships between components:
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
# Create PV from disk or partition
pvcreate /dev/sdb
pvcreate /dev/sdc1

# Show PV info
pvs         # Brief info
pvdisplay   # Detailed info
```

## Volume Groups (VG)
```bash
# Create new VG from PV[s]
vgcreate vg_name /dev/sdb [/dev/sdc1]

# Add PV to existing VG
vgextend vg_name /dev/sdc1

# Show VG info
vgs         # Brief info  
vgdisplay   # Detailed info

# Remove PV from VG (requires unmounting)
vgreduce vg_name /dev/sdb
```

## Logical Volumes (LV) 

### Create LV
```bash
# Create LV with specific size
lvcreate -L 10G -n lv_name vg_name

# Create LV using all available space
lvcreate -l 100%FREE -n lv_name vg_name

# Show LV info
lvs         # Brief info
lvdisplay   # Detailed info
```

### Extend/Reduce LV
```bash
# Extend by 1GB
lvextend -L +1G /dev/vg_name/lv_name

# Reduce by 1GB (requires unmounting)
lvreduce -L -1G /dev/vg_name/lv_name

# Extend to use all available space
lvextend -l +100%FREE /dev/vg_name/lv_name
```

### Resize Filesystem After LV Changes
```bash
# For ext4
resize2fs /dev/vg_name/lv_name

# For xfs (only growing)
xfs_growfs /dev/vg_name/lv_name
```

### Create and Mount New LV
```bash
# Create PV
pvcreate /dev/sdb

# Create VG
vgcreate vg_data /dev/sdb

# Create LV
lvcreate -L 10G -n lv_data vg_data

# Format LV with filesystem
mkfs.ext4 /dev/vg_data/lv_data

# Mount LV
mkdir /mnt/data
mount /dev/vg_data/lv_data /mnt/data
```

### Remove LV, VG and PV
```bash
# Unmount
umount /mnt/data

# Remove LV
lvremove /dev/vg_data/lv_data

# Remove VG
vgremove vg_data

# Remove PV
pvremove /dev/sdb
```

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

### Snapshot Sizing Guidelines
- Size based on expected changes during snapshot lifetime
- Too small = snapshot fails if it fills up
- Typical sizes: 10-20% of original LV
- Monitor usage with lvs command

### Snapshot Performance Impact
- Reads are fast, writes are slower
- Performance impact increases as snapshot fills up
- Monitor with iostat or vmstat commands

### Snapshot monitoring
```bash
# Watch snapshot usage
watch -n 10 'lvs -o +snap_percent'

# Alert if snapshot nearly full
if [ $(lvs -o snap_percent --noheadings snap_root) -gt 80 ]; then
    echo "Warning: Snapshot nearly full"
fi
```

### Creating and Managing Backups from Snapshots
```bash
# Backup data fom snapshot
mkdir /mnt/snapshot
mount -o ro /dev/vg_system/snap_root /mnt/snapshot
tar czf /backup/data.tar.gz /mnt/backup/
umount /mnt/backup
rmdir /mnt/backup

# Restore data from backup
mkdir /mnt/snapshot
tar xzf /backup/data.tar.gz -C /mnt/snapshot
rsync -av /mnt/snapshot/ /mnt/original/
rmdir /mnt/snapshot
```

### Best Practices
- Size snapshots appropriately
- Keep snapshots temporary (hours/days, not weeks)
- Monitor snapshot usage
- Mount read-only unless changes needed
- Remove snapshots when no longer needed
- Don't use as backup replacement
- Consider performance impact

## Additional Tips and Best Practices:
- Always leave free space in Volume Groups for future expansion or emergencies
- Always backup data before resizing
- Monitor free space with `vgs` and `lvs`
- LV paths are typically in `/dev/vg_name/lv_name`
- Use `lsblk` to see block device hierarchy
- Database servers: Separate LV for database files
- Web servers: Separate LV for web content
- Backup servers: Large LV for backup storage

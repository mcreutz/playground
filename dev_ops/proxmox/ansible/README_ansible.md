# Ansible Disk Setup

Ansible version of `setup_new_disk.sh` for partitioning, formatting, and mounting new disks.

## Quick Start

1. Edit `inventory.ini` and add your hosts with inline disk configuration (⚠️ **WARNING**: all data on disk will be erased!)
   ```ini
   [proxmox_vms]
   vm1.example.com disk_device=/dev/sdb mount_point=/mnt/data fs_label=data
   vm2.example.com disk_device=/dev/sdc mount_point=/mnt/backup fs_label=backup
   ```

2. Run:
   ```bash
   ansible-playbook -i inventory.ini setup_new_disk.yml
   ```

## Usage Examples

**Different disks on different hosts (recommended):**
```bash
ansible-playbook -i inventory.ini setup_new_disk.yml
```

**Single host with inline vars:**
```bash
ansible-playbook setup_new_disk.yml -i "192.168.1.100," -e "disk_device=/dev/sdb mount_point=/mnt/data"
```

**Same config for all hosts (use disk_config.yml):**
```bash
ansible-playbook -i inventory.ini setup_new_disk.yml -e @disk_config.yml
```

**Local execution:**
```bash
ansible-playbook setup_new_disk.yml --connection=local -i localhost, --become -e "disk_device=/dev/sdb mount_point=/mnt/data"
```

## Notes

- Creates GPT partition table with single partition
- Formats with ext4 by default (configurable via `filesystem` var)
- Mounts and adds to /etc/fstab with UUID
- Backs up /etc/fstab before modification
- Fails safely if disk is already mounted or has existing partitions

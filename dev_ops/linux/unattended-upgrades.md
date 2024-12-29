# Unattended Upgrades

## Installation
```shell
apt install unattended-upgrades apt-listchanges update-notifier-common
```

## Configuration Files
- Main config: `/etc/apt/apt.conf.d/50unattended-upgrades`
- Auto-upgrades settings: `/etc/apt/apt.conf.d/20auto-upgrades`
- Update notifier config: `/etc/apt/apt.conf.d/10periodic`

## Key Configuration Options
```shell
# Enable automatic updates
dpkg-reconfigure -plow unattended-upgrades

# Check status
systemctl status unattended-upgrades
```

## Common Settings
File: `/etc/apt/apt.conf.d/50unattended-upgrades`
```shell
// Automatically download and install stable updates
Unattended-Upgrade::Allowed-Origins {
    "${distro_id}:${distro_codename}-security";
    "${distro_id}:${distro_codename}-updates";
};

// Auto reboot if needed
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-Time "02:00";
```

## Update Notifier Settings
File: `/etc/apt/apt.conf.d/10periodic`
```shell
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
```

## Logs and Troubleshooting
- Main log: `/var/log/unattended-upgrades/unattended-upgrades.log`
- Debug log: `/var/log/unattended-upgrades/unattended-upgrades-debug.log`

## Manual Operations
```shell
# Dry run
unattended-upgrades --dry-run

# Force check
unattended-upgrades --debug
```
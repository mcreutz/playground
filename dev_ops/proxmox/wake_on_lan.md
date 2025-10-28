# Setup WakeOnLan for a Proxmox server

## Setup BIOS for Wake-on-LAN support
todo

## Enable Wake-on-LAN on network interface
Find network interface name with `ip a` command
```sh
ip a
```

Install ethtool and enable Wake-on-LAN
```sh
apt install ethtool
ethtool -s <interface> wol g
```

## Make Wake-on-LAN setting persistent
```sh
nano /etc/systemd/system/wol.service
```

Add the following content to the file, replace <interface> with your network interface name
```ini
[Unit]
Description=Enable Wake-on-LAN

[Service]
Type=oneshot
ExecStart=/sbin/ethtool -s <interface> wol g

[Install]
WantedBy=multi-user.target
```

## Enable and start the service
```sh
systemctl enable wol.service
systemctl start wol.service
```
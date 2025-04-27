# Subnet routing on Linux

## Install Tailscale
see docs

## Add subnet routing
see: https://tailscale.com/kb/1019/subnets#connect-to-tailscale-as-a-subnet-router

start service with `sudo tailscale up --advertise-routes=192.0.2.0/24,198.51.100.0/24` (example)

## performance optimization for UDP
Indicated my this message: "Warning: UDP GRO forwarding is suboptimally configured on eth0, UDP forwarding throughput capability will increase with a configuration change."

see: https://tailscale.com/kb/1320/performance-best-practices#ethtool-configuration

```shell
NETDEV=$(ip -o route get 8.8.8.8 | cut -f 5 -d " ")
sudo ethtool -K $NETDEV rx-udp-gro-forwarding on rx-gro-list off
```

## Autmaically optimize UDP GRO forwarding on startup
```shell
sudo nano /etc/systemd/system/udp-gro-fix.service
```
Put the following in the file:
```ini
[Unit]
Description=Enable UDP GRO Forwarding Fix
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'NETDEV=$(ip -o route get 8.8.8.8 | cut -f 5 -d " "); ethtool -K $NETDEV rx-udp-gro-forwarding on rx-gro-list off'
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```shell
sudo systemctl daemon-reload
sudo systemctl enable udp-gro-fix.service
sudo systemctl start udp-gro-fix.service
```

## Activate the subnet routing in the Tailscale admin console
- Go to the Tailscale admin console
- Click on the machine you want to use as a subnet router
- "Edit routes"
- Check the box for the subnet you want to route

## Access the subnet from another machine
If you are on a Linux machine, you need to start Tailscale with the `--accept-routes` flag:
```shell
sudo tailscale up --accept-routes
```
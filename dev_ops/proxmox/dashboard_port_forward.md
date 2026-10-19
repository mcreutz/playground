route traffic from port 443 to 8006 for proxmox dashboard

test with
```sh
iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 8006
```

to persist, first check the current network interface (usually vmbr0)
```sh
ip -br addr
```

then edit the network interface configuration file `/etc/network/interfaces` by adding the following lines to the vmbr0 section (replace `192.168.x.x` with your proxmox host IP address):

```text
...
iface vmbr0 inet static
    ...
    # redirect port 443 to 8006 for proxmox dashboard
    post-up iptables -t nat -A PREROUTING -d 192.168.x.x -p tcp --dport 443 -j REDIRECT --to-port 8006 || true
```

helm repo add mojo2600 https://mojo2600.github.io/pihole-kubernetes/
helm repo update

kubectl create namespace pi-hole
helm install pi-hole mojo2600/pihole -n pi-hole



create nat rules from the hosts port 53 to the nodeport service of the pihole service
```bash
sudo nft add rule ip nat PREROUTING tcp dport 53 dnat 127.0.0.1:30053
sudo nft add rule ip nat PREROUTING udp dport 53 dnat 127.0.0.1:30053

sudo nft add rule nat PREROUTING tcp dport 53 redirect to 30053
sudo nft add rule nat PREROUTING udp dport 53 redirect to 30053

```

remove the port forwarding
```bash
iptables -t nat -D PREROUTING -p udp --dport 53 -j REDIRECT --to-port $nodeport_udp
iptables -t nat -D PREROUTING -p tcp --dport 53 -j REDIRECT --to-port $nodeport_tcp
```
or
```bash
iptables -t nat -L --line-numbers  # to get the line number
iptables -t nat -D PREROUTING 1  # to delete the rule
```
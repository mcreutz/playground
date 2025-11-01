# RKE2

## Install
```sh
curl -sfL https://get.rke2.io | sudo INSTALL_RKE2_VERSION=v1.34.1+rke2r1 sh -
systemctl enable rke2-server.service
systemctl start rke2-server.service
journalctl -u rke2-server -f
```

## Join node to cluster
```sh
# get token from master node
sudo cat /var/lib/rancher/rke2/server/node-token

# add token to new node config
sudo mkdir -p  /etc/rancher/rke2/
sudo touch /etc/rancher/rke2/config.yaml
sudo tee /etc/rancher/rke2/config.yaml << EOF
server: https://my-kubernetes-domain.com:9345
token: my-shared-secret
EOF
```



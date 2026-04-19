# RKE2

RKE2 uses **server** (control plane) and **agent** (worker) terminology.

Must have an odd number of server nodes for etcd quorum (3 recommended).

Critical config values (e.g. `cluster-cidr`) must match across all server nodes.

A full uninstall is needed before rejoining as a different role (worker ↔ master).

This installation assumes a LVM partition is used for the RKE2 data directory (`/mnt/rke2_data` in this example) to allow for easier management of disk space and snapshots. Adjust `data-dir` in the config if using a different setup.

## Install
Install RKE2 
```sh
# EITHER as a server (default)
curl -sfL https://get.rke2.io | sudo INSTALL_RKE2_VERSION=v1.35.2+rke2r1 sh -
# OR as an agent
curl -sfL https://get.rke2.io | sudo INSTALL_RKE2_TYPE="agent" INSTALL_RKE2_VERSION=v1.35.2+rke2r1 sh -
```

Configure
```sh
# Disable ingress controllers and snapshot tools
sudo mkdir -p /etc/rancher/rke2
sudo tee -a /etc/rancher/rke2/config.yaml > /dev/null <<EOF
ingress-controller: none

disable:
  - rke2-snapshot-controller
  - rke2-snapshot-controller-crd
  - rke2-snapshot-validation-webhook

data-dir: /mnt/rke2_data

kubelet-arg:
  # Reserve resources for Kubernetes components (kubelet, containerd, etc.)
  - "kube-reserved=cpu=500m,memory=1Gi,ephemeral-storage=5Gi"  
  # Reserve resources for OS system daemons (sshd, journald, etc.)
  - "system-reserved=cpu=500m,memory=1Gi,ephemeral-storage=10Gi"
  # (Optional but recommended) Explicitly tell the Kubelet what to enforce
  - "enforce-node-allocatable=pods"
EOF
```

Join an existing cluster
```sh
# get token from existing server node (auto-generated at install)
# optionally set a custom token in config.yaml before first install for easier automation
sudo cat /var/lib/rancher/rke2/server/node-token

# on the new node
sudo mkdir -p /etc/rancher/rke2/

# EITHER as a server node
sudo tee /etc/rancher/rke2/config.yaml << EOF
server: https://my-kubernetes-domain.com:9345
token: my-shared-secret
# tls-san: only needed on server nodes if accessing the API via a LB, DNS name,
# or IP that isn't the node's own. Not needed for agents or direct IP access.
tls-san:
  - my-kubernetes-domain.com
EOF

# OR as an agent node
sudo tee /etc/rancher/rke2/config.yaml << EOF
server: https://my-kubernetes-domain.com:9345
token: my-shared-secret
EOF
```

Start the service
```sh
# EITHER for the server
systemctl enable rke2-server.service  # will auto-start on boot
systemctl start rke2-server.service
journalctl -u rke2-server -f # view server logs, ctrl+c to exit
# OR for the agent
systemctl enable rke2-agent.service # will auto-start on boot
systemctl start rke2-agent.service
journalctl -u rke2-agent -f # view agent logs, ctrl+c to exit
```

Post-install setup (server nodes only):
- Kubeconfig is written to `/etc/rancher/rke2/rke2.yaml`
- `kubectl`, `crictl`, and `ctr` are installed at `/var/lib/rancher/rke2/bin/` (not on PATH by default)
```sh
echo 'export KUBECONFIG=/etc/rancher/rke2/rke2.yaml' >> ~/.bashrc
echo 'export PATH=$PATH:/var/lib/rancher/rke2/bin' >> ~/.bashrc
source ~/.bashrc
```


## Update RKE2
Update server nodes first, one at a time. Then update agent nodes.
Do not skip minor Kubernetes versions (version skew policy applies).

### Manual update (re-run installer)
```sh
# on each server node (one at a time)
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
curl -sfL https://get.rke2.io | sudo INSTALL_RKE2_VERSION=v1.35.2+rke2r1 sh -
systemctl restart rke2-server
kubectl uncordon <node-name>

# on each agent node
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
curl -sfL https://get.rke2.io | sudo INSTALL_RKE2_TYPE="agent" INSTALL_RKE2_VERSION=v1.35.2+rke2r1 sh -
systemctl restart rke2-agent
kubectl uncordon <node-name>
```
Omit `INSTALL_RKE2_VERSION` to update to the latest stable release.

### Automated update (system-upgrade-controller)
```sh
# install the controller
kubectl apply -f https://github.com/rancher/system-upgrade-controller/releases/latest/download/crd.yaml \
  -f https://github.com/rancher/system-upgrade-controller/releases/latest/download/system-upgrade-controller.yaml
```
Then apply the update plans:
```sh
kubectl apply -f upgrade-server-plan.yaml -f upgrade-agent-plan.yaml
```
See [upgrade-server-plan.yaml](upgrade-server-plan.yaml) and [upgrade-agent-plan.yaml](upgrade-agent-plan.yaml).
The agent plan's `prepare` step waits for the server plan to complete before updating agents.
Replace `channel` with `version: v1.35.2+rke2r1` to pin a specific version.


## Remove RKE2 from a node

```sh
# on a server node
kubectl delete node <node-name>

# on the node to remove — fully uninstall RKE2
# tarball installs:
/usr/local/bin/rke2-uninstall.sh
# rpm installs:
/usr/bin/rke2-uninstall.sh
```
This shuts down RKE2 processes and removes binaries, systemd units, data dirs, CNI config, and iptables rules.



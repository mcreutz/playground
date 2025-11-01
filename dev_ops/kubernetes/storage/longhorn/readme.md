Check if your distro uses multipathd
```shell
sudo systemctl status multipathd
```

If yes, disable multipathd on each node (not done by longhornctl)
```shell
sudo systemctl stop multipathd
sudo systemctl stop multipathd.socket
sudo systemctl disable multipathd
sudo reboot
```

Setup Kubernetes on the nodes and join the cluster, example for MicroK8s
```shell
sudo snap install microk8s --classic
sudo microk8s add-node  # on the first node
sudo microk8s join ... # on the other nodes
# create local .kubeconfig file
mkdir -p ~/.kube
sudo microk8s config > ~/.kube/microk8s.kubeconfig
```

Prepare nodes for Longhorn installation (needs to be run on one node only)
```shell
# Install lonhorn cli: for AMD64 platform
curl -sSfL -o longhornctl https://github.com/longhorn/cli/releases/download/v1.10.0/longhornctl-linux-amd64
# Install lonhorn cli: for ARM platform
curl -sSfL -o longhornctl https://github.com/longhorn/cli/releases/download/v1.10.0/longhornctl-linux-arm64
chmod +x longhornctl
./longhornctl check preflight --kubeconfig path/to/kubeconfig
./longhornctl install preflight --kubeconfig path/to/kubeconfig
./longhornctl check preflight --kubeconfig path/to/kubeconfig
sudo reboot
```

Add the helm repo (on dev machine)
```shell
helm repo add longhorn https://charts.longhorn.io
helm repo update
```

Install Longhorn
```shell
helm upgrade --install longhorn longhorn/longhorn \
    --namespace longhorn-system \  # must be this namespace
    --create-namespace \
    --version 1.10.0 \
    --values dev_ops/kubernetes/storage/longhorn/values.yaml
```

Uninstall Longhorn
```shell
kubectl -n longhorn-system edit settings.longhorn.io deleting-confirmation-flag
# alternatively use checkbox in Longhorn UI, settings, general, delete confirmation
helm delete longhorn -n longhorn-system
kubectl delete namespace longhorn-system
```



ToDo:
- Automatic file system trimming, recurring job? -> kubelet metrics show correct volume size
- Test RWX volumes
- Volume resizing
- Backups

- namespace longhorn-system needed to be present for preflight check?
- do the automated stuff for installation survive reboots?


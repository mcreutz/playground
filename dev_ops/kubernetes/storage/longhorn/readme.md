Disable multipathd on each node
```shell
sudo systemctl stop multipathd
sudo systemctl stop multipathd.socket
sudo systemctl disable multipathd
sudo reboot
```

Prepare nodes for Longhorn installation (needs to be run on one node only)
```shell
# create .kubeconfig file (example for microk8s)
mkdir -p ~/.kube
sudo microk8s config > ~/.kube/microk8s.kubeconfig

# For AMD64 platform
curl -sSfL -o longhornctl https://github.com/longhorn/cli/releases/download/v1.7.2/longhornctl-linux-amd64
# For ARM platform
curl -sSfL -o longhornctl https://github.com/longhorn/cli/releases/download/v1.7.2/longhornctl-linux-arm64

chmod +x longhornctl
./longhornctl install preflight  --kube-config ~/.kube/microk8s.kubeconfig
./longhornctl check preflight  --kube-config ~/.kube/microk8s.kubeconfig
```

Add helm repo (on dev machine)
```shell
helm repo add longhorn https://charts.longhorn.io
helm repo update
```

Install Longhorn
```shell
kubectl create namespace longhorn-system
helm install longhorn longhorn/longhorn \
    --namespace longhorn-system \
    --version 1.7.2 \
    --values dev_ops/kubernetes/storage/longhorn/values.yaml
```

Uninstall Longhorn
```shell
kubectl -n longhorn-system edit settings.longhorn.io deleting-confirmation-flag
# alternatively use checkbox in Longhorn UI, settings, general, delete confirmation
helm delete longhorn -n longhorn-system
kubectl delete namespace longhorn-system
```




what are the most common problems reported for the k8s storage provider longhorn?

Answer:
The most common problems reported for the Kubernetes storage provider Longhorn are:
- Attachment issues: Volumes may get stuck during attaching and detaching processes1
- Data loss: If a pod or VM is down for some time and the PVC is detached, data can be lost due to lack of replication for detached PVCs9
- Performance issues: Disk latency can cause timeouts and performance problems1
- Storage inefficiency: Nested storage virtualization can lead to storage overhead1
- Mounting delays: Volumes with many files/directories can take a long time to finish mounting, especially when using fsGroup in the pod's security context2
- Snapshot and backup complications: Users report difficulties in using snapshots and working with backups effectively9
- Drive corruption: Some users have experienced drive corruption issues6
- Failure to mount: Volumes sometimes fail to mount properly6
- Node recovery problems: There have been reports of unrecoverable nodes upon reboot6
- Size limitations: Hardcoded rebuild limits and practical size constraints can cause issues1

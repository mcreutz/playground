Prepare nodes
```shell
sudo apt update
sudo apt install nfs-common open-iscsi
sudo modprobe iscsi_tcp
```

Add helm repo
```shell
helm repo add longhorn https://charts.longhorn.io
helm repo update
```

Install Longhorn
```shell
kubectl create namespace longhorn-system
helm install longhorn longhorn/longhorn \
    --namespace longhorn-system \
    --version 1.7.1 \
    --values dev_ops/kubernetes/storage/longhorn/values.yaml

Uninstall Longhorn
```shell
kubectl -n longhorn-system edit settings.longhorn.io deleting-confirmation-flag
# alternatively use checkbox in Longhorn UI, settings, general, delete confirmation
helm delete longhorn -n longhorn-system
kubectl delete namespace longhorn-system
```
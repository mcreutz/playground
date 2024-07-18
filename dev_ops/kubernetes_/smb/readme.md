# Connecting to SMB Shares in Kubernetes
## Add Helm Repo for CSI Driver
```bash
helm repo add csi-driver-smb https://raw.githubusercontent.com/kubernetes-csi/csi-driver-smb/master/charts
```

## Install Helm Chart for CSI Driver
```bash
helm install csi-driver-smb csi-driver-smb/csi-driver-smb --namespace kube-system --version v1.14.0 --set linux.kubelet="/var/snap/microk8s/common/var/lib/kubelet"
```
`--set linux.kubelet="..."` is required for MicroK8s, as it uses a different path for the kubelet.

## Wait for the driver to be installed
```bash
kubectl wait --for=condition=ready pod -n kube-system -l app=csi-smb-controller
kubectl wait --for=condition=ready pod -n kube-system -l app=csi-smb-node
```

## Create a secret for the SMB server credentials
```bash
kubectl create secret generic <secret-name> --from-literal username='<user-name>' --from-literal password='<password>' -n <secret-namespace>
```

## Create PV and PVC
```bash
kubectl create -f pv-smb.yaml
kubectl create -f pvc-smb.yaml -n <pvc-namespace>
```

## Uninstall

```bash
# First, delete all workloads that use the PV and PVC
# <...>

# Delete PV and PVC
kubectl delete -f pvc-smb.yaml -n <pvc-namespace>
kubectl delete -f pv-smb.yaml

# Delete secret
kubectl delete secret <secret name> -n <secret-namespace>

# Delete CSI driver for SMB
helm uninstall csi-driver-smb -n kube-system
```
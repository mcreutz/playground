# Install MinIO Helm chart
Add helm repository
```shell
helm repo add minio https://charts.min.io/
helm repo update
```

Create Kubernetes namespace
```shell
kubectl create ns minio
```

Install or upgrade the MinIO Helm chart
```shell
helm upgrade --install mino minio/minio \
    --version 5.4.0 \
    --namespace minio \
    --values dev_ops/kubernetes/storage/minio/values.yaml
```

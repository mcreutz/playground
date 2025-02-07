# Install MinIO Helm chart
Create Kubernetes namespace
```shell
kubectl create ns minio
```

Add helm repository
```shell
helm repo add minio https://charts.min.io/
helm repo update
```

Install or upgrade the MinIO Helm chart
```shell
helm upgrade --install minio minio/minio \
    --version 5.4.0 \
    --namespace minio \
    --values dev_ops/kubernetes/storage/minio/values.yaml
```

Todo
- Grafana dashboard
- Prometheus alerts
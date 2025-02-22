# Install Postgres Helm chart
Create Kubernetes namespace
```shell
kubectl create ns postgres
```

Install Helm chart
```shell
helm upgrade --install postgres oci://registry-1.docker.io/bitnamicharts/postgresql \
    --version 16.4.9 \
    --values dev_ops/kubernetes/storage/postgres/values.yaml \
    --namespace postgres
```

Todo
- Grafana dashboard
- Prometheus alerts
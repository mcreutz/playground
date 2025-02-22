Add helm repos
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

Create namespace
```bash
kubectl create ns monitoring                                         
```

Install kube-prometheus-stack
```bash
helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
    --version 69.4.1 \
    -n monitoring \
    -f dev_ops/kubernetes/monitoring/my_stack/prometheus_values.yaml
```

Install Promtail
```bash
helm upgrade --install promtail grafana/promtail \
    --version 6.16.6 \
    -n monitoring \
    -f dev_ops/kubernetes/monitoring/my_stack/promtail_values.yaml
```

Install Loki
```bash
helm upgrade --install loki grafana/loki \
    --version 6.27.0 \
    -n monitoring \
    -f dev_ops/kubernetes/monitoring/my_stack/loki_values.yaml
```

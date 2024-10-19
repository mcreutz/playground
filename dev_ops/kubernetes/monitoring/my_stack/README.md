helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update


Install kube-prometheus-stack
```bash
kubectl create ns monitoring                                         
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
    --version 60.4.0 \
    -n monitoring \
    -f dev_ops/kubernetes/monitoring/my_stack/prometheus_values.yaml
```

Install additional pod- and service-monitors
```bash
kubectl apply -f ./additional_objects/pod_monitor.yaml
kubectl apply -f ./additional_objects/service_monitor.yaml
```

Install additional Grafana dashboards
```bash
kubectl apply -f ./additional_objects/grafana_dashboards.yaml
```

Install Promtail
```bash
helm install promtail grafana/promtail \
    --version 6.16.0 \
    -n monitoring \
    -f dev_ops/kubernetes_/monitoring/my_stack/promtail_values.yaml
```

Install Loki
```bash
helm install loki grafana/loki \
    --version 6.6.4 \
    -n monitoring \
    -f dev_ops/kubernetes_/monitoring/my_stack/loki_values_dev.yaml
```

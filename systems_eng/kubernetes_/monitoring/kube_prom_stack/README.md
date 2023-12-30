Install kube-prometheus-stack
```bash
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring
```

Install additional Prometheus instance for application monitoring
```bash
kubectl apply -f ./additional_objects/prometheus.yaml
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
helm install promtail grafana/promtail -n monitoring -f ./promtail_values.yaml
```

Install Loki
```bash
helm install loki grafana/loki -n monitoring -f ./loki_values.yaml
```

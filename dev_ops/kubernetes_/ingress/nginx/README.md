# Ingress
## For microk8s, if not already enabled, enable the ingress controller addon:
```bash
sudo microk8s enable ingress
```

## For other Kubernetes distros, install the Nginx Ingress Controller using Helm:
```bash
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

```bash
kubectl create ingress grafana \
  --class=nginx \
  --rule="demo.localdev.me/*=demo:80"
```


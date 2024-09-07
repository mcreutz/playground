# Ingress
## Install the Nginx Ingress Controller
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


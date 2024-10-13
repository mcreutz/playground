# Nginx Ingress Controller
## For microk8s, if not already enabled, enable the ingress controller addon:
```bash
sudo microk8s enable ingress
```

## As a general way, install the Nginx Ingress Controller using Helm:
```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx \
  -n ingress-nginx \
  -f dev_ops/kubernetes_/ingress/nginx_ingress_controller/nginx_values_baremetal.yaml
  --version 4.11.2
```

## Todo
- SSL termination
- TCP ingress
- basic auth


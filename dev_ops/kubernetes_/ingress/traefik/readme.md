https://github.com/traefik/traefik-helm-chart/blob/master/EXAMPLES.md

helm repo add traefik https://traefik.github.io/charts
helm repo update
kubectl create ns traefik
helm install traefik traefik/traefik -v 32.1.0 -n traefik -f dev_ops/kubernetes_/ingress/traefik/traefik_values.yaml
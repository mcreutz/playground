Deploy ArgoCD helm chart
```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update     
kubectl create namespace argocd
helm install argocd argo/argo-cd \
    --namespace argocd \
    --version 7.6.12 \
    --values values.yaml
```

Get the password for the ArgoCD UI
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
```shell
# Add repo
helm repo add k8sgpt https://charts.k8sgpt.ai/
helm repo update
# Install chart
helm install k8sgpt k8sgpt/k8sgpt-operator \
    -n k8sgpt \
    -f ai/k8sgpt/values.yaml \
    --create-namespace
```

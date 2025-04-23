kubectl create secret generic kagent-openai -n kagent --from-literal OPENAI_API_KEY=xxx

helm upgrade --install kagent oci://ghcr.io/kagent-dev/kagent/helm/kagent \
    --version 0.1.15 \
    --namespace kagent \
    --values dev_ops/kubernetes/ai/kagent/values.yaml
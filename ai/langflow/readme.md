# repo
helm repo add langflow https://langflow-ai.github.io/langflow-helm-charts
helm repo update

# ide
helm upgrade --install langflow-ide langflow/langflow-ide \
    -n langflow \
    --version 0.1.1     \
    --values ai/langflow/ide-values.yaml \
    --create-namespace

# runtime
helm upgrade --install langflow-runtime langflow/langflow-runtime \
    -n langflow \
    --version 0.1.1     \
    --values ai/langflow/runtime-values.yaml \
    --create-namespace
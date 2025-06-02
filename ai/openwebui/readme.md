helm repo add open-webui https://helm.openwebui.com/
helm repo update

helm upgrade --install open-webui open-webui/open-webui \
    --namespace open-webui \
    --create-namespace \
    --version 6.16.0 \
    --values ai/openwebui/openwebui_values.yaml
helm repo add open-webui https://helm.openwebui.com/
helm repo update

kubectl create namespace open-webui
helm upgrade --install open-webui open-webui/open-webui \
    --namespace open-webui \
    --values ai/openwebui/openwebui_values.yaml
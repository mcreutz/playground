helm repo add ollama-helm https://otwld.github.io/ollama-helm/
helm repo update
helm upgrade --install ollama ollama-helm/ollama \
  --version 1.17.0 \
  --namespace langflow \
  --create-namespace \
  --values ai/ollama/values.yaml

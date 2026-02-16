# First, install the required CRDs
helm upgrade --install kagent-crds oci://ghcr.io/kagent-dev/kagent/helm/kagent-crds -n kagent --create-namespace

# Then install Kagent with default provider 
# --set providers.default=openAI enabled by default, but you need to provide your openAI apikey
helm upgrade --install kagent oci://ghcr.io/kagent-dev/kagent/helm/kagent -n kagent -f kagent_values.yaml

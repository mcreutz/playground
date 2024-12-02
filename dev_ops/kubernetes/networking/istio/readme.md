## Install with helm charts
```shell
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
kubectl create namespace istio-system
helm install istio-base istio/base -n istio-system
helm install istiod istio/istiod -n istio-system

# Install the ingress gateway
# create namespace istio-ingress
helm install istio-ingressgateway istio/gateway \
    -n istio-system # -n istio-ingress
    --values values_ingressgateway.yaml
```

Add label to namespaces to enable automatic sidecar injection
```shell
kubectl label <namespace> default istio-injection=enabled
```
OR enable automatic sidecar injection for all namespaces in the istiod helm chart
```shell
--set enableNamespacesByDefault=true
```



## Install Kiali
```shell
helm repo add kiali https://kiali.org/helm-charts
helm repo update

# Install Kiali operator
kubectl create namespace kiali-operator
helm install \
    --namespace kiali-operator \
    kiali-operator \
    kiali/kiali-operator \
    --set cr.create=true \
    --set cr.namespace=istio-system \
    --set cr.spec.auth.strategy="anonymous"

# OR install Kiali server directly
helm install \
    --namespace istio-system \
    kiali-server \
    kiali/kiali-server \
    --set server.web_fqdn=example.com
```

Kiali needs the `app`-label to be set on the deployments to work properly.

# Kubernetes Gateway API

The Gateway API is the successor to the Ingress API, providing a more expressive and extensible way to manage traffic into a Kubernetes cluster. It supports HTTP, HTTPS, TCP, TLS, and UDP routing through a consistent set of resources.

## API channels

| Channel | CRD bundle | Includes |
|---|---|---|
| **Standard** | `standard-install.yaml` | `GatewayClass`, `Gateway`, `HTTPRoute`, `GRPCRoute`, `ReferenceGrant` |
| **Experimental** | `experimental-install.yaml` | All standard resources + `TCPRoute`, `TLSRoute`, `UDPRoute`, `BackendTLSPolicy` |

Use the experimental bundle if you need `TCPRoute` or `TLSRoute` (e.g. raw TCP proxying via Traefik).

## Installation

> **Use `--server-side`** — some Gateway API CRDs (notably `HTTPRoute`) exceed the 262144-byte annotation limit that client-side `kubectl apply` imposes.

```bash
# Standard channel
kubectl apply --server-side -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/standard-install.yaml

# Experimental channel (superset of standard – pick one)
kubectl apply --server-side -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/experimental-install.yaml
```

## Verify

```bash
kubectl get crd | grep gateway.networking.k8s.io
```

Expected output includes:
```
gatewayclasses.gateway.networking.k8s.io
gateways.gateway.networking.k8s.io
httproutes.gateway.networking.k8s.io
tcproutes.gateway.networking.k8s.io      # experimental only
tlsroutes.gateway.networking.k8s.io      # experimental only
```


## Removal

```bash
# Standard channel
kubectl delete -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/standard-install.yaml

# Experimental channel
kubectl delete -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/experimental-install.yaml
```

> **Warning:** deleting the CRDs will also delete all `Gateway`, `HTTPRoute`, `TLSRoute`, etc. objects in the cluster. Drain/remove dependent resources first.

## References

- [Gateway API docs](https://gateway-api.sigs.k8s.io/)
- [GitHub releases](https://github.com/kubernetes-sigs/gateway-api/releases)
- [API reference](https://gateway-api.sigs.k8s.io/reference/spec/)

# Traefik v3 - Wildcard TLS, Let's Encrypt DNS-01 (Cloudflare)

Bare-metal single-node setup. Traefik handles ACME directly (no cert-manager). Wildcard cert `*.example.com` via Cloudflare DNS-01. Serves both standard `Ingress` and Gateway API (`HTTPRoute`, `TLSRoute`) from the same cert.

`hostNetwork: true` + `strategy: Recreate` -- required because multiple pods can't bind the same host ports simultaneously.

Gateway API experimental CRDs (v1.5.1) and `gateway.yaml` are applied automatically via the Helmfile `postsync` hook (or manually before `helm install`).

---

## Setup

### 1. Label the ingress node and create the Cloudflare secret

```bash
kubectl label node <node> ingress-node=true   # pin pod; match service.externalIPs in values
kubectl create namespace traefik
kubectl create secret generic cloudflare-api-token \
  --namespace traefik \
  --from-literal=api-token='<token>' # Needs Zone:DNS:Edit and Zone:Zone:Read
```

### 2. Install
```bash
kubectl apply --server-side -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.1/experimental-install.yaml
kubectl apply -f gateway.yaml
helm repo add traefik https://traefik.github.io/charts && helm repo update
helm upgrade --install traefik traefik/traefik \
  --namespace traefik --values traefik_values.yaml --version 39.0.5
```

Use the staging CA (`https://acme-staging-v02.api.letsencrypt.org/directory`) in `traefik_values.yaml` while testing to avoid LE rate limits. When switching to production, see below.

### 3. Verify certificate issuance

Watch Traefik logs immediately after deploy -- cert issuance should start within seconds, if an ingress or similar uses it:

Check the current cert being served (should show issuer `Let's Encrypt` once issued):
```bash
echo | openssl s_client -connect <node-ip>:443 -servername <your-domain> 2>/dev/null | openssl x509 -noout -issuer -dates
```

---

## Switching CA or email (clearing acme.json)

When changing `caServer` or `acme.email`, the cached cert is stale -- Traefik won't re-issue it automatically.

```bash
kubectl exec -n traefik deploy/traefik -- sh -c 'echo "{}" > /data/acme.json'
kubectl rollout restart deployment/traefik -n traefik
```

New cert issued within ~60 seconds. Traefik serves its self-signed fallback in the meantime.

---

## Uninstall

```bash
helm uninstall traefik -n traefik
kubectl delete -f gateway.yaml
kubectl get crds -o name | grep traefik.io | xargs kubectl delete
kubectl delete -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.1/experimental-install.yaml

## Files

| File | Purpose |
|---|---|
| `traefik_values.yaml` | Helm values -- ACME, entrypoints, hostNetwork, Gateway API provider |
| `gateway.yaml` | Gateway with HTTPS + TCP listeners (applied via Helmfile hook) |
| `ingress-app-a.yaml` | `Ingress` example |
| `httproute-app-b.yaml` | `HTTPRoute` example |
| `tlsroute-postgres-a/b.yaml` | `TLSRoute` examples -- SNI-based TCP routing, multiple PostgreSQL instances on port 5432 |

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Pod stuck `Pending` | Another process holds host ports 80/443/5432, or multiple nodes labeled `ingress-node=true` |
| `CF_DNS_API_TOKEN` empty | Secret key mismatch -- verify `kubectl get secret -n traefik cloudflare-api-token -o yaml` |
| DNS challenge fails | Check token permissions (Zone:DNS:Edit); check resolvers can reach 1.1.1.1:53 |
| Rate limited by Let's Encrypt | Switch to staging CA; existing certs are cached and won't re-issue until cleared |
| Browser shows self-signed cert after CA change | Clear `acme.json` -- see above |
| `TLSRoute` not working | Verify `experimentalChannel: true` and `postgres` listener has `protocol: TLS, mode: Terminate` |
| `Gateway` stuck `Pending` | GatewayClass `traefik` not ready; wait or re-run install |

---

## References

- [Traefik ACME docs](https://doc.traefik.io/traefik/https/acme/)
- [Traefik Gateway API provider](https://doc.traefik.io/traefik/routing/providers/kubernetes-gateway/)
- [Gateway API](https://gateway-api.sigs.k8s.io/)

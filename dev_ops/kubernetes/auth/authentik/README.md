# authentik on Kubernetes — hello world

A minimal authentik install (server + worker + bundled PostgreSQL). Connected
apps are declared statically in `connected_apps_blueprint.yaml` and loaded by the
chart's native blueprint support — no sidecar, no auto-reload, no GitOps.

> authentik 2026.x requires **only PostgreSQL** — Redis was replaced by a
> Postgres-backed cache and task queue, so there is nothing else to run.

## Generate secrets

Put the output into `authentik_values.yaml` (`secret_key` and the two passwords):

```sh
pwgen -s 50 1                  # secret_key
openssl rand 60 | base64 -w 0  # postgres password
```

## Install

The blueprint ConfigMap must exist before the worker starts (the chart mounts it
as a volume), so apply it first:

```sh
kubectl create namespace authentik
kubectl apply -f connected_apps_blueprint.yaml

helm repo add authentik https://charts.goauthentik.io
helm repo update

helm upgrade --install authentik authentik/authentik --version 2026.5.3 \
  -n authentik -f authentik_values.yaml
```

The worker discovers and applies the blueprint automatically. Check it landed:

```sh
kubectl -n authentik logs deploy/authentik-worker | grep -i blueprint
```

## Connected apps

All connected apps live in `connected_apps_blueprint.yaml` (referenced from
`authentik_values.yaml` under `blueprints.configMaps`). It currently defines the
`pk_admins` / `pk_users` groups and a Grafana OAuth2 provider + application.

To add or change an app, edit that file and re-apply:

```sh
kubectl apply -f connected_apps_blueprint.yaml
```

The worker re-applies modified blueprints within ~60 min; to apply immediately,
restart it: `kubectl -n authentik rollout restart deploy/authentik-worker`.

## Example consumer: Grafana via authentik OAuth

`grafana_values.yaml` is the Grafana-side OAuth client config that pairs with the
provider above.

```sh
helm repo add grafana-community https://grafana-community.github.io/helm-charts
helm repo update

helm upgrade --install grafana grafana-community/grafana \
  -n grafana -f grafana_values.yaml --create-namespace
```

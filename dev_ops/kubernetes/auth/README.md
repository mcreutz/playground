minikube delete   

minikube start --disk-size=20g

minikube addons enable storage-provisioner
minikube addons enable default-storageclass

minikube addons enable ingress
minikube addons enable ingress-dns

minikube addons enable metrics-server

echo "$(minikube ip) minikube.test authentik.minikube.test" | sudo tee -a /etc/hosts

pwgen -s 50 1
openssl rand 60 | base64 -w 0


helm repo add authentik https://charts.goauthentik.io
helm repo update

helm upgrade --install authentik authentik/authentik -n authentik -f authentik_values.yaml --create-namespace


helm repo add grafana-community https://grafana-community.github.io/helm-charts
helm repo update

helm upgrade --install grafana grafana-community/grafana -n grafana -f grafana_values.yaml --create-namespace

k apply -f grafana_blueprint.yaml -n authentik    
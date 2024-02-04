## Basic commands
```bash
minikube profile list
minikube start 
minikube status
minikube stop
minikube delete
```

## Nodes
```bash
minikube node list
minikube node add
minikube node remove
```

## Global configuration
```bash
minikube config view
minikube config set memory 8192
minkube config set cpus 6
```

## Run minikube instance on cloud vm
```bash
minikube start --cpus="no-limit" --memory="no-limit" --listen-address="127.0.0.1" --nodes=3 --ports=8443 --embed-certs=true --driver=docker --apiserver-ips="127.0.0.1" --accept-hosts='.*'

kubectl proxy -p 8443 --accept-hosts='.*' --address='0.0.0.0'
```
- allow incoming traffic on port 8443
- copy ~/.kube/config to local machine and replace server with http://<cloud-vm-ip>:8443
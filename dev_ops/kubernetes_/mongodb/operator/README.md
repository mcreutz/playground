# Install a MongoDB instance using the MongoDB Community Operator
This will install the MongoDB Community Operator into a new namespace and create a MongoDB instance in another namespace.

## Install MongoDB Community Operator
```bash
helm repo add mongodb https://mongodb.github.io/helm-charts
helm install community-operator mongodb/community-operator --namespace mongodb-operator --create-namespace --set operator.watchNamespace="*"
```

## Create the namespace for MongoDB instance
```bash
kubectl create namespace mongodb
```

## Install RBAC components for MongoDB instance
```bash
kubectl create -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/rbac/service_account_database.yaml -n mongodb
kubectl create -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/rbac/role_database.yaml -n mongodb
kubectl create -f https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/rbac/role_binding_database.yaml -n mongodb
```

## Create a MongoDB instance
```bash
kubectl create -f ./mongodb.yaml -n mongodb
```

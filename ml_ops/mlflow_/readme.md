Run MLflow in docker
```shell
docker run -p 5050:5000 --entrypoint "mlflow" bitnami/mlflow:latest server --host 0.0.0.0
```

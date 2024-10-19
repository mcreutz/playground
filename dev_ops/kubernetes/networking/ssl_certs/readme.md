Install cert-manager
```shell
# For mirok8s do:
sudo microk8s enable cert-manager
```

Create a secret with an api token for your domain provider
```shell
kubectl create secret generic cloudflare-api-token-secret \
  --namespace cert-manager \
  --from-literal=api-token='<cloudflare-api-token>'
```

Create the cluster issuer and a certificate. As Let's Encrypt has rate limits, it is recommended to use the staging issuer for testing purposes. 
```shell
kubectl create -f dev_ops/kubernetes/networking/ssl_certs/cluster_issuer_staging.yaml
kubectl create -f certificate_staging.yaml -n cert-manager
```

Check the status of the certificate
```shell
kubectl get certificate my-service-tls
```

If the certificate is ready, you can use it in an ingress
```shell
kubectl create -f dev_ops/kubernetes/networking/ssl_certs/ingress_demo.yaml
```

If that works, you can create a production certificate.

Remove the staging issuer and certificate and create the production issuer
```shell
kubectl delete -f dev_ops/kubernetes/networking/ssl_certs/certificate_staging.yaml -n cert-manager
kubectl delete -f dev_ops/kubernetes/networking/ssl_certs/cluster_issuer_staging.yaml
kubectl create -f dev_ops/kubernetes/networking/ssl_certs/cluster_issuer.yaml
```

Add the annotation to the ingress as shown in the ingress_demo.yaml file and the Ingress controller will automatically instruct cert-manager to request a certificate if not present.#

Install cert-manager
```shell
# For microk8s do:
sudo microk8s enable cert-manager
```

Create an api token at your domain registrar. For Cloudflare, create an API token with the following permissions:
- Zone:Zone:Read
- Zone:DNS:Edit

Then create a secret with that api token
```shell
kubectl create secret generic cloudflare-api-token-secret \
  --namespace cert-manager \
  --from-literal=api-token='<cloudflare-api-token>'
```

Create a cluster issuer and a certificate. As Let's Encrypt has tight rate limits, it is recommended to use a staging issuer for testing purposes. 
```shell
kubectl create -f dev_ops/kubernetes/networking/cert-manager/lets-encrypt/cluster_issuer_staging.yaml
kubectl create -f dev_ops/kubernetes/networking/cert-manager/lets-encrypt/certificate_staging.yaml -n cert-manager
```

Check the status of the certificate
```shell
kubectl get certificate my-service-tls
```

When the certificate is ready, you can use it in an ingress
```shell
kubectl create -f dev_ops/kubernetes/networking/ssl_certs/ingress_demo.yaml
```

If that works, you can move to an actual production certificate.

Remove the staging issuer and certificate and create the production issuer
```shell
kubectl delete -f dev_ops/kubernetes/networking/ssl_certs/certificate_staging.yaml -n cert-manager
kubectl delete -f dev_ops/kubernetes/networking/ssl_certs/cluster_issuer_staging.yaml
kubectl create -f dev_ops/kubernetes/networking/ssl_certs/cluster_issuer.yaml
```

Either create the certificate manually
```shell
kubectl create -f dev_ops/kubernetes/networking/ssl_certs/certificate.yaml -n <your-apps-namespace>
```

or add the cert-manager annotation to the ingress as shown in the `ingress_demo.yaml` file and the Ingress controller will automatically instruct cert-manager to request the certificate if not present.

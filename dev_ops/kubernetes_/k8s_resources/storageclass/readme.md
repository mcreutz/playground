The default storageclass in MicroK8s for local storage deletes the data when the pvc is deleted. This is not ideal for persistent storage. To create a storageclass that does not delete the data when the pvc is deleted, use the storageclass from the `microk8s_hostpath_retain.yaml` file.

```bash
kubectl apply -f microk8s_hostpath_retain.yaml
```

You can also make the new storageclass the default
```bash
kubectl patch storageclass microk8s-hostpath -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'       
kubectl patch storageclass microk8s-hostpath-retain -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

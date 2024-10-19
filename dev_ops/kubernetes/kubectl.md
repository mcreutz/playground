# kubectl

## Create Objects on a Cluster
### Create an object from a file
```bash
kubectl create -f <filename>
```
* `-k <directory>`  (directory with kustomization.yaml file)
### Run a particular image on the cluster
```bash
kubectl run <name> --image=<image>
```

## Read Objects from a Cluster
### List all objects of type <resource>
```bash
kubectl get <resource>
```

## Modify existing Objects on a Cluster
### Edit existing object in default editor
```bash
kubectl edit <resource> <object-name>
```
### Update existing object from file (creates new if not existing)
```bash
kubectl apply -f <filename>
```
### Replace object from file
```bash
kubectl replace -f <filename>
```
### Patch object with JSON or YAML patch
```bash
kubectl patch <resource> <object-name> --patch-file=<patch-file>
```
You can add entries to lists and maps, if the [object definition](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json) has `"x-kubernetes-patch-strategy": "merge"` defined for that element. If not, you can only replace the whole list or map.
### Modify attribute of existing object
```bash
kubectl set <attribute> <resource> <object-name> <value>
```
### Add a new label to an object
```bash
kubectl label <resource> <object-name> <label-key>=<label-value>
```
### Add a new annotation to an object
```bash
kubectl annotate <resource> <object-name> <annotation-key>=<annotation-value>
```
### Show rollout status of a resource
```bash
kubectl rollout status <resource> <object-name>
```

## Delete Objects on a Cluster
### Delete existing object
```bash
kubectl delete <resource> <object-name>
```

## Inspect Objects on a Cluster
### Show details of a specific resource or group of resources
```bash
kubectl describe <resource> <object-name>
```
### Print the logs from a container in a pod
```bash
kubectl logs <resource> <object-name>
```
### Show events from all resources in current namespace
```bash
kubectl events
```
### Run a new pod for debugging purpose
```bash
kubectl debug <pod>
```
### Attach to a running container
```bash
kubectl attach <podname> -i
```
### Execute a command on a container in a pod
```bash
kubectl exec <podname> -- command
```
### Diff a manifest file against the corresponding object on the cluster
```bash
kubectl diff -f <filename>
```

## Inspect Resources
### List the fields for supported resources
```bash
kubectl explain <resource>
```
### Print the supported API resources on the server
```bash
kubectl api-resources
```

## Cluster Management Commands
### Display addresses of the master and services
```bash
kubectl cluster-info
```
### Show node metrics
```bash
kubectl top node 
```
### Mark node as unschedulable
```bash
kubectl cordon <node>
```
### Mark node as schedulable
```bash
kubectl uncordon <node>
```
### Drain node in preparation for maintenance
```bash
kubectl drain <node>
```
### Update the taints on one or more nodes
```bash
kubectl taint <resource> <object-name> <key>=<value>:<effect>
```

## Auth
### Modify certificate resources
```bash
kubectl certificate
```
### Check if the current user has permissions to do an action
```bash
kubectl auth can-i <verb> <resource>
```

## Scaling
### Scale a resource
```bash
kubectl scale <resource> <object-name> --replicas=<count>
```
### Auto-scale a resource
```bash
kubectl autoscale <resource> <object-name> --min=<count> --max=<count> --cpu-percent=<percent>
```

## Networking
###  Forward one or more local ports to a pod
```bash
kubectl port-forward <resource> <object-name> <port>:<target-port>
```
### Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
```bash
kubectl expose <resource> <object-name> --port=<port> --target-port=<target-port> --type=<service-type>
```
### Run a proxy to the Kubernetes API server
```bash
kubectl proxy
```
### Copy files and directories to and from containers
```bash
kubectl cp <resource> <object-name>:<src-path> <dest-path>
```

## Other
### Wait for a specific condition on one or many resources
```bash
kubectl wait <resource> <object-name> --for=<condition>
```
### Build a kustomization target from a directory or a remote url
```bash
kubectl kustomize <directory>
```
### Modify kubeconfig files
```bash
kubectl config 
```

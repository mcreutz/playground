# kubectl

## Create Objects on a Cluster
#### Create an object from a file
```shell
kubectl create -f <filename>
```
* `-k <directory>`  (directory with kustomization.yaml file)

#### Create an object from a file (updates if existing)
```shell
kubectl apply -f <filename>
```
* `-k <directory>`  (directory with kustomization.yaml file)

#### Run a particular image on the cluster
```shell
kubectl run <name> --image=<image>
```

## Read Objects from a Cluster
#### List all objects of type <resource>
```shell
kubectl get <resource>
```


## Modify existing Objects on a Cluster
#### Edit existing object in default editor
```shell
kubectl edit <resource> <object-name>
```
#### Update existing object from file (creates new if not existing)
```shell
kubectl apply -f <filename>
```
#### Replace object from file
```shell
kubectl replace -f <filename>
```
#### Patch object with JSON or YAML patch
```shell
kubectl patch <resource> <object-name> -p <patch>
```
#### Modify attribute of existing object
```shell
kubectl set <attribute> <resource> <object-name> <value>
```
#### Add a new label to an object
```shell
kubectl label <resource> <object-name> <label-key>=<label-value>
```
#### Add a new annotation to an object
```shell
kubectl annotate <resource> <object-name> <annotation-key>=<annotation-value>
```
#### Show rollout status of a resource
```shell
kubectl rollout status <resource> <object-name>
```

## Delete Objects on a Cluster
#### Delete existing object
```shell
kubectl delete <resource> <object-name>
```

## Inspect Objects on a Cluster
#### Show details of a specific resource or group of resources
```shell
kubectl describe <resource> <object-name>
```
#### Print the logs from a container in a pod
```shell
kubectl logs <resource> <object-name>
```
#### Show events from all resources in current namespace
```shell
kubectl events
```
#### Run a new pod for debugging purpose
```shell
kubectl debug <pod>
```
#### Attach to a running container
```shell
kubectl attach <podname> -i
```
#### Execute a command on a container in a pod
```shell
kubectl exec <podname> -- command
```
#### Diff file against Kubernetes server
```shell
kubectl diff -f <filename>
```
## Inspect Resources
#### List the fields for supported resources
```shell
kubectl explain <resource>
```
#### Print the supported API resources on the server
```shell
kubectl api-resources
```

## Cluster Management Commands
#### Display addresses of the master and services
```shell
kubectl cluster-info
```
#### Show metrics for a given node
```shell
kubectl top node
```
#### Mark node as unschedulable
```shell
kubectl cordon <node>
```
#### Mark node as schedulable
```shell
kubectl uncordon <node>
```
#### Drain node in preparation for maintenance
```shell
kubectl drain <node>
```
#### Update the taints on one or more nodes
```shell
kubectl taint <resource> <object-name> <key>=<value>:<effect>
```

## Auth
#### Modify certificate resources
```shell
kubectl certificate
```
#### Check if the current user has permissions to do an action
```shell
kubectl auth can-i <verb> <resource>
```

## Scaling
#### Scale a resource
```shell
kubectl scale <resource> <object-name> --replicas=<count>
```
#### Auto-scale a resource
```shell
kubectl autoscale <resource> <object-name> --min=<count> --max=<count> --cpu-percent=<percent>
```

## Networking
####  Forward one or more local ports to a pod
```shell
kubectl port-forward <resource> <object-name> <port>:<target-port>
```
#### Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
```shell
kubectl expose <resource> <object-name> --port=<port> --target-port=<target-port> --type=<service-type>
```
#### Run a proxy to the Kubernetes API server
```shell
kubectl proxy
```
#### Copy files and directories to and from containers
```shell
kubectl cp <resource> <object-name>:<src-path> <dest-path>
```

## Other
#### Wait for a specific condition on one or many resources
```shell
kubectl wait <resource> <object-name> --for=<condition>
```
#### Build a kustomization target from a directory or a remote url
```shell
kubectl kustomize <directory>
```
#### Modify kubeconfig files
```shell
kubectl config 
```

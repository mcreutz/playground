# kubectl

## Create Objects on a Cluster
```bash
# Create an object from a file
kubectl create -f <filename>  # * `-k <directory>`  (directory with kustomization.yaml file)

# Run a particular image on the cluster
kubectl run <name> --image=<image>
```

## Read Objects from a Cluster
```bash
# List all objects of type <resource>
kubectl get <resource>
```

## Modify existing Objects on a Cluster
```bash
# Edit existing object in default editor
kubectl edit <resource> <object-name>

# Update existing object from file (creates new if not existing)
kubectl apply -f <filename>

# Replace object from file
kubectl replace -f <filename>

# Patch object with JSON or YAML patch
kubectl patch <resource> <object-name> --patch-file=<patch-file>

# You can add entries to lists and maps, if the [object definition](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json) has `"x-kubernetes-patch-strategy": "merge"` defined for that element. If not, you can only replace the whole list or map.

# Modify attribute of existing object
kubectl set <attribute> <resource> <object-name> <value>

# Add a new label to an object
kubectl label <resource> <object-name> <label-key>=<label-value>

# Add a new annotation to an object
kubectl annotate <resource> <object-name> <annotation-key>=<annotation-value>

# Show rollout status of a resource
kubectl rollout status <resource> <object-name>
```

## Delete Objects on a Cluster
# Delete existing object
```bash
kubectl delete <resource> <object-name>
```

## Inspect Objects on a Cluster
```bash
# Show details of a specific resource or group of resources
kubectl describe <resource> <object-name>

# Print the logs from a container in a pod
kubectl logs <resource> <object-name>

# Show events from all resources in current namespace
kubectl events

# Run a new pod for debugging purpose
kubectl debug <pod>

# Attach to a running container
kubectl attach <podname> -i

# Execute a command on a container in a pod
kubectl exec <podname> -- command

# Diff a manifest file against the corresponding object on the cluster
kubectl diff -f <filename>
```

## Inspect Resources
```bash
# List the fields for supported resources
kubectl explain <resource>

# Print the supported API resources on the server
kubectl api-resources
```

## Cluster Management Commands
```bash
# Display addresses of the master and services
kubectl cluster-info

# Show node metrics
kubectl top node 

# Mark node as unschedulable
kubectl cordon <node>

# Mark node as schedulable
kubectl uncordon <node>

# Drain node in preparation for maintenance
kubectl drain <node>

# Update the taints on one or more nodes
kubectl taint <resource> <object-name> <key>=<value>:<effect>
```

## Auth
```bash
# Modify certificate resources
kubectl certificate

# Check if the current user has permissions to do an action
kubectl auth can-i <verb> <resource>
```

## Scaling
```bash
# Scale a resource
kubectl scale <resource> <object-name> --replicas=<count>

# Auto-scale a resource
kubectl autoscale <resource> <object-name> --min=<count> --max=<count> --cpu-percent=<percent>
```

## Networking
```bash
#  Forward one or more local ports to a pod
kubectl port-forward <resource> <object-name> <port>:<target-port>

# Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
kubectl expose <resource> <object-name> --port=<port> --target-port=<target-port> --type=<service-type>

# Run a proxy to the Kubernetes API server
kubectl proxy

# Copy files and directories to and from containers
kubectl cp <resource> <object-name>:<src-path> <dest-path>
```

## Other
```bash
# Wait for a specific condition on one or many resources
kubectl wait <resource> <object-name> --for=<condition>

# Build a kustomization target from a directory or a remote url
kubectl kustomize <directory>

# Modify kubeconfig files
kubectl config 
```

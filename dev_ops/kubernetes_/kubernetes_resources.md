# Cluster
- The sum of Control Planes, Nodes and Networks, used to run containerized workloads

# Node
- Physical or virtual machine.
- There are master-nodes and worker-nodes. Master-nodes are nowerdays called 'Control-Planes', worker-nodes are usually just referred to as nodes.

## Control Plane (Master Node)
- Set of processes running on a dedicated node, responsible for managing the worker-nodes.
- Was previously called 'master-node'.
- Should be run with redundance in production.

## Worker-Node (Node)
- Running the workloads as Pods
- Usually referred to as just 'Node'

# Pod
- An abstraction layer over a container, abstracts away the Docker technologies, so that it can encapsulate other containers as well.
- Usually one app (in the sense of one process) per Pod. Sometimes also helper- or service-containers within the Pod of a main container.

# Virtual Networks
- One virtual network connects the Control Plane and Nodes (previously master-node and worker-nodes).
- Each Node has an internal virtual network, connecting its Pods. Each Pod gets assigned an individual IP. 

# Services / Components

## Api
- Api-server, responsible for communication to external sources. Eg GUI, CLI.
- Running on the Control Plane

## Controller-manager (c-m)
- Responsible for controlling and managing the pods within the cluster
- Running on the Control Plane

## Scheduler
- Responsible for scheduling, scaling and distributing pods within the cluster, based eg. on ressources and workloads
- Running on the Control Plane

## Etcd
- Key-Value-Strorage, holds the current state of the cluster.
- Is used eg. for recovery of the cluster.
- Running on the Control Plane

## kubelet
- Process running on each worker-node, responsible for communication between nodes (workers and master) and the running processes on its own node. 

## Service (svc)
- Pods are ephemeral, so shutdowns or restarts have to be expected. Also, Pod IPs are not bound to the Pods content, means restarting a Pod results in a new IP
- Service is an abstraction over one or multiple Pods, offering a permanent IP or service name to the front
- Also offers to make services externally accessible via the individual service IP (also see Ingress)
- Also offers redundancy by connecting to multiple Pods of the same kind as replicas
- Also offers load balancing for Pods with multiple replicas

## Ingress (ing)
- Route traffic into the cluster
- Kind of a remote Proxy, hadling transport layer encryption (https) and domain names (?)

## Config-Map (cm)
- Configuration strorage for Pods

## Secret
- Secrets (configuration) storage for Pods
- Stored in etcd
- Further actions need to be taken to ensure encryption

## Volumes (vol)
- Linking local (same Node) or remote storage into a Pod for data persistance
- Kubernetes itself does not offer data persistance, but it offers to link to it by Volumes.

## Deployment (deploy)
- An abstraction layer on top of a Pod, managing the the underlying Pods in terms of configuration and replicas
- In practice, you create Deployments, not Pods
- With deployments, you can only replicate stateless pods (eg. no databases), because parallel accesses to the same database would result in data corruption. See StatefulSet.
- In practice, databases are often hosted outside of Kubernetes

## StatefulSet (sts)
- Deployment for stateful Pods (eg. databases)
- Not easy to work with, so databases are often hosted outside of Kubernetes

## ReplicaSet (rs)
- Abstraction layer on top of a Pod, managing the the underlying Pods in terms of replicas
- In practice, you create ReplicaSets, not Pods


# todo
- kubeadm


point local docker cli to minikube docker daemon:
eval $(minikube -p minikube docker-env)

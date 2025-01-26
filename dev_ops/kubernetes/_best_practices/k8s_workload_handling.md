scaling, pod and cluster, horizontal and vertical
affinity, anti-affinity

### Pod lifecycle
A Pod goes through the following phases in its lifecycle:
- Pending: The Pod has been accepted by the Kubernetes system, but one or more of its containers are not yet running.
- Running: The Pod has been bound to a node, and all of its containers have been created. At least one container is still running, or is in the process of starting or restarting.
- Succeeded: All containers in the Pod have terminated in success, and will not be restarted.
- Failed: All containers in the Pod have terminated, and at least one container has terminated in failure. That is, the container either exited with a non-zero status or was terminated by the system.
- Unknown: For some reason the state of the Pod could not be obtained, typically due to an error in communicating with the host of the Pod.


### pod states
- Pending: The pod has been accepted by the Kubernetes API, but a node has not yet been assigned to run it.
- Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting.
- Succeeded: All containers in the pod have terminated in success, and will not be restarted.
- Failed: All containers in the pod have terminated, and at least one container has terminated in failure. That is, the container either exited with a non-zero status or was terminated by the system.
- Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.


### deployment states
- Progressing: The deployment is progressing as expected.
- Degraded: The deployment is not progressing as expected.
- Available: The deployment is available and running as expected.
pod desruption budgets play a role here.


### pod healthness and readiness
- Liveness probe: Indicates whether the container is running. If the liveness probe fails, the container is restarted. If the liveness probe is not configured, the container is assumed to be running.
- Readiness probe: Indicates whether the container is ready to serve requests. If the readiness probe fails, the container is removed from the service load balancer. If the readiness probe is not configured, the container is assumed to be ready.


### pod disruption budget
The key difference is that Deployments and ReplicaSets manage the desired number of replicas under normal conditions, while a PodDisruptionBudget (PDB) specifically manages application availability during voluntary disruptions caused by cluster-level operations. The PDB adds an extra layer of protection by preventing the eviction of too many pods during planned events.



## disruptions
voluntary disruptions caused by cluster operations, such as:
    Draining a node (e.g., for maintenance or the cluster scaler scaling down the cluster).
    Upgrading the Kubernetes version.
    Rolling updates to the application or cluster components.
if they would violate the budget, PDBs will temp block these disruptions until execution does not violate the budget anymore.


involuntary disruptions (e.g., node failures)
PDBs do not protect against involuntary disruptions, such as node failures. Kubernetes handles these by rescheduling the affected pods to healthy nodes.


The key difference is that Deployments and ReplicaSets manage the desired number of replicas under normal conditions, while a PodDisruptionBudget (PDB) specifically manages application availability during voluntary disruptions caused by cluster-level operations. The PDB adds an extra layer of protection by preventing the eviction of too many pods during planned events.

A PDB ensures a consistent availability guarantee across different controllers.

    Example: For a database running with 2 StatefulSet instances and a web server with 3 Deployment replicas, a PDB can enforce the combined availability of both components.

When to Use a PDB
    Cluster Operations: When frequent maintenance or upgrades are expected, and application downtime must be minimized.
    High Availability: For applications where even a temporary drop in replicas is unacceptable.
    Multiple Controllers: To coordinate availability requirements across controllers.
    Autoscaling: To prevent aggressive evictions during scale-down operations.

### taints and tolerations
Taints allow a node to repel a set of pods. Tolerations allow a pod to tolerate (or ignore) a taint. Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes. One or more taints can be applied to a node. Tolerations are applied to pods, and allow (but do not require) the pods to schedule onto nodes with matching taints.
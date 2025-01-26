# Maintenance

updates: rolling updates, blue-green deployments, canary deployments
rollbacks

## Removing a node from a cluster
- Cordoning: Mark the node as unschedulable
- Draining: Evict all pods from the node
- Deleting: Remove the node from the cluster

If you remove a node without draining it first, k8s will reschedule the failed pods to other nodes after the node-monitor-grace-period has passed (default 5m).

does a liveness probe help here?

Session affinity?
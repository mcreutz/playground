## Example configuration
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
name: app-1-cluster
nodes:
- role: control-plane
- role: worker
  extraMounts:
  - hostPath: /path/to/my/files
    containerPath: /files
- role: worker
  extraMounts:
  - hostPath: /path/to/my/files
    containerPath: /files

## Example command to create a cluster
kind create cluster --name my-cluster
# Ray Workers Helm Chart

This Helm chart deploys Ray worker pods that connect to an **existing Ray cluster running outside of Kubernetes**.

## Use Case
- Ray head node running on your local machine/VM/server
- Kubernetes cluster with available compute resources  
- Want to add K8s pods as worker nodes to the external Ray cluster

## Installation

```bash
# Install the chart
helm install my-ray-workers ./ray-workers-chart \
    --set rayHead.address="YOUR_EXTERNAL_RAY_HEAD_IP:10001" \
    --set replicaCount=3 \
    --namespace ray-system \
    --create-namespace
```

## Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `rayHead.address` | Address of external Ray head node | `HOST_MACHINE_IP:10001` |
| `replicaCount` | Number of worker pods | `3` |
| `image.repository` | Ray Docker image | `rayproject/ray` |
| `image.tag` | Ray version | `2.47.1` |
| `resources.requests.cpu` | CPU request per pod | `1` |
| `resources.requests.memory` | Memory request per pod | `2Gi` |

## Example: Connect to Ray cluster at 192.168.1.100

```bash
helm install ray-workers ./ray-workers-chart \
    --set rayHead.address="192.168.1.100:10001" \
    --set replicaCount=5 \
    --namespace ray-system \
    --create-namespace
```

## Verify Connection

After deployment, check your external Ray cluster:
```bash
ray status  # Run this on your external Ray head node
```

You should see the Kubernetes pods listed as worker nodes! 
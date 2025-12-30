# KubeRay

## Add Helm repo
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update

## Install KubeRay operator incl. CRDs
helm upgrade --install kuberay-operator kuberay/kuberay-operator \
    --version 1.4.2 \
    --namespace kuberay \
    --create-namespace

## Add a RayCluster resource to the cluster
helm upgrade --install raycluster-py312 kuberay/ray-cluster \
    --version 1.3.0 \
    --namespace test-project \
    --create-namespace \
    --set 'image.tag=latest-py312-aarch64'







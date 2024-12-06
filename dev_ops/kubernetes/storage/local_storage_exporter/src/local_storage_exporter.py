from dataclasses import dataclass
import logging
import subprocess

from kubernetes import client, config
from prometheus_client import Gauge


_logger = logging.getLogger(__name__)


@dataclass
class Volume:
    pvc_name: str
    pv_name: str
    storage_path: str


# ------- Prometheus metrics -------
pv_bytes_used = Gauge(
    name="lse_pv_bytes_used",
    documentation="The amount of bytes used by local storage volume",
)


def get_k8s_core_client():
    try:
        # Load in-cluster config
        config.load_incluster_config()
        return client.CoreV1Api()
    except config.ConfigException:
        # Fallback to local kubeconfig for development
        config.load_kube_config()
        return client.CoreV1Api()


def list_pods(namespace="default"):
    k8s_client = get_k8s_core_client()
    pods = k8s_client.list_namespaced_pod(namespace)
    return [pod.metadata.name for pod in pods.items]


def get_volumes():
    k8s_client = get_k8s_core_client()
    pvcs = k8s_client.list_persistent_volume_claim_for_all_namespaces()
    volumes = []
    for pvc in pvcs:
        # if not storageclass = given sc
        #   continue
        pv_name = pvc.spec.volume_name
        volumes.append(Volume(pv_name=pv_name, pvc_name=pvc, storage_path=""))
    for volume in volumes:
        pv = k8s_client.read_persistent_volume(volume.pv_name)
        volume.storage_path = pv.spec.local.path
    return volumes


def get_pv_storage(volume):
    try:
        result = subprocess.run(
            ["du", "-sh", volume.storage_path],
            capture_output=True,
            text=True,
            check=True,
        )
        size = result.stdout.split()[0]
        return size
    except subprocess.CalledProcessError as e:
        _logger.error(f"Failed to get storage usage for volume {volume.pv_name}: {e}")
        return None


def get_partition_data():
    result = subprocess.run(
        ["df", "-h", pvs_path], capture_output=True, text=True, check=True
    )
    return result.stdout

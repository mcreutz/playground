k create ns local-storage-exporter
helm install local-storage-exporter .  -n local-storage-exporter

du -sh /volumes/pvc-27018334-9d5f-4ff1-9dba-c4eb5c4728ad
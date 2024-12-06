k create ns local-storage-exporter
helm install local-storage-exporter ./helmchart  -n local-storage-exporter

du -sh /volumes/pvc-27018334-9d5f-4ff1-9dba-c4eb5c4728ad



todo:
- prometheus metrics
- rbac: sa, cr, crb
- envs for storage class and path
- tests
- dockerfile, noroot, multistage
- repo
- healthcheck
- k8s labels
- readme
- gitignore
- public image
- public helm chart
- metric names
- build script, gh actions
- chart and app versions
- scheduling
- podmonitor
- helm chart init

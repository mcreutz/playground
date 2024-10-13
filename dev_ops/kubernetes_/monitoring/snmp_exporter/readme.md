# SNMP monitoring with Prometheus

## Setup the devices to monitor
Enable SNMP with corresponding version and auth/privacy in the devices and download the ".mib" files for the devices you want to monitor.

Install the snmp utility and test the connection to the devices
```bash
# on MacOS
brew install net-snmp
snmpwalk -v3 -l authPriv \
    -a <auth-protocol> -u <username> -A <auth-password> \
    -x <privacy-protocol> -X <privacy-password> \
    <device-ip> [<oid>]
```

## Prepare the config for the SNMP exporter
### Use the snmp_exporter's included generator to generate the snmp.yml file
Clone the SNMP exporter repository 
```bash
git clone https://github.com/prometheus/snmp_exporter.git
```

Put the downloaded ".mib" files in the `./snmp_exporter/generator/mibs` directory.

Build the generator
```bash
# Install dependencies (example is for MacOS)
brew install go net-snmp unzip
# Build the generator
cd snmp_exporter/generator
make generator mibs
```

Backup the existing `generator.yml` file
```bash
mv generator.yml generator.yml.bak
```

Modify the `generator.yml` file
- Add protocol version 3 on the top if needed
- Remove the existing modules if not needed
- Add the modules for the devices you want to monitor. Google on how to do that for your devices.

Generate the snmp.yml file with the generator
```bash
./generator -m mibs generate
```

Add the content of the generated `snmp.yml` file to the `values.yaml` file under the `config: |` key

## Install the SNMP exporter
### Install the Helm chart
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install snmp-exporter prometheus-community/prometheus-snmp-exporter \
    --namespace monitoring \
    --version 5.5.1 \
    --values dev_ops/kubernetes_/monitoring/snmp_exporter/values.yaml
```

### Install the additional ServiceMonitor for self-monitoring
```bash
kubectl create -f dev_ops/kubernetes_/monitoring/snmp_exporter/servicemonitor-self-monitoring.yaml -n monitoring                 
```

## Helpful links
- https://grafana.com/blog/2022/02/01/an-advanced-guide-to-network-monitoring-with-grafana-and-prometheus/
- https://grafana.com/grafana/dashboards/14572-qnap-monitor/
- https://artifacthub.io/packages/helm/prometheus-community/prometheus-snmp-exporter/5.5.1
- https://github.com/prometheus/snmp_exporter/
- https://www.youtube.com/watch?v=P9p2MmAT3PA&t=597s
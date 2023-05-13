## initialize a chart
$ helm create mychart

use .yaml for YAML files and .tpl for helpers to define the chart

files in templates/ are sent to the template engine

$ helm install <release-name> ./mychart
$ helm install --debug --dry-run goodly-guppy ./mychart

$ helm get manifest <release-name>

$ helm uninstall <release-name>

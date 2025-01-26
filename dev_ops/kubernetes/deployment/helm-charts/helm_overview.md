- Initialize a chart directory: `helm create <chart-name>`

- Install a local chart: `helm install <release-name> ./mychart`
- Install or upgrade a chart: `helm upgrade --install <release-name> ./mychart`
- Install a chart with a specific value: `helm install --set key=value ./mychart`
- Install a chart with a values file: `helm install ./mychart --values myvalues.yaml`
- Dry run installation: `helm install ./mychart --debug --dry-run goodly-guppy`

- Run templating engine for a chart but output instead of deploying: `helm template ./mychart`
- Run templating engine for a single template file: `helm template ./mychart -s templates/mytemplate.yaml`
- Get manifests for an installed release from a cluster: `helm get manifest <release-name>`

- Uninstall a chart: `helm uninstall <release-name>`

- Use .yaml for YAML files and .tpl for helpers to define the chart
- Files in templates/ are sent to the template engine
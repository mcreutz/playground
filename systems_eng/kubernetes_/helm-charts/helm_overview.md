- Initialize a chart directory: `helm create mychart`

- Install a chart: `helm install <release-name> ./mychart`
- Dry run installation: `helm install --debug --dry-run goodly-guppy ./mychart`

- Run templating engine for a chart but output instead of deploying: `helm template ./mychart`
- Get manifests for a release from cluster: `helm get manifest <release-name>`

- Uninstall a chart: `helm uninstall <release-name>`

- Use .yaml for YAML files and .tpl for helpers to define the chart
- Files in templates/ are sent to the template engine
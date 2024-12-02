helm charts need to be pulled explicitly before they can be used in kluctl
kluctl helm-pull

diffing
kluctl --args-from-file values_default.yaml --args-from-file ../values_cluster-one.yaml diff 

deploying
kluctl --args-from-file values_default.yaml --args-from-file ../values_cluster-one.yaml deploy

deleting
kluctl --args-from-file values_default.yaml --args-from-file ../values_cluster-one.yaml delete





todo
- multiple namespaces
- sequencing, waiting
- detailed diffing
- argocd plugin
- templating kustomize patches
- gitops server
- better way to add values than args? probably not
- exclude from diff, no modifications
- ignoring conflicts
- loard default values in deplyment file
- force deploy without diff and confirmation (for scripting)
- how to work with quick fixes made on the cluster
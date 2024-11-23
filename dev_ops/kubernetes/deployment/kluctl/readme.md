helm charts need to be pulled explicitly before they can be used in kluctl
kluctl helm-pull

diffing
kluctl --args-from-file ../values_default.yaml --args-from-file ../values_cluster-one.yaml diff 

deploying
kluctl --args-from-file ../values_default.yaml --args-from-file ../values_cluster-one.yaml deploy

deleting
kluctl --args-from-file ../values_default.yaml --args-from-file ../values_cluster-one.yaml delete
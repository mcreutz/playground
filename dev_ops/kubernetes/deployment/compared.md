## general tasks
- rendering templated helmchart values
- rendering helmcharts
- rendering kustomize patches
- applying kustomize patches
- diffing results for apps or platform with the cluster
- installing or updating results with seqencing and waiting

## setup
### kluctl
- kluctl installed locally
- platform repo
- cluster values file in any repo
- apps as kluctl applications

### carvel
- ytt and kapps installed locally
- platform repo
- cluster values file in any repo
- carvel file for sequencing
- script files for rendering, diffing and deploying

### ansible without argocd
- ansible installed locally
- platform repo
- cluster values file in any repo
- ansible script for sequencing

### ansible mit argocd
- ansible installed locally
- argocd installed on the cluster
- platform repo
- applications as argocd applications
- ansible script for sequencing
- cluster repo reachable for customer (no pforge etc.)
- cluster branch holding the rendered manifests



## workflow installation


## workflow update



# open questions
- do we need to template helm values?
- do we need to template helm values and kustomize patches in one app?
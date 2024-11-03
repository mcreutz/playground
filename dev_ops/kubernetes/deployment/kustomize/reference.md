# Kustomization file syntax
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
```

## There are 4 basic operations in kustomize. All other operations are just conveniece syntaxes / shorthands for built-in operations of one of these 4 basic operations.
```yaml
resources:
- {pathOrUrl}
- ../base
- github.com/kubernetes-sigs/kustomize//examples/multibases/dev/
- ...
bases: # Same as resources, but deprecated
- ...
generators:
- {pathOrUrl}
- ...
transformers:
- {pathOrUrl}
- ...
validators:
- {pathOrUrl}
- ...
```

### The annotation transformer adds the given annotations to all resources.
```yaml
commonAnnotations:
  myAnnotation: myValue
```

### The label transformer that adds the given labels to all resources.
```yaml
commonLabels:
  myLabel: myValue
```

### The config map generator generates a ConfigMap from the given data.
```yaml
configMapGenerator:
- name: my-java-server-props
  behavior: merge
  files:
  - application.properties
  - more.properties
- name: my-java-server-env-vars
  literals: 
  - JAVA_HOME=/opt/java/jdk
  - JAVA_TOOL_OPTIONS=-agentlib:hprof
  options:
    disableNameSuffixHash: true
    labels:
      pet: dog
- name: dashboards
  files:
  - mydashboard.json
  options:
    annotations:
      dashboard: "1"
    labels:
      app.kubernetes.io/name: "app1"
```

### The namespace transformer sets the namespace of all resources to the given namespace.
```yaml
namespace: my-namespace
```

### The patchesJson6902 transformer applies the given JSON patches to the matching resources.
```yaml
patchesJson6902:
# 'target' is a selector that selects the resources to apply the patches to.
# 'path' is the path to the patch file containing the patch in JSON or YAML format.
- target:
    group: apps
    version: v1
    kind: Deployment
    name: my-deployment
    namespace: my-namespace
  path: add_init_container.yaml
- target:
    version: v1
    kind: Service
    name: my-service
  path: add_service_annotation.yaml
# The content of the patch file can also be specified as an inline string using the 'patch' field instead.
- target:
    version: v1
    kind: Deployment
    name: my-deployment
  patch: |-
    - op: add
      path: /some/new/path
      value: value
    - op: replace
      path: /some/existing/path
      value: "new value"
```
- Uses JSON Patch format (RFC 6902)
- Best for precise, targeted changes using specific operations (add/remove/replace)
- Requires explicit target selection
- Good for making multiple small changes
- Format is more verbose but very explicit

### The patchesStrategicMerge transformer applies the given strategic merge patches to the matching resources.
```yaml
patchesStrategicMerge:
- service_port_8888.yaml
- deployment_increase_replicas.yaml
- deployment_increase_memory.yaml
# The content of the patch file can also be specified as an inline string.
- |-
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: nginx
  spec:
    template:
      spec:
        containers:
          - name: nginx
            image: nignx:latest
```
- Uses Kubernetes Strategic Merge Patch
- Merges entire resource definitions
- Automatically matches resources based on name/kind
- Better for larger changes or multiple field updates
- More Kubernetes-aware (understands arrays and merge directives)
- Simpler syntax but less precise control

### The patch transformer applies the given patches to the matching resources. 
```yaml
patches:
- path: patch.yaml      # Path to patch file
  target:
    kind: Deployment
    name: my-deployment
- patch: |-            # Inline patch
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
    spec:
      replicas: 3
```
- Newer, unified way to apply both types of patches
- Can use either JSON Patch or Strategic Merge format
- Combines features of both above methods
- More flexible targeting options
- Recommended for newer Kustomize versions

## Reference:
https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/
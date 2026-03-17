# needed for a proper pipeline framework

- compile, upload and run pipeline without connection
- hand over data from step to step without local machine
- declare envs, eg. python, with external packages and caching
- executing steps in parallel, graph
- collect local python code by serialization
- run from jupyter
- scheduling / execution can be done by ray
- set resources per step
- gui
- logs
- scale over the cluster
- gpu support
- cluster worker with low resources itself, steps in pods with resources free to choose
- 
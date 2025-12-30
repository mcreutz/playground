to run a pipeline on a prefect server/worker, you need to create a prefect deployment 
you could alternatively use a ray cluster for the execution of the tasks.

a prefect deployment 
+ is managed on the cluster, no local connection necessary.
- needs the pipeline code in s3, git or a custom docker image
- cannot be run from jupyter

a prefect pipeline with execution through a ray cluster can be started 
- needs a local connection for orchestration


### Pod termination
Make sure your app shuts down gracefully when receiving a SIGTERM signal. This is the signal that Kubernetes sends to your app when it wants to stop it. If your app doesn't handle this signal, Kubernetes will kill it with a SIGKILL, which doesn't give your app a chance to clean up.
If your app take longer than the default 30s of the terminationGracePeriodSeconds parameter to shut down, increase this value. This is the time that Kubernetes waits for your app to shut down before killing it with a SIGKILL. You can set this value in your Pod spec.


### Pod healthness and readyness checks
Kubernetes can check the health of your app by sending requests to it. If your app doesn't respond with a 200 status code, Kubernetes will restart it. You can configure these health checks in your Pod spec. There are two types of health checks:
- Liveness probe: Indicates whether the container is running. If the liveness probe fails, the container is restarted. If the liveness probe is not configured, the container is assumed to be running.
- Readiness probe: Indicates whether the container is ready to serve requests. If the readiness probe fails, the container is removed from the service load balancer. If the readiness probe is not configured, the container is assumed to be ready.
Simple apps can use the same probe for both liveness and readiness checks or even noe at all. More complex apps may need separate probes.
Also see minReadySeconds and initialDelaySeconds.

### Pod resource requests and limits
You can set resource requests and limits for your Pods. Requests are the amount of resources that your app needs to run. Limits are the maximum amount of resources that your app can use. If your app exceeds its limits, Kubernetes will kill it.

### Pod security context
You can set a security context for your Pods. This allows you to run your app as a specific user, group, or with specific permissions. This can help you secure your app and prevent it from doing things it shouldn't be doing.

### Pod environment variables
You can set environment variables for your Pods. This allows you to pass configuration values to your app at runtime. You can set these environment variables in your Pod spec.

### pod disruption budget
The key difference is that Deployments and ReplicaSets manage the desired number of replicas under normal conditions, while a PodDisruptionBudget (PDB) specifically manages application availability during voluntary disruptions caused by cluster-level operations. The PDB adds an extra layer of protection by preventing the eviction of too many pods during planned events.


## Replication steps

Ran on ubuntu20.
Requirements:
    - Docker
    - Minikube

```bash

cd docker
./build.sh

cd ../kubernetes
./deploy.sh

# The cron job is scheduled to run every minute, so you'll have to wait a bit before logs appear...

tail -f /mnt/logs/resource-logs.txt
```

## Questions

1. Why could it be a problem to have deployments that don’t specify their requirements?

The kubelet uses this information to determine which node to place a pod on, so resource requirements are important for optimal distribution of an application workload. Processing/memory bottlenecks could occur if a container is too hungry. Limits are important values used to prevent a container from exceeding a certain amount of resource usage.

2. Is there a better way to check deployments than periodically calling the API server?

I'd hope so! I'd be keen on validating/running compliance on the yaml file before `kubectl apply` is run. In addition, I'd look to include pre-commit hooks as part of the dev process so that any newly written yaml files get checked on commit.

I also took a look at templating yaml - Kustomize seems to be the preferred method, where you apply patches rather than using templates. One piece of further work I was going to do was use kustomize to patch in a different log level environment var in the cron job.

3. Are there any existing tools we could use instead? Why might we write our own tool?

Yep a few it seems. Some options here: https://learnk8s.io/validating-kubernetes-yaml

We may want to write our own tool so that we can call some centralized monitoring/logging capability and monitor multiple deployments at once. 
There may be a convention for deployments that a team would want to implement, that is not a recognised standard best practice for kubernetes clusters but something more specific to the workloads being deployed.
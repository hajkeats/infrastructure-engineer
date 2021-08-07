# Infrastructure Engineer — Technical Task

Welcome to the technical task for the Infrastructure Engineer!

The task is to write a small application to check for errors in Kubernetes Deployments. There are a lot of possible options to set in a Deployment, and sometimes the devs forget one of them. Your application will periodically check that all of the existing Deployments have [Resource Requirements](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) set.

## Requirements
Your submission will be an application that must satisfy the following criteria:
- it will call the Kubernetes API to check for deployments that don’t have resource requirements set for `cpu` and `memory`.
- for those invalid deployments, it will trigger an alert — this can just be a log. The message should include at least the deployment name and namespace.
- it will perform its check at a regular interval

If you have time, you could include the following:
- deploy your application onto your Kubernetes cluster
- exclude the kube-system namespace from the check
- check that the resource quantities are within a specific range

The task can be done in any programming language.

## Submitting the task

You can see a sample submission file in `SAMPLE_SUBMISSION.md`.

This contains space for replication steps and a few questions to think about. You can, but do not have to submit written answers, we will discuss them in the follow up interview.

We don’t want you to spend more than 3 hours or so on the task. If you have ideas for further improvements that would push you beyond this timeframe, please outline those in your submission. If you are unable to perform this task for some reason get in touch and we will work out an alternative.

Please send submissions to oliver@cervest.earth, including as an attachment any code you write. We look forward to reading your submissions!

## Tips
[Minikube](https://minikube.sigs.k8s.io/docs/start/) is a very easy way to deploy a Kubernetes cluster locally to develop against. You can also use something else if you prefer.

Once you are connected to Kubernetes you can create some deployments with the supplied specs.
```
# with minikube
minikube kubectl -- apply -f deployments/
```

It’s recommended to use a [Kubernetes client library](https://kubernetes.io/docs/reference/using-api/client-libraries/), which will handle authentication for you. If you can connect to your cluster with `kubectl`, the client library can probably authenticate itself automatically.

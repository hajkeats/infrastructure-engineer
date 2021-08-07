#!/usr/bin/env python3

from kubernetes import client, config
import logging
from os import environ

LOGLEVEL = environ.get('LOGLEVEL', 'WARNING').upper()
IGNORED_NAMESPACES = ['kubernetes-dashboard', 'kube-system', 'resource-check']

logging.basicConfig(
    filename='/logs/resource-logs.txt',
    level=LOGLEVEL,
    format='%(asctime)s %(levelname)s: %(message)s'
)


def check_resource_fields():
    """
    Uses the default kubectl api to identify missing resource request and limits fields within deployments
    """
    print('Loading config!')
    print(f'Log Level: {LOGLEVEL}')
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False).items

    print(f'Found pods!')

    for pod in pods:
        namespace = pod.metadata.namespace
        if namespace in IGNORED_NAMESPACES:  # Only care about apps we've deployed
            continue

        pod_name = pod.metadata.name
        containers = pod.spec.containers
        for container in containers:
            container_name = container.name

            request_fields = container.resources.requests
            if request_fields:
                logging.info(f'NAMESPACE: {namespace} POD: {pod_name} CONTAINER: {container_name} '
                             f'REQUESTS: {request_fields}')
            else:
                logging.warning(f'NAMESPACE: {namespace} POD: {pod_name} CONTAINER: {container_name}'
                                ' is missing request resource requirements!')

            limit_fields = container.resources.limits
            if limit_fields:
                logging.info(f'NAMESPACE: {namespace} POD: {pod_name} CONTAINER: {container_name} '
                             f'LIMITS: {request_fields}')
            else:
                logging.warning(f'NAMESPACE: {namespace} POD: {pod_name} CONTAINER: {container_name}'
                                ' is missing limits resource requirements!')


if __name__ == '__main__':
    check_resource_fields()

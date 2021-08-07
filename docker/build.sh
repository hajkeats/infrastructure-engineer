#!/usr/bin/env bash

eval $(minikube docker-env)
docker build -f Dockerfile -t python-resource-checker:latest .
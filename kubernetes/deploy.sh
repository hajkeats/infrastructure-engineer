#!/usr/bin/env bash

minikube start

eval $(minikube docker-env)
minikube kubectl -- apply -f deployments/ --recursive

echo
echo "Waiting a minute for the cronjob to kickoff!"
echo

sleep 60

echo
echo "Entering node. Run 'tail -f /mnt/logs/resource-logs.txt' to see logging!"
echo

minikube ssh
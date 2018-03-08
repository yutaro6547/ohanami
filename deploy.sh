#!/bin/bash

# Exit on any error
set -e

for f in k8s/*.yml
do
	envsubst < $f > "generated-$(basename $f)"
done
gcloud docker -- push asia.gcr.io/${PROJECT_NAME}/tanoshingo:$CIRCLE_SHA1
kubectl apply -f generated-deployment.yml --record

# Restaurant Customer Satisfaction Survey.

## Install and Start Minikube

1. curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
2. sudo install minikube-linux-amd64 /usr/local/bin/minikube
3. minikube start

## Start Database Services

cd kubernetes/mongo
kubectl apply -f statefulset.yaml
kubectl get statefulsets

cd kubernetes/mongo
kubectl apply -f service.yaml
kubectl get svc
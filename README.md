# Restaurant Customer Satisfaction Survey.

## Install Python dependencies

```pip install -r python/requirements.txt```

## Install and Start Minikube

1. ```curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64```
2. ```sudo install minikube-linux-amd64 /usr/local/bin/minikube```
3. ```minikube start```

## Start Database Services

```cd kubernetes/mongo```
```kubectl apply -f statefulset.yaml```
```kubectl get statefulsets```

```kubectl apply -f service.yaml```
```kubectl get svc```

## Start Flask App Services

```cd kubernetes/flask-app```
```kubectl apply -f deployment.yaml```
```kubectl get deployments```

```kubectl apply -f service.yaml```
```kubectl get svc```
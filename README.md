# BOOKSTORE

## Create the Docker Image

```docker build -t flask-app .```

## Install and Start Minikube

1. ```curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64```
2. ```sudo install minikube-linux-amd64 /usr/local/bin/minikube```
3. ```minikube start```

## Start Database Services

```cd kubernetes/mongo```<br/>
```kubectl apply -f statefulset.yaml```<br/>
```kubectl get statefulsets```<br/><br/>

```kubectl apply -f service.yaml```<br/>
```kubectl get svc```<br/>

## Start Flask App Services

```cd kubernetes/flask-app```<br/>
```kubectl apply -f deployment.yaml```<br/>
```kubectl get deployments```<br/><br/>

```kubectl apply -f service.yaml```<br/>
```kubectl get svc```<br/>

## Check for the External-IP for the created flask-app service

```kubectl get svc flask-app```<br/><br/>

- if it is still pending wait for a bit until your cloud provider assigns an external-IP

## Using Postman you can test the newly created Flask API

```http://{EXTERNAL-IP}:5000/books```

# My Inventory System

This application stores information on water bottles sold by different suppliers. The user can add or delete a water bottle in the system and they can view the list of suppliers and the water bottles produced by each supplier. 

## General Steps

### Uploading to Dockerhub

1. docker build -t zenknm/gitgods-inventory .
2. docker tag zenknm/gitgods-inventory:latest zenknm/gitgods-inventory:latest
3. docker zenknm/gitgods-inventory:latest

### Pulling Image from Docker
1. docker pull zenknm/gitgods-inventory:latest

### Deploying to Kubernetes
1. Go to GCP and create a kubernetes cluster
2. Connect to the cluster 
4. Apply the Kubernetes manifests:
     - `kubectl apply -f kubernetes-manifests/inventory-deployment.yaml`
     - `kubectl apply -f kubernetes-manifests/inventory-service.yaml`
     - `kubectl apply -f kubernetes-manifests/inventory-ingress.yaml`


## Deployment Process

These are the major phases the team followed in deploying the inventory system on Kubernetes.


### Building the Image through CloudRun

1. Created a Dockerfile and Compose file to support installation of all application dependencies
2. Created Docker container with Cloud Build
3. Deployed container through Cloud Run

### Deploying Google Kubernetes Engine Cluster

1. Created a standard cluster under Kubernetes Engine
2. Created a Kubernetes deployment yaml file initializing pods (3 replicas) and specifying tainer image
3. Created a Kubernetes service yaml file containing
4. Applied both files to cluster
5. Get services and verify external IP 


### Deploy Ingress Resource

1. Installed ingress
2. Created a global static IP address
3. Created yaml link for ingress and applied it to cluster
4. Get ingress under the name inventory-ingress and verify address linked

## Author
Aliya Galang, Zen Magdamit, and Julienne Bobadilla iscs-30-23-d2-gitgods


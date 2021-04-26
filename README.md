## How to run 

- eval $(minikube docker-env)
- minikube start or minikube start --driver=docker
- docker build . -t test
- kubectl apply -f .
- kubectl get svc
- minikube ip
- hit the URL  "http://<Minikube_IP>:<NODEPORT>/pucsd" in any browser.

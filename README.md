## How to run 

- minikube start or minikube start --driver=docker
- eval $(minikube docker-env)
- docker build . -t test
- kubectl apply -f .
- kubectl get svc
- minikube ip
- hit the URL  "http://< minikube ip >:<NODEPORT>/pucsd" in any browser.

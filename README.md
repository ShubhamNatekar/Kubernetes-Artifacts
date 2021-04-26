## How to run 

- eval $(minikube docker-env)
- docker build . -t test
- kubectl apply -f .
- kubectl get svc
- minikube ip
- hit the URL  "http://<Minikube_IP>:<NODEPORT>/pucsd" in any browser.

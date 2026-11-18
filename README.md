# k8s-cicd-mini-project

A hands-on CI/CD project: a small Python (Flask) web app, packaged with Docker,
deployed on Kubernetes, with an automated pipeline.

## How it works

```
Edit app/app.py -> git push
        |
GitHub Actions (CI)  : build image -> push to Docker Hub -> update image tag in k8s/deployment.yaml
        |
Argo CD (CD, GitOps) : sees the change in Git -> updates the Kubernetes cluster (rolling update)
```

## Project structure

| Path | What it is |
|---|---|
| `app/app.py` | Flask web app (shows the version and the pod name; `/health` for probes) |
| `app/Dockerfile` | Recipe for the Docker image |
| `k8s/deployment.yaml` | Kubernetes Deployment: 3 replicas, readiness and liveness probes |
| `k8s/service.yaml` | Kubernetes Service (port 80 -> app port 5000) |
| `.github/workflows/ci.yml` | CI pipeline (GitHub Actions) |

## Run it locally

```
kubectl apply -f k8s/
kubectl port-forward service/web 8080:80
```
Then open http://localhost:8080

## Tools

Docker Desktop (Kubernetes with kind), kubectl, GitHub Actions, Docker Hub, Argo CD

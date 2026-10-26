
# DevOps with Kubernetes 2026

Sina Zare's exercise submissions for the University of Helsinki
DevOps with Kubernetes course.

## Exercises

| Exercise | Application | Description |
|---|---|---|
| [1.1](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.1/log_output) | [Log output](log_output/) | Generate a random string at startup and output it with a timestamp every five seconds. |
| [1.2](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.2/todo_app) | [Todo app](todo_app/) | Create and deploy a web server with a configurable listening port using the `PORT` environment variable. |
| [1.3](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.3/log_output) | [Log output](log_output/) | Same `log output` app but this time in declarative manner under k8s directory `deployments.yml`.|
| [1.4](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.4/todo_app) | [Todo app](todo_app/) | Same `todo app` but this time in declarative manner with manifest file under k8s directory `deployments.yml`.|
| [1.5](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.5/todo_app) | [Todo app](todo_app/) | Same todo app for project 1.4, now returns a simple HTTP page at `GET /` and accessible through kubectl port-forward.|
| [1.6](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.6/todo_app) | [Todo app](todo_app/) | Same todo app for project 1.5, now configured NodePort Service to access the project|

Each exercise is documented in its application's README. GitHub Releases are used to identify the completed state of each exercise.
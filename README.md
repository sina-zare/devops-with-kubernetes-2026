
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
| [1.7](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.7/log_output) | [Log output](log_output/) | log_output app that now has an http endpoint at `/` and made accessible to browser via ingress and ClusterIP service manifests|
| [1.8](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.8/todo_app) | [Todo app](todo_app/) | Todo app that now has an http endpoint at `/` and made accessible to browser via ingress and ClusterIP service manifests|
| [1.9](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.9/ping_pong) | [Ping pong](ping_pong/) | Create a second FastAPI application with an in-memory request counter that returns an incrementing `pong` response at `GET /pingpong`. Route requests through the existing Log Output Ingress using path-based routing. |
| [1.10](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.10/log_output) | [Log output](log_output/) | log_output app now running with 2 containers, one server and one generator using one `emptyDir` shared volume. |
| [1.11](https://github.com/sina-zare/devops-with-kubernetes-2026/tree/1.11) | Log output / Ping-Pong | Introduce Kubernetes PersistentVolumes and PersistentVolumeClaims to share persistent data between applications. The Ping-Pong request counter is stored in persistent storage and exposed through the Log Output application. |

Each exercise is documented in its application's README. GitHub Releases are used to identify the completed state of each exercise.

## Storage architecture

Starting with Exercise 1.11, the project uses Kubernetes PersistentVolumes (PV) and PersistentVolumeClaims (PVC) to share persistent data between applications.

The storage resources are defined separately from application-specific Kubernetes manifests.

### Shared storage

The `log_output` and `ping_pong` applications use the same PersistentVolumeClaim (`shared-pvc`), which is bound to a PersistentVolume (`shared-pv`).

The underlying storage is a local directory on a Kubernetes node.

```text
                  Kubernetes Cluster
                          |
              +-----------+-----------+
              |                       |
         Log Output              Ping-Pong
              |                       |
              +-----------+-----------+
                          |
                    shared-pvc
                          |
                     shared-pv
                          |
                 Local Node Storage
                    /tmp/kube
```

### Storage resources

| Resource | Purpose |
|---|---|
| PersistentVolume (`shared-pv`) | Defines the available persistent storage. |
| PersistentVolumeClaim (`shared-pvc`) | Requests and binds to the PersistentVolume. |
| `emptyDir` | Provides temporary shared storage between containers inside the Log Output Pod. |

The PersistentVolume and PersistentVolumeClaim are managed independently of the application Deployments.

This implementation demonstrates the difference between Pod-scoped temporary storage and persistent storage that can be reused by multiple application Pods.

**Note:** The current implementation uses local node storage for learning purposes. It demonstrates persistence across Pod recreation, but does not provide node-level storage high availability or automatic replication.
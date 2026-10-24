# Todo App - Exercise 1.2

A simple web server built with Python and FastAPI for exercise 1.2 of the University of Helsinki's DevOps with Kubernetes course.

The application prints `Server started in port NNNN` when it starts. The listening port can be configured using the `PORT` environment variable, which defaults to `8080`.

## Application

- **`app.py`** - Starts the FastAPI web server and exposes a `GET /` endpoint.
- **`requirements.txt`** - Lists the Python dependencies.
- **`Dockerfile`** - Builds the application image.
- **`k8s/deployment.yml`** - Defines the Kubernetes Deployment.

The root endpoint returns:

```json
{
  "message": "Todo app is running!"
}
```

## Build the Docker image

From the repository root:

```bash
docker build -t todo-app:1.0 ./todo_app
```

The Dockerfile installs Python dependencies using the configured internal PyPI repository.

## Deploy to Kubernetes

For making image available to k3d cluster, import the image to the cluster as below. Replace `YOUR_CLUSTER_NAME` with your cluster name:

```bash
k3d image import todo-app:1.0 -c YOUR_CLUSTER_NAME
```

Apply the Deployment:

```bash
kubectl apply -f todo_app/k8s/deployment.yml
```


## Verify the application

Check the application logs:

```bash
kubectl logs deployment/todo-app
```

Expected startup message:

```text
Server started in port 9090
```

The Deployment sets `PORT=9090`, so the application listens on port `9090` inside the container.


## Change the listening port

The application reads the `PORT` environment variable at startup. To change the port, update the `PORT` value and `containerPort` in `k8s/deployment.yml` to the same port, then apply the updated Deployment:

```bash
kubectl apply -f todo_app/k8s/deployment.yml
kubectl rollout status deployment/todo-app
```

No image rebuild is needed to change the port because it is configured through an environment variable.

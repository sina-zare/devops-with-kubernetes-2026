# Ping-Pong Application

A simple web application built with Python and FastAPI for University of Helsinki's `DevOps with Kubernetes course`

The application exposes a `GET /pingpong` endpoint that returns a response containing `pong` and an incrementing counter.

## Application

- `app.py` - Starts the FastAPI web server and implements the application endpoints.
- `requirements.txt` - Lists the Python dependencies.
- `Dockerfile` - Builds the application image.
- `k8s/deployment.yml` - Defines the Kubernetes Deployment.
- `k8s/service.yml` - Defines the Kubernetes ClusterIP Service.

### Endpoints

| Endpoint | Description |
|---|---|
| `GET /pingpong` | Returns `pong` followed by an incrementing counter. |
| `GET /` | Returns a simple HTML page guiding users to explore `/pingpong`. |

Example responses from consecutive requests:

```text
pong 0
pong 1
pong 2
pong 3
```

The counter is stored in application memory. It resets when the application restarts, and each replica maintains its own counter.

## Build the Docker image

From the repository root:

```bash
docker build -t ping_pong:1.0 ./ping_pong
```

## Deploy to Kubernetes

Import the image into your k3d cluster. Replace `YOUR_CLUSTER_NAME` with your cluster name:

```bash
k3d image import ping_pong:1.0 -c YOUR_CLUSTER_NAME
```

Apply the Deployment and Service:

```bash
kubectl apply -f ping_pong/k8s/deployment.yml
kubectl apply -f ping_pong/k8s/service.yml
```

The Deployment runs one replica of the application:

- Container image: `ping_pong:1.0`
- Container port: `8181`
- Image pull policy: `Never`

The Service exposes port `80` internally and forwards traffic to container port `8181`.

## Ingress configuration

The Ping-Pong application shares the existing `log-output-ingress` with the Log Output application present at [Log output Ingress](../log_output/k8s/ingress.yml).

The Ingress routes requests based on their URL paths:

| Path | Backend Service |
|---|---|
| `/` | `log-output-svc:80` |
| `/pingpong` | `ping-pong-svc:80` |

The `/pingpong` path is routed to the Ping-Pong application, while `/` is handled by the Log Output application.

The existing Ingress is updated to include the Ping-Pong routing rule. No separate Ingress resource is required.

Apply the updated shared Ingress manifest:

```bash
kubectl apply -f log_output/k8s/ingress.yml
```

## Access the application

With the k3d host port mapped to `8081`, access the Ping-Pong endpoint through the shared Ingress:

```text
http://localhost:8081/pingpong
```

Send multiple requests to observe the counter increasing.


## Networking overview

The request flow for Ping-Pong is:

```text
Browser
   |
   | http://localhost:8081/pingpong
   |
k3d Load Balancer
   |
   | Port 80
   |
Traefik Ingress Controller
   |
   | /pingpong
   |
log-output-ingress
   |
   | ping-pong-svc:80
   |
Ping-Pong Pod:8181
```

## Exercises

- Course: DevOps with Kubernetes 2026
- Exercise 1.9
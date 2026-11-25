# Ping-Pong Application

A simple web application built with Python and FastAPI for the University of Helsinki's `DevOps with Kubernetes` course.

The application exposes a `GET /pingpong` endpoint that returns a response containing `pong` and an incrementing request counter.

The request counter is persisted to a shared file on a Kubernetes PersistentVolumeClaim, allowing the counter to survive application Pod restarts and be accessed by the Log Output application.

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

The request counter is stored in `/data/pingpong.txt` on a shared PersistentVolumeClaim instead of application memory.

On each `/pingpong` request, the application:

1. Reads the current counter value from the persistent file.
2. Increments the counter.
3. Writes the updated value back to the file.
4. Returns the updated counter in the HTTP response.

The counter is shared with the Log Output application, which reads the same file and includes its value in its HTTP response.

Unlike an in-memory counter, the persisted counter survives Pod recreation and application restarts, provided the underlying persistent storage remains available.

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

## Persistent storage

The Ping-Pong application uses a Kubernetes PersistentVolumeClaim (`shared-pvc`) to store its request counter.

The PVC is mounted inside the container at `/data`, and the application stores its counter in:

```text
/data/pingpong.txt
```

The same PVC is mounted by the Log Output application, allowing both applications to access the shared counter file.

The storage resources are defined separately from the application manifests at the project level:

- **PersistentVolume (`shared-pv`):** Provides the underlying local storage.
- **PersistentVolumeClaim (`shared-pvc`):** Requests and binds to the available PersistentVolume.

The volume is independent of the application Pod lifecycle. However, this implementation uses local node storage, so it does not provide automatic storage failover if the Kubernetes node becomes unavailable.

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
- Exercise 1.11
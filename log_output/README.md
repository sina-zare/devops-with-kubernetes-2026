
# Log output - Exercise 1.1

This application was created for exercise 1.1 of the University of Helsinki
DevOps with Kubernetes 2026 course.

## Description

The application generates a random string when it starts, keeps the string
in memory, and prints it to standard output every five seconds together
with a UTC timestamp.

Example output:

```text
2026-10-24T08:35:52.423Z: ucnl-0c5b-batg
2026-10-24T08:35:57.424Z: ucnl-0c5b-batg
2026-10-24T08:36:02.424Z: ucnl-0c5b-batg
```

The random string remains the same while the application process is running.

## Project files

- `app.py` - application logic
- `Dockerfile` - container image definition
- `k8s/deployment.yml` - Kubernetes deployment configuration

## Build and deploy

Build the container image using the instructions and image name configured
for this project:

```bash
docker build -t log-output:latest .
```

Apply the Kubernetes deployment:

```bash
kubectl apply -f k8s/deployment.yml
```

## Verify

Check the deployment and pods:

```bash
kubectl get deployments
kubectl get pods
```

View the application logs:

```bash
kubectl logs -f deployment/log-output
```

The logs should show a timestamp and the same random string every five seconds.

## Exercise

- Course: DevOps with Kubernetes 2026
- Exercise: 1.1 - Getting started

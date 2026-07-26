# Blue-Green Deployment with Kubernetes

A Kubernetes project demonstrating zero-downtime deployments using the Blue-Green deployment strategy.

## Features

- Blue environment
- Green environment
- Service-based traffic switching
- Zero-downtime deployment
- Easy rollback

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes

## Installation

Deploy Blue:

```bash
kubectl apply -f deployment-blue.yaml
kubectl apply -f service.yaml
```

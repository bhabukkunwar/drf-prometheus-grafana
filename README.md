# Django Monitoring with Prometheus and Grafana

This repository contains a monitoring implementation for Django applications using Prometheus and Grafana, deployed on Kubernetes.

## Prerequisites

Before getting started, make sure you have the following tools installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) or other Kubernetes cluster

## Getting Started

### 1. Start your Kubernetes cluster

If using Minikube:

```bash
# Start Minikube cluster
minikube start
```
### 2. Deploy the Django application

```bash
# Apply the Django application deployment
kubectl apply -f k8s/django-deployment.yaml

# Check if the pods are running
kubectl get pods

# Create Ingress for the Django application
kubectl apply -f k8s/ingress.yaml
```

### 3. Map minikube ip to ingress url
```bash
echo "$(minikube ip) drf-monitor.com" | sudo tee -a /etc/hosts
```

### 4. Test django endpoints in browser

```
http://drf-monitor.com/metrics    -- Prometheus metrics
http://drf-monitor.com/api/hello/ -- GET Request
```

### 5. Deploy Prometheus and Grafana
```bash
kubectl apply -f k8s-monitor/prometheus-deployment.yaml
kubectl apply -f k8s-monitor/grafana-deployment.yaml
```

### 6. Expose Graphana and Prometheus endpoints

```bash
# Port forward Prometheus UI (access at http://localhost:9090)
kubectl port-forward svc/prometheus-service 9090:9090

# Port forward Grafana (access at http://localhost:3000)
kubectl port-forward svc/grafana-service 3000:3000
```

Grafana default credentials:

Username: admin
Password: admin

### 7. Configure Grafana
1. Log in to Grafana at http://localhost:3000
2. Add Prometheus as a data source:
   - Go to Configuration > Data Sources > Add data source
   - Select Prometheus
   - URL: http://prometheus-service:9090
   - Click "Save & Test"
3. Import the Django monitoring dashboard:
   - Go to Create > Import
   - Upload the k8s-monitor/drf-dashboard.json file or enter the dashboard ID
   -  Select the Prometheus data source
   -  Click "Import"

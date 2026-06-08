# NodePort Viewer

NodePort Viewer is a lightweight web application for Kubernetes that provides a real-time overview of all NodePort services deployed across the cluster.

The application queries the Kubernetes API and displays currently allocated NodePort ports in a simple and user-friendly web interface. It helps Kubernetes administrators and DevOps engineers quickly identify used NodePorts, avoid port conflicts, and troubleshoot service exposure issues.

## Features

* Displays all Kubernetes services of type `NodePort`
* Shows namespace, service name, service port, target port, and allocated NodePort
* Automatic page refresh for near real-time updates
* Runs natively inside Kubernetes
* Uses Kubernetes ServiceAccount and RBAC for secure API access
* Easy deployment using Kubernetes manifests or Helm

## Use Cases

* Auditing NodePort allocations across the cluster
* Detecting potential NodePort conflicts
* Supporting Kubernetes operations and troubleshooting
* Providing a simple operational dashboard for cluster administrators

## Architecture

The application consists of:

* Flask web application
* Kubernetes Python Client
* ServiceAccount with RBAC permissions
* Kubernetes Deployment
* ClusterIP Service
* Ingress for external access

## Requirements

* Kubernetes cluster
* RBAC enabled
* Python Kubernetes Client access
* Ingress Controller (optional)

## License

MIT License



```
Used Kubernetes NodePorts
Page refreshes every 15 seconds.

Namespace	Service	Type	Port	TargetPort	NodePort	Protocol
cnpg-database	cnpg-cluster-rw	NodePort	5432	5432	32176	TCP
kafka	kafka-cluster-kraft-brokers-0	NodePort	9094	tcp-external	32593	TCP
kafka	kafka-cluster-kraft-brokers-1	NodePort	9094	tcp-external	32735	TCP
```

# NodePort Viewer 

## Tool for display used nodeports in kubernetes cluster

```
Used Kubernetes NodePorts
Page refreshes every 15 seconds.

Namespace	Service	Type	Port	TargetPort	NodePort	Protocol
cnpg-database	cnpg-cluster-rw	NodePort	5432	5432	32176	TCP
kafka	kafka-cluster-kraft-brokers-0	NodePort	9094	tcp-external	32593	TCP
kafka	kafka-cluster-kraft-brokers-1	NodePort	9094	tcp-external	32735	TCP
```

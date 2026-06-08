from flask import Flask, render_template_string
from kubernetes import client, config

app = Flask(__name__)

try:
    config.load_incluster_config()
except Exception:
    config.load_kube_config()

v1 = client.CoreV1Api()

HTML = """
<!doctype html>
<html>
<head>
  <title>Kubernetes NodePorts</title>
  <meta http-equiv="refresh" content="15">
  <style>
    body { font-family: Arial, sans-serif; margin: 30px; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 8px; }
    th { background: #f2f2f2; }
  </style>
</head>
<body>
  <h1>Used Kubernetes NodePorts</h1>
  <p>Page refreshes every 15 seconds.</p>

  <table>
    <tr>
      <th>Namespace</th>
      <th>Service</th>
      <th>Type</th>
      <th>Port</th>
      <th>TargetPort</th>
      <th>NodePort</th>
      <th>Protocol</th>
    </tr>
    {% for item in services %}
    <tr>
      <td>{{ item.namespace }}</td>
      <td>{{ item.name }}</td>
      <td>{{ item.type }}</td>
      <td>{{ item.port }}</td>
      <td>{{ item.target_port }}</td>
      <td><b>{{ item.node_port }}</b></td>
      <td>{{ item.protocol }}</td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>
"""

@app.route("/")
def index():
    result = []

    services = v1.list_service_for_all_namespaces()

    for svc in services.items:
        if svc.spec.type != "NodePort":
            continue

        for port in svc.spec.ports:
            result.append({
                "namespace": svc.metadata.namespace,
                "name": svc.metadata.name,
                "type": svc.spec.type,
                "port": port.port,
                "target_port": port.target_port,
                "node_port": port.node_port,
                "protocol": port.protocol,
            })

    result.sort(key=lambda x: x["node_port"])

    return render_template_string(HTML, services=result)


@app.route("/health")
def health():
    return {"status": "UP"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

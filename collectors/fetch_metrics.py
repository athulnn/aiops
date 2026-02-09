import requests
import pandas as pd
import time

PROM_URL = "http://prometheus:9090/api/v1/query"

queries = {
    "cpu": "rate(node_cpu_seconds_total[1m])",
    "memory": "node_memory_MemAvailable_bytes",
    "disk": "node_filesystem_avail_bytes"
}

rows = []

for name, query in queries.items():
    response = requests.get(PROM_URL, params={"query": query})
    results = response.json()["data"]["result"]

    for r in results:
        rows.append({
            "metric": name,
            "value": float(r["value"][1]),
            "timestamp": int(time.time())
        })

df = pd.DataFrame(rows)
df.to_csv("data/metrics_raw.csv", mode="a", index=False, header=False)

print("Metrics saved")

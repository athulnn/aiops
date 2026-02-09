import pandas as pd

import os
import sys

path = "data/system_anomalies.csv"

if not os.path.exists(path) or os.stat(path).st_size == 0:
    print("⚠ No anomalies detected yet. Skipping alerts.")
    sys.exit(0)


df = pd.read_csv("data/system_anomalies.csv")

df = df.sort_values("timestamp")

CONSECUTIVE_THRESHOLD = 3
CPU_HIGH = 70
MEMORY_LOW = 1.0  # GB

alerts = []
anomaly_streak = 0

for _, row in df.iterrows():
    if row["anomaly"] == 1:
        anomaly_streak += 1
    else:
        anomaly_streak = 0

    if (
        anomaly_streak >= CONSECUTIVE_THRESHOLD
        and row["cpu_percent"] > CPU_HIGH
        or row["memory_available_gb"] < MEMORY_LOW
    ):
        alerts.append({
            "timestamp": row["timestamp"],
            "cpu": row["cpu_percent"],
            "memory": row["memory_available_gb"],
            "disk": row["disk_available_gb"],
            "reason": "Sustained anomaly detected"
        })

alerts_df = pd.DataFrame(alerts)
alerts_df.to_csv("data/system_alerts.csv", index=False)

print(f"{len(alerts)} alerts generated")

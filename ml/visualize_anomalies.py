import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/system_anomalies.csv")

df["time"] = pd.to_datetime(df["timestamp"], unit="s")

normal = df[df["anomaly"] == 0]
anomalies = df[df["anomaly"] == 1]

# -------- CPU PLOT --------
plt.figure()
plt.plot(normal["time"], normal["cpu_percent"], label="CPU (normal)")
plt.scatter(anomalies["time"], anomalies["cpu_percent"], label="CPU anomaly")
plt.xlabel("Time")
plt.ylabel("CPU (idle %)")
plt.title("CPU Behavior with Anomalies")
plt.legend()
plt.show()

# -------- MEMORY PLOT --------
plt.figure()
plt.plot(normal["time"], normal["memory_available_gb"], label="Memory (normal)")
plt.scatter(anomalies["time"], anomalies["memory_available_gb"], label="Memory anomaly")
plt.xlabel("Time")
plt.ylabel("Memory Available (GB)")
plt.title("Memory Behavior with Anomalies")
plt.legend()
plt.show()

# -------- DISK PLOT --------
plt.figure()
plt.plot(normal["time"], normal["disk_available_gb"], label="Disk (normal)")
plt.scatter(anomalies["time"], anomalies["disk_available_gb"], label="Disk anomaly")
plt.xlabel("Time")
plt.ylabel("Disk Available (GB)")
plt.title("Disk Behavior with Anomalies")
plt.legend()
plt.show()

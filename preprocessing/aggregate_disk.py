import pandas as pd

df = pd.read_csv(
    "data/metrics_raw.csv",
    names=["metric", "value", "timestamp"]
)

#  disk rows
disk_df = df[df["metric"] == "disk"]

grouped = disk_df.groupby("timestamp")["value"]

avg_disk_available = grouped.mean()

disk_available_gb = avg_disk_available / (1024 ** 3)

result = disk_available_gb.reset_index()
result.columns = ["timestamp", "disk_available_gb"]

result.to_csv("data/disk_features.csv", index=False)

print("Disk aggregation complete. Saved to data/disk_features.csv")

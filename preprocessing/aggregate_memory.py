import pandas as pd

df = pd.read_csv(
    "data/metrics_raw.csv",
    names=["metric", "value", "timestamp"]
)

# 2.  memory rows
mem_df = df[df["metric"] == "memory"]

grouped = mem_df.groupby("timestamp")["value"]

avg_mem_available = grouped.mean()

mem_available_gb = avg_mem_available / (1024 ** 3)

result = mem_available_gb.reset_index()
result.columns = ["timestamp", "memory_available_gb"]

result.to_csv("data/memory_features.csv", index=False)

print("Memory aggregation complete. Saved to data/memory_features.csv")

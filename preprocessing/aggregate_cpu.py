import pandas as pd

df = pd.read_csv(
    "data/metrics_raw.csv",
    names=["metric", "value", "timestamp"]
)

#  CPU rows
cpu_df = df[df["metric"] == "cpu"]

grouped = cpu_df.groupby("timestamp")["value"]

avg_cpu_time = grouped.mean()

# Convert idle-time ratio into CPU usage percentage
cpu_usage_percent = (1 - avg_cpu_time) * 100

#  Convert result back to a DataFrame
result = cpu_usage_percent.reset_index()
result.columns = ["timestamp", "cpu_percent"]

result.to_csv("data/cpu_features.csv", index=False)

print("CPU aggregation complete. Saved to data/cpu_features.csv")

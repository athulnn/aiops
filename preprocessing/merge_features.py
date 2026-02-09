import pandas as pd

cpu_df = pd.read_csv("data/cpu_features.csv")
mem_df = pd.read_csv("data/memory_features.csv")
disk_df = pd.read_csv("data/disk_features.csv")

#  Merge CPU and Memory on timestamp
merged_df = pd.merge(cpu_df, mem_df, on="timestamp", how="inner")

# Merge Disk
merged_df = pd.merge(merged_df, disk_df, on="timestamp", how="inner")

merged_df = merged_df.sort_values("timestamp")

merged_df.to_csv("data/system_features.csv", index=False)

print("Feature merge complete. Saved to data/system_features.csv")

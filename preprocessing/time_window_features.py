import pandas as pd

df = pd.read_csv("data/system_features.csv")

df = df.sort_values("timestamp")

df["time"] = pd.to_datetime(df["timestamp"], unit="s")
df = df.set_index("time")

# Rolling window features (5-point window)

df["cpu_mean_5"] = df["cpu_percent"].rolling(window=5).mean()
df["cpu_std_5"] = df["cpu_percent"].rolling(window=5).std()

df["memory_mean_5"] = df["memory_available_gb"].rolling(window=5).mean()
df["memory_trend_5"] = df["memory_available_gb"].diff(periods=5)

df["disk_mean_5"] = df["disk_available_gb"].rolling(window=5).mean()

df = df.dropna()

df = df.reset_index(drop=True)

df.to_csv("data/system_features_windowed.csv", index=False)

print("Time-window features created: data/system_features_windowed.csv")

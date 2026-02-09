import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


import sys

df = pd.read_csv("data/system_features_windowed.csv")

if df.empty:
    print("⚠ No data available for anomaly detection yet. Skipping.")
    sys.exit(0)


df = pd.read_csv("data/system_features_windowed.csv")

#  Select BOTH raw + window features
feature_columns = [
    # raw (instant)
    "cpu_percent",
    "memory_available_gb",
    "disk_available_gb",

    # windowed (behavior)
    "cpu_mean_5",
    "cpu_std_5",
    "memory_mean_5",
    "memory_trend_5",
    "disk_mean_5"
]

features = df[feature_columns]

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Train Isolation Forest
model = IsolationForest(
    n_estimators=150,
    contamination=0.05,
    random_state=42
)

model.fit(scaled_features)

df["anomaly"] = model.predict(scaled_features)
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

df.to_csv("data/system_anomalies.csv", index=False)

print("Integrated anomaly detection complete (raw + window features).")

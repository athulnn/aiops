import pandas as pd
import matplotlib
matplotlib.use("Agg")  # IMPORTANT: headless backend
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "system_anomalies.csv"
OUTPUT_PATH = BASE_DIR / "dashboards" / "dashboard.png"

def generate_dashboard():
    # 1. File existence check
    if not DATA_PATH.exists():
        print("Dashboard: system_anomalies.csv not found")
        return False

    df = pd.read_csv(DATA_PATH)

    # 2. Empty data check
    if df.empty:
        print("Dashboard: CSV is empty")
        return False

    # 3. Column sanity check
    required_cols = {
        "timestamp",
        "cpu_percent",
        "memory_available_gb",
        "disk_available_gb",
        "anomaly"
    }

    if not required_cols.issubset(df.columns):
        print("Dashboard: Missing columns", df.columns)
        return False

    # 4. Plot
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    # CPU
    axs[0].plot(df["timestamp"], df["cpu_percent"], label="CPU %")
    axs[0].scatter(
        df[df["anomaly"] == 1]["timestamp"],
        df[df["anomaly"] == 1]["cpu_percent"],
        color="red",
        label="Anomaly"
    )
    axs[0].set_ylabel("CPU %")
    axs[0].legend()

    # Memory
    axs[1].plot(df["timestamp"], df["memory_available_gb"], color="green")
    axs[1].scatter(
        df[df["anomaly"] == 1]["timestamp"],
        df[df["anomaly"] == 1]["memory_available_gb"],
        color="red"
    )
    axs[1].set_ylabel("Memory (GB)")

    # Disk
    axs[2].plot(df["timestamp"], df["disk_available_gb"], color="orange")
    axs[2].scatter(
        df[df["anomaly"] == 1]["timestamp"],
        df[df["anomaly"] == 1]["disk_available_gb"],
        color="red"
    )
    axs[2].set_ylabel("Disk (GB)")
    axs[2].set_xlabel("Timestamp")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    return True

import time
import subprocess
import sys
import os

PYTHON = sys.executable
DATA_DIR = "data"
DASHBOARD_DIR = "dashboards"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DASHBOARD_DIR, exist_ok=True)


PIPELINE_SCRIPTS = [
    "collectors/fetch_metrics.py",
    "preprocessing/aggregate_cpu.py",
    "preprocessing/aggregate_memory.py",
    "preprocessing/aggregate_disk.py",
    "preprocessing/merge_features.py",
    "preprocessing/time_window_features.py",
    "ml/anomaly_detection.py",
    "alerts/alert_engine.py",
]

INTERVAL_SECONDS = 60


def run_pipeline_once():
    print("\n⏱ Running monitoring pipeline...")
    print("🧠 Using Python:", PYTHON)

    for script in PIPELINE_SCRIPTS:
        print(f"▶ Running {script}")
        result = subprocess.run(
            [PYTHON, script],
            cwd=os.getcwd()
        )

        if result.returncode != 0:
            print(f"⚠ Failed: {script}")
        else:
            print(f"✅ Completed: {script}")


def start_monitoring():
    print("🚀 AI System Monitoring started...")
    while True:
        run_pipeline_once()
        print(f"😴 Sleeping {INTERVAL_SECONDS}s...")
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    start_monitoring()

import time
import subprocess
import sys
import os

PYTHON = sys.executable

print("🚀 AI System Monitoring started...")
print("🧠 Using Python:", PYTHON)

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

while True:
    print("\n⏱ Running monitoring pipeline...")

    for script in PIPELINE_SCRIPTS:
        print(f"▶ Running {script}")
        result = subprocess.run(
            [PYTHON, script],
            cwd=os.getcwd()
        )

        if result.returncode != 0:
            print(f"⚠ Failed: {script}")

    print(f"✅ Pipeline completed. Sleeping {INTERVAL_SECONDS}s...")
    time.sleep(INTERVAL_SECONDS)

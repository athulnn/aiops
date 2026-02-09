# AI System Monitoring & Anomaly Detection

An AI-powered system monitoring platform that collects system metrics, engineers time-window features, detects anomalies using machine learning, and visualizes system behavior through interactive dashboards.

---

## 🚀 Features

- System metrics collection (CPU, Memory, Disk)
- Time-window feature engineering
- Unsupervised anomaly detection (Isolation Forest)
- Continuous monitoring pipeline
- REST API (FastAPI)
- Interactive dashboards (Plotly)
- Alert generation for anomalous behavior

---

## 🏗 Architecture Overview

System Metrics
↓
Collectors
↓
Preprocessing & Feature Engineering
↓
ML Anomaly Detection
↓
Alerts + API
↓
Interactive Dashboard



---

## 📂 Project Structure

api/ → FastAPI endpoints
collectors/ → Metrics collection
preprocessing/ → Aggregation & time-window features
ml/ → Anomaly detection model
alerts/ → Alert logic
dashboards/ → Static & interactive dashboards
runner/ → Orchestrates full pipeline
data/ → Runtime-generated data (ignored in Git)



---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/athulnn/aiops.git


python -m venv venv
venv\Scripts\activate   # Windows


pip install -r requirements.txt


python runner/monitor.py


python -m uvicorn api.main:app --reload



🧠 Machine Learning

Algorithm: Isolation Forest

Type: Unsupervised anomaly detection

Inputs: Aggregated CPU, Memory, Disk + rolling window features

Output: Binary anomaly label

🔮 Future Enhancements

Alert severity levels

Auto-refresh dashboards

Cloud deployment (Docker / Azure)

Log-based anomaly detection

Model retraining pipeline

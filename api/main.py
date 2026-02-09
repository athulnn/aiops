from fastapi import FastAPI, HTTPException
import pandas as pd
import os
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from dashboards.dashboard import generate_dashboard
from pathlib import Path as FilePath
import threading
from runner.monitor import start_monitoring
from dashboards.interactive_dashboard import build_interactive_dashboard

app = FastAPI(title="AI System Monitoring API")


@app.on_event("startup")
def start_background_monitor():
    thread = threading.Thread(target=start_monitoring, daemon=True)
    thread.start()


@app.get("/")
def root():
    return {"status": "AI monitoring service running"}


@app.get("/anomalies")
def get_anomalies(limit: int = 10):
    path = "data/system_anomalies.csv"

    if not os.path.exists(path) or os.stat(path).st_size == 0:
        return []

    df = pd.read_csv(path)
    return df.tail(limit).to_dict(orient="records")


@app.get("/alerts")
def get_alerts():
    path = "data/system_alerts.csv"

    if not os.path.exists(path) or os.stat(path).st_size == 0:
        return []

    try:
        df = pd.read_csv(path)

        if df.empty:
            return []

        return df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    return {"health": "ok"}


@app.get("/dashboard")
def dashboard():
    success = generate_dashboard()

    if not success:
        return JSONResponse(
            status_code=200,
            content={"message": "Dashboard not ready yet (no data or no anomalies)"}
        )

    path = FilePath("dashboards/dashboard.png")
    return FileResponse(path)


@app.get("/dashboard/interactive", response_class=HTMLResponse)
def interactive_dashboard():
    html = build_interactive_dashboard()
    if html is None:
        return "<h3>No data yet. Monitoring still warming up.</h3>"
    return html

from fastapi import FastAPI, HTTPException
import pandas as pd
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from dashboards.dashboard import generate_dashboard
from pathlib import Path as FilePath

from dashboards.interactive_dashboard import build_interactive_dashboard



app = FastAPI(title="AI System Monitoring API")

@app.get("/")
def root():
    return {"status": "AI monitoring service running"}

@app.get("/anomalies")
def get_anomalies(limit: int = 10):
    df = pd.read_csv("data/system_anomalies.csv")
    return df.tail(limit).to_dict(orient="records")

@app.get("/alerts")
def get_alerts():
    path = "data/system_alerts.csv"

    if not os.path.exists(path):
        return []

    if os.stat(path).st_size == 0:
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
    
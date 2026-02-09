import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "system_anomalies.csv"


def build_interactive_dashboard():
    # Safety checks
    if not DATA_PATH.exists():
        return None

    df = pd.read_csv(DATA_PATH)
    if df.empty:
        return None

    fig = go.Figure()

    # ---------------- CPU ----------------
    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["cpu_percent"],
            mode="lines",
            name="CPU %",
            line=dict(color="blue"),
        )
    )

    # ---------------- Memory ----------------
    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["memory_available_gb"],
            mode="lines",
            name="Memory (GB)",
            yaxis="y2",
            line=dict(color="green"),
        )
    )

    # ---------------- Disk ----------------
    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["disk_available_gb"],
            mode="lines",
            name="Disk (GB)",
            yaxis="y2",
            line=dict(color="orange"),
        )
    )

    # ---------------- Anomalies ----------------
    anomalies = df[df["anomaly"] == 1]

    if not anomalies.empty:
        fig.add_trace(
            go.Scatter(
                x=anomalies["timestamp"],
                y=anomalies["cpu_percent"],
                mode="markers",
                name="Anomaly",
                marker=dict(color="red", size=10, symbol="x"),
            )
        )

    # ---------------- Layout ----------------
    fig.update_layout(
        title="AI System Monitoring – Interactive Dashboard",
        xaxis=dict(title="Timestamp"),
        yaxis=dict(
            title="CPU %",
            showgrid=True,
        ),
        yaxis2=dict(
            title="Memory / Disk (GB)",
            overlaying="y",
            side="right",
            showgrid=False,
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        template="plotly_white",
        height=650,
        margin=dict(l=60, r=60, t=80, b=60),
    )

    return fig.to_html(full_html=True)

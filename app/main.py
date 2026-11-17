
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Cynbit Backend Audit Prototype",
    description="A demonstration backend implementing secure API design principles.",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Cynbit Backend Audit API",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/api/v1/about")
async def about():
    return {
        "project": "Cynbit Backend Technical Audit",
        "framework": "FastAPI",
        "purpose": "Demonstrating backend engineering improvements"
    }

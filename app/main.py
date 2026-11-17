
from fastapi import FastAPI
from datetime import datetime, timezone

from app.routers.users import router as users_router

app = FastAPI(
    title="Cynbit Backend Audit Prototype",
    description="Backend engineering improvement demonstration",
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


app.include_router(users_router)

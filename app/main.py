
from datetime import datetime, timezone

from fastapi import FastAPI
from dotenv import load_dotenv
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

load_dotenv()

from app.routers.users import router as users_router
from app.routers.auth import router as auth_router
from app.middleware import SecurityHeadersMiddleware
from app.rate_limit import limiter

app = FastAPI(
    title="Cynbit Backend Security Audit",
    description="Backend security assessment prototype",
    version="1.0.0"
)

app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_middleware(SecurityHeadersMiddleware)


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
app.include_router(auth_router)

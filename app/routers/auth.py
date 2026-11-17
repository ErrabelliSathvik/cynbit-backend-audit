
from fastapi import APIRouter, HTTPException, Request, status
from slowapi import Limiter

from app.rate_limit import limiter
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services.user_store import users
from app.services.security import (
    hash_password,
    verify_password,
    create_access_token
)
from app.services.authentication import get_current_user
from fastapi import Depends

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def register(
    payload: RegisterRequest,
    request: Request
):
    email = str(payload.email).lower()

    if email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    users[email] = {
        "name": payload.name,
        "email": email,
        "password_hash": hash_password(payload.password)
    }

    return {
        "message": "Account created successfully"
    }


@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
async def login(
    payload: LoginRequest,
    request: Request
):
    email = str(payload.email).lower()
    user = users.get(email)

    if not user or not verify_password(
        payload.password,
        user["password_hash"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    token = create_access_token(email)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me")
async def get_profile(
    current_user: dict = Depends(get_current_user)
):
    return {
        "message": "Authenticated successfully",
        "user": current_user
    }

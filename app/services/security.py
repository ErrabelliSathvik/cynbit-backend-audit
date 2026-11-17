
import os
import jwt

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from pwdlib import PasswordHash

load_dotenv()

password_hash = PasswordHash.recommended()

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


def get_secret_key():
    secret_key = os.getenv("JWT_SECRET_KEY")

    if not secret_key or len(secret_key) < 32:
        raise RuntimeError(
            "JWT_SECRET_KEY is missing or too short. "
            "Configure a strong secret in your .env file."
        )

    return secret_key


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(email: str) -> str:
    expires = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": email,
        "exp": expires
    }

    return jwt.encode(
        payload,
        get_secret_key(),
        algorithm=ALGORITHM
    )


def verify_access_token(token: str) -> str:
    payload = jwt.decode(
        token,
        get_secret_key(),
        algorithms=[ALGORITHM]
    )

    subject = payload.get("sub")

    if not subject:
        raise jwt.InvalidTokenError("Missing token subject")

    return subject

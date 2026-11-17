
from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)

users = []


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    email = str(user.email).lower()

    for existing_user in users:
        if existing_user["email"] == email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

    new_user = user.model_dump()
    new_user["email"] = email
    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": {
            "name": new_user["name"],
            "email": new_user["email"]
        }
    }

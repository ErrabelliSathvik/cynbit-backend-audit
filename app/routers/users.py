
from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)

# Temporary in-memory storage for demonstration
users = []


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):

    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

    new_user = user.model_dump()

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }


@router.get("/")
async def get_users():
    return {
        "total": len(users),
        "users": users
    }

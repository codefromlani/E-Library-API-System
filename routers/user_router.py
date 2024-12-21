from fastapi import APIRouter, status
from services import user_service
import schemas


router = APIRouter(
    tags=["User"]
)

@router.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate):
    return user_service.create_user(user=user)

@router.get("/users/")
def get_users(skip: int = 0, limit: int = 5):
    return user_service.get_users(skip=skip, limit=limit)

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return user_service.get_user_by_id(user_id=user_id)

@router.patch("/users/{user_id}")
def update_user(user_id: int, user_data: schemas.UserUpdate):
    return user_service.update_user(user_id=user_id, user_data=user_data)

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_service.delete_user(user_id=user_id)

@router.post("/users/deactivate/{user_id}")
def deactivate_user(user_id: int):
    return user_service.deactivate_user(user_id=user_id)
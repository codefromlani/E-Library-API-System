from fastapi import HTTPException, status
from typing import List
import schemas
import data


def create_user(user: schemas.UserCreate):
    for existing_user in data.users_db.values():
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists"
            )
        
    new_user = {
        "id": len(data.users_db) + 1,
        "name": user.name,
        "email": user.email,
        "is_active": True
    }

    data.users_db[new_user["id"]] = new_user
    return schemas.UserResponse(**new_user)

def get_users(skip: int = 0, limit: int = 5) -> List[schemas.UserResponse]:
    users = list(data.users_db.values())
    return [schemas.UserResponse(**user) for user in users[skip:skip+limit]]

def get_user_by_id(user_id: int):
    user = data.users_db.get(user_id)
    if user:
        return schemas.UserResponse(**user)
    else:
       raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND,
           detail="User not found"
       )
    
def update_user(user_id: int, user_data: schemas.UserUpdate):
    existing_user = data.users_db.get(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if user_data.name is not None:
        existing_user["name"] = user_data.name
    if user_data.email is not None:
        existing_user["email"] = user_data.email

    return schemas.UserResponse(**existing_user)

def delete_user(user_id: int):
    existing_user = data.users_db.get(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    data.users_db.pop(user_id)
    return {"detail": "User successfully deleted"}

def deactivate_user(user_id: int):
    existing_user = data.users_db.get(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    existing_user["is_active"] = False
    return schemas.UserResponse(**existing_user)
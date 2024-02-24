from fastapi import HTTPException, Depends
from database.services import get_user, get_users, create_user, delete_user, get_db, update_user
from database.models import User
from sqlalchemy.orm import Session
from ..schemas import UserBase
from fastapi.routing import APIRouter


users_router = APIRouter()


class UsersRouter:
    # Create User Endpoint
    @users_router.post("/users")
    def create_user_endpoint(user_data: dict, db: Session = Depends(get_db)):
        user = create_user(db, user_data)
        return {"user": user}

    # Get User Endpoint
    @users_router.get("/users/{user_id}")
    def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
        user = get_user(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user": user}

    # Get Users Endpoint
    @users_router.get("/users")
    def get_users_endpoint(db: Session = Depends(get_db)):
        users = get_users(db)
        return {"users": users}

    # Update User Endpoint
    @users_router.put("/users/{user_id}")
    def update_user_endpoint(user_id: int, user_data: dict, db: Session = Depends(get_db)):
        user = update_user(db, user_id, user_data)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user": user}

    # Delete User Endpoint
    @users_router.delete("/users/{user_id}")
    def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
        user = delete_user(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user": user}


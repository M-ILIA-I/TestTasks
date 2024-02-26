from fastapi import HTTPException, Depends, Response
from database.services import get_user, get_users, create_user, delete_user, get_db, update_user
from sqlalchemy.orm import Session
from ..schemas import UserBase, UserUpdate
from fastapi.routing import APIRouter
from passlib.context import CryptContext
from authentication.auth_bearer import create_access_token
from datetime import timedelta


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_router = APIRouter()


class UsersRouter:
    # Create User Endpoint
    @users_router.post("/users")
    async def create_user_endpoint(user_data: UserBase, db: Session = Depends(get_db)):
        return await create_user(db, user_data)

    # Get User Endpoint
    @users_router.get("/users/{user_id}")
    async def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
        user = await get_user(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    # Get Users Endpoint
    @users_router.get("/users")
    async def get_users_endpoint(db: Session = Depends(get_db)):
        return await get_users(db)

    # Update User Endpoint
    @users_router.put("/users/{user_id}")
    async def update_user_endpoint(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
        user = await update_user(db, user_id, user_data)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    # Delete User Endpoint
    @users_router.delete("/users/{user_id}")
    async def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
        user = await delete_user(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    # Register User Endpoint
    @users_router.post("/register")
    async def register(responce: Response, user: UserBase, db: Session = Depends(get_db)):
        hashed_password = pwd_context.hash(user.password)
        user.password = hashed_password
        await create_user(db, user.dict())
        access_token = create_access_token(data=user.dict(), expires_delta = timedelta(minutes=30))
        responce.set_cookie(key="jwt", value=access_token)
        return user

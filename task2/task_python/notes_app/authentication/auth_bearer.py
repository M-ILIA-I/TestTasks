from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from database.services import get_user
from typing import Optional
from dotenv import load_dotenv
import os
from api.schemas import UserBase


load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_user(db: AsyncSession, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.getenv("SECRETE_KEY"), algorithms="HS256")
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        if get_user(db, user_id):
            raise HTTPException(status_code=401, detail="User not found")
        return get_user(db, user_id)
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.exceptions.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")


def create_access_token(data: UserBase, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRETE_KEY"), algorithm="HS256")
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, os.getenv("SECRETE_KEY"), algorithm="HS256")
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None


class NoteBase(BaseModel):
    title : str
    content : str
    user_id : int
    created_at : datetime
    updated_at : datetime


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    title : str | None = None
    content : str | None = None
    user_id : int | None = None
    created_at : datetime | None = None
    updated_at : datetime | None = None
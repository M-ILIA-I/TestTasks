from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserCreate(UserBase):
    name: str
    email: str
    password: str


class UserUpdate(UserBase):
    pass


class NoteBase(BaseModel):
    title : str
    content : str
    user_id : int
    created_at : datetime
    updated_at : datetime



class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    pass
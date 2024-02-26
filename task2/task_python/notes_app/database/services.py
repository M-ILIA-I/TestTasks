from datetime import datetime
from .models import User, Note
from .db import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import asc
from api.schemas import UserUpdate, UserBase, NoteBase, NoteUpdate


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


async def create_user(db: AsyncSession, user_data: UserBase):
    user = User(**user_data)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(db: AsyncSession, user_id: int):
    return await db.query(User).filter(User.id == user_id).first()


async def get_users(db: AsyncSession):
    return await db.query(User).all()


async def update_user(db: AsyncSession, user_id: int, user_data: UserUpdate):
    user = await get_user(db, user_id)
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
        return user


async def delete_user(db: AsyncSession, user_id: int):
    user = await get_user(db, user_id)
    if user:
        db.delete(user)
        await db.commit()
        return user


async def create_note(db: AsyncSession, note_data: NoteBase):
    note = Note(**note_data)
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note


async def get_note(db: AsyncSession, note_id: int):
    return await db.query(Note).filter(Note.id == note_id).first()


async def get_notes(db: AsyncSession):
    return await db.query(Note).all()


async def get_user_notes(db: AsyncSession, user_id: int):
    return await db.query(Note).filter(Note.user_id == user_id).all()


async def update_note(db: AsyncSession, note_id: int, note_data: NoteBase):
    note = await get_note(db, note_id)
    if note:
        for key, value in note_data.items():
            setattr(note, key, value)
        note.updated_at = datetime.utcnow()
        await db.commit()
        await db.refresh(note)
        return note


async def delete_note(db: AsyncSession, note_id: int):
    note = await get_note(db, note_id)
    if note:
        db.delete(note)
        await db.commit()
        return note
    

async def get_notes_sorted_by_title(db: AsyncSession):
    return await db.query(Note).order_by(asc(Note.title)).all()


async def get_notes_sorted_by_created_at(db: AsyncSession):
    return await db.query(Note).order_by(asc(Note.created_at)).all()
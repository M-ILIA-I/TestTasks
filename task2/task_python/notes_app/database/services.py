from datetime import datetime
from .models import User, Note
from .db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_user(user_data):
    with get_db() as db:
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


def get_user(user_id):
    with get_db() as db:
        return db.query(User).filter(User.id == user_id).first()


def get_users():
    with get_db() as db:
        return db.query(User).all()


def update_user(user_id, user_data):
    with get_db() as db:
        user = get_user(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            user.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(user)
            return user


def delete_user(user_id):
    with get_db() as db:
        user = get_user(user_id)
        if user:
            db.delete(user)
            db.commit()
            return user


def create_note(note_data):
    with get_db() as db:
        note = Note(**note_data)
        db.add(note)
        db.commit()
        db.refresh(note)
        return note


def get_note(note_id):
    with get_db() as db:
        return db.query(Note).filter(Note.id == note_id).first()


def get_notes():
    with get_db() as db:
        return db.query(Note).all()


def update_note(note_id, note_data):
    with get_db() as db:
        note = get_note(note_id)
        if note:
            for key, value in note_data.items():
                setattr(note, key, value)
            note.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(note)
            return note


def delete_note(note_id):
    with get_db() as db:
        note = get_note(note_id)
        if note:
            db.delete(note)
            db.commit()
            return note
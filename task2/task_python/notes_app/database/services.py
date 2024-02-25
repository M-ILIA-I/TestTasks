from datetime import datetime
from .models import User, Note
from .db import SessionLocal
from sqlalchemy import asc


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_user(db, user_data):
    print(user_data)
    user = User(**user_data)
    print(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db):
    return db.query(User).all()


def update_user(db, user_id, user_data):
    user = get_user(db, user_id)
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user


def delete_user(db, user_id):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return user


def create_note(db, note_data):
    note = Note(**note_data)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_note(db, note_id):
    return db.query(Note).filter(Note.id == note_id).first()


def get_notes(db):
    return db.query(Note).all()


def get_user_notes(db, user_id: int):
    return db.query(Note).filter(Note.user_id == user_id).all()


def update_note(db, note_id, note_data):
    note = get_note(db, note_id)
    if note:
        for key, value in note_data.items():
            setattr(note, key, value)
        note.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(note)
        return note


def delete_note(db, note_id):
    note = get_note(db, note_id)
    if note:
        db.delete(note)
        db.commit()
        return note
    

def get_notes_sorted_by_title(db):
    return db.query(Note).order_by(asc(Note.title)).all()


def get_notes_sorted_by_created_at(db):
    return db.query(Note).order_by(asc(Note.created_at)).all()
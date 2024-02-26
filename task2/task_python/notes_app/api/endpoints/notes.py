from fastapi import HTTPException, Depends
from database.services import get_note, get_notes, create_note, delete_note, get_db, update_note, get_user_notes
from database.models import User, Note
from sqlalchemy.orm import Session
from ..schemas import NoteBase, NoteUpdate
from fastapi.routing import APIRouter
from authentication.auth_bearer import get_current_user


notes_router = APIRouter()


class NotesRouter:
    # Create Note Endpoint
    @notes_router.post("/notes")
    async def create_note_endpoint(note_data: NoteBase, db: Session = Depends(get_db)):
        return await create_note(db, note_data)

    # Get Note Endpoint
    @notes_router.get("/notes/{note_id}")
    async def get_note_endpoint(note_id: int, user_id :int, db: Session = Depends(get_db)):
        note = await get_note(db, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        if note.user_id != user_id:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

    # Get Notes Endpoint
    @notes_router.get("/notes")
    async def get_notes_endpoint(db: Session = Depends(get_db)):
        notes = await get_notes(db)
        return notes

    # Get User Notes Endpoint
    @notes_router.get("/notes")
    async def get_notes_endpoint(user_id: int, db: Session = Depends(get_db)):
        return await get_user_notes(db, user_id)

    # Update Note Endpoint
    @notes_router.put("/notes/{note_id}")
    async def update_note_endpoint(note_id: int, note_data: NoteUpdate, user_id: int, db: Session = Depends(get_db)):
        note = await get_note(db, note_id)
        if note and note.user_id != user_id:
            raise HTTPException(status_code=404, detail="Permission denyed")
        note = await update_note(db, note_id, note_data)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

    # Delete Note Endpoint
    @notes_router.delete("/notes/{note_id}")
    async def delete_note_endpoint(note_id: int, user_id: int, db: Session = Depends(get_db)):
        note = await get_note(db, note_id)
        if note and note.user_id != user_id:
            raise HTTPException(status_code=404, detail="Permission denyed")
        note = await delete_note(db, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note
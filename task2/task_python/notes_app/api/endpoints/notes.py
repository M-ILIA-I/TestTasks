from fastapi import HTTPException, Depends
from database.services import get_note, get_notes, create_note, delete_note, get_db, update_note
from database.models import User, Note
from sqlalchemy.orm import Session
from ..schemas import NoteBase
from fastapi.routing import APIRouter


notes_router = APIRouter()


class NotesRouter:

    # Create Note Endpoint
    @notes_router.post("/notes")
    def create_note_endpoint(note_data: dict, db: Session = Depends(get_db)):
        note = create_note(db, note_data)
        return {"note": note}

    # Get Note Endpoint
    @notes_router.get("/notes/{note_id}")
    def get_note_endpoint(note_id: int, db: Session = Depends(get_db)):
        note = get_note(db, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return {"note": note}

    # Get Notes Endpoint
    @notes_router.get("/notes")
    def get_notes_endpoint(db: Session = Depends(get_db)):
        notes = get_notes(db)
        return {"notes": notes}

    # Update Note Endpoint
    @notes_router.put("/notes/{note_id}")
    def update_note_endpoint(note_id: int, note_data: dict, db: Session = Depends(get_db)):
        note = update_note(db, note_id, note_data)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return {"note": note}

    # Delete Note Endpoint
    @notes_router.delete("/notes/{note_id}")
    def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
        note = delete_note(db, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return {"note": note}
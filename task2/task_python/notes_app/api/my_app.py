from fastapi import FastAPI
from .endpoints.users import users_router
from .endpoints.notes import notes_router


app = FastAPI()

app.include_router(users_router)
app.include_router(notes_router)
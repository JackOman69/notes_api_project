from fastapi import FastAPI
from pydantic import BaseModel
from notes_db_py import add_note, delete_note, change_note, get_all_notes, get_note_by_id, get_id_note, check_deleted_note

app = FastAPI()

class Note(BaseModel):
    note_name: str
    note_date: str
    note_description: str 
    user_id: int
    tags: str | None = None 

@app.get("/api/notes/")
async def get_notes():
    return get_all_notes()

@app.get("/api/notes/{note_id}")
async def get_note(note_id):
    return get_note_by_id(note_id)

@app.post("/api/notes/")
async def create_note(note: Note):
    add_note(note.note_name, note.note_date, note.note_description, note.user_id, note.tags)
    last_note_id = {"The last note's id": get_id_note()}
    return last_note_id

@app.put("/api/notes/")
async def note_into_db(note: Note, note_id):
    change_note(note_id, note.note_name, note.note_date, note.note_description, note.user_id, note.tags)
    return note

@app.delete("/api/notes/{note_id}")
async def delete_from_db(note_id: int):
    if check_deleted_note(note_id):
        return "Wow! This note has already been deleted or hasn't exist at all!"
    else:
        delete_note(note_id)
        return "Successful!"
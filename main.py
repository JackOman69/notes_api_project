import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from database import add_note, delete_note, change_note, get_all_notes, get_note_by_id, check_deleted_note, get_id_note

app = FastAPI()


class Note(BaseModel):
    note_name: str
    note_description: str
    tags: list | None = None


BASE_URL = "/api/notes/"


@app.get(BASE_URL)
async def get_notes():
    return get_all_notes()


@app.get(BASE_URL + "{note_id}")
async def get_note(note_id: int):
    return get_note_by_id(note_id)


@app.post(BASE_URL)
async def create_note(note: Note):
    '''
    Понимаешь блин блять,
    Тут не получится просто взять из note нужную нам колоночку
    Нам нужно выполнение отдельной функции под это дело, чтобы не было никаких ошибок
    У меня не получилось твоим решением, потому что выдавало ошибку, оставлю так
    '''
    add_note(note.note_name, note.note_description, note.tags)
    result = {
        "result": "Successful!",
        "Your note": get_id_note()
    }
    return result


@app.put(BASE_URL)
async def note_into_db(note: Note, note_id: int):
    change_note(note_id, note.note_name, note.note_description, note.tags)
    return get_note_by_id(note_id)


@app.delete(BASE_URL + "{note_id}")
async def delete_from_db(note_id: int):
    if check_deleted_note(note_id):
        return "This note has been already deleted or doesn't exist at all"
    else:
        delete_note(note_id)
        return "Successful!"


# https://fastapi.tiangolo.com/tutorial/debugging/
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from notes_db_py import add_note, delete_note, change_note, get_all_notes, get_note_by_id, get_id_note, check_deleted_note

app = FastAPI()

'''
Используй чаще константы, например

BASE_URL = "/api/notes/"

@app.get(BASE_URL)
async def get_notes():
    return get_all_notes()

@app.get(BASE_URL + "{note_id}")
async def get_note(note_id):
    return get_note_by_id(note_id)

Старайся чтобы код не повторялся
'''

class Note(BaseModel):
    note_name: str
    note_date: str # Проверирь есть ли в питоне формат даты или в этой хрени, как бы хотелось бы чтобы это была не строка а дата
    note_description: str
    user_id: int # Че за user_id?)
    tags: str | None = None


@app.get("/api/notes/")
async def get_notes():
    return get_all_notes()


@app.get("/api/notes/{note_id}")
async def get_note(note_id):
    return get_note_by_id(note_id)


@app.post("/api/notes/")
async def create_note(note: Note):
    '''
    Почему тут такой велосипед?
    Зачем нужна функция get_id_note, если можно возвращать 
    note_id с add_note???

    должно быть что-то типо
    new_note = add_note(note.note_name, note.note_date,
             note.note_description, note.user_id, note.tags)
    
    result = {
        result: 'OK',
        data: {
            note_id: new_note.note_id
        }
    } или вместо возвращение note_id можно возвращать всю заметку

    result = {
        result: 'OK',
        data: new_note
    }
    
    return result
    '''
    add_note(note.note_name, note.note_date,
             note.note_description, note.user_id, note.tags)
    last_note_id = {"The last note's id": get_id_note()}
    return last_note_id


@app.put("/api/notes/")
async def note_into_db(note: Note, note_id):
    '''
    Тоже самое. 
    Почему мы возвращем то что отправил фронтенд.

    функция change_note должна возвращать нам заметку полность,
    вместе с note_id и всех фигней
    '''
    change_note(note_id, note.note_name, note.note_date,
                note.note_description, note.user_id, note.tags)
    return note


@app.delete("/api/notes/{note_id}")
async def delete_from_db(note_id: int):
    '''
    Никаких wow и Successful. Я про тебе это написал в туду

    if check_deleted_note(note_id):
        return "Wow! This note has already been deleted or hasn't exist at all!"
    Можно пользователю не возвращать такую фигню, а постоянно слать 'OK' типо даэе если он прислал id, которого не существует, Всегда ок
    '''
    if check_deleted_note(note_id):
        return "Wow! This note has already been deleted or hasn't exist at all!"
    else:
        delete_note(note_id)
        return "Successful!"

# https://fastapi.tiangolo.com/tutorial/debugging/
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

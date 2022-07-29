import sqlite3

def add_note(note_name, note_date, note_description, user_id, tags):
    with sqlite3.connect("notes_api_database/notes_db.db") as db:
        cursor = db.cursor()
        query = """ INSERT INTO notes(note_name, note_date, note_description, user_id, tags) 
                    VALUES("{}", "{}", "{}", "{}", "{}")""".format(note_name, note_date, note_description, user_id, tags)
        cursor.execute(query)

def delete_note(note_id):
    with sqlite3.connect("notes_api_database/notes_db.db") as db:
        cursor = db.cursor()
        delete_query = """ DELETE FROM notes WHERE note_id = {}""".format(note_id)
        cursor.execute(delete_query)

def check_deleted_note(note_id):
    with sqlite3.connect("notes_api_database/notes_db.db") as db:
        cursor = db.cursor()
        check_deleted_id = cursor.execute("""SELECT note_id FROM notes WHERE note_id = {}""".format(note_id))
        try:
            check_deleted_id.fetchone()[0]
        except:
            return True

def change_note(note_id, note_name, note_date, note_description, user_id, tags):
     with sqlite3.connect("notes_api_database/notes_db.db") as db:
        cursor = db.cursor()
        change_note_name_query = """UPDATE notes 
                                    SET note_name = "{}", 
                                    note_date = "{}", 
                                    note_description = "{}", 
                                    user_id = {}, 
                                    tags = "{}"
                                    WHERE note_id = {} """.format(note_name, note_date, note_description, user_id, tags, note_id)
        cursor.execute(change_note_name_query)

def get_all_notes():
    with sqlite3.connect("notes_api_database/notes_db.db") as db:
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM notes""")
        get_all_notes_query = cursor.fetchall()
        result_dict = []
        for row in get_all_notes_query:
            get_all_notes_dict={"note_id": row[0], 
                                "note_name": row[1], 
                                "note_date": row[2], 
                                "note_description": row[3], 
                                "user_id": row[4], 
                                "tags": row[5]}
            result_dict.append(get_all_notes_dict)
        return result_dict

def get_note_by_id(note_id):
    with sqlite3.connect("notes_api_database/notes_db.db") as db:
        cursor = db.cursor()
        get_note_by_id_query = cursor.execute("""SELECT * FROM notes WHERE note_id = {}""".format(note_id))
        for row in get_note_by_id_query:
            single_note_dict={"note_id": row[0], 
                                "note_name": row[1], 
                                "note_date": row[2], 
                                "note_description": row[3], 
                                "user_id": row[4], 
                                "tags": row[5]}
        return single_note_dict

def get_id_note():
    with sqlite3.connect("notes_api_database/notes_db.db") as db:
        cursor = db.cursor()
        get_id_note_query = cursor.execute("""SELECT note_id FROM notes ORDER BY note_id DESC LIMIT 1""")
        return get_id_note_query.fetchone()[0]
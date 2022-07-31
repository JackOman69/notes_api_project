import sqlite3

with sqlite3.connect("database/notes.db") as db:
    cursor = db.cursor()
    initialization_query = """CREATE TABLE IF NOT EXISTS notes(note_id INT PRIMARY KEY, note_name TEXT, note_date TEXT, note_description TEXT, tags TEXT)"""
    cursor.execute(initialization_query)


def add_note(note_name, note_description, tags):
    with sqlite3.connect("database/notes.db") as db:
        cursor = db.cursor()
        cursor.executescript(
            """SELECT datetime("now","localtime");
                INSERT INTO notes(note_name, note_date, note_description, tags) VALUES("{}", datetime("now","localtime"), "{}", "{}")""".format(note_name, note_description, tags)
        )


def delete_note(note_id):
    with sqlite3.connect("database/notes.db") as db:
        cursor = db.cursor()
        delete_query = """ DELETE FROM notes WHERE note_id = {}""".format(
            note_id)
        cursor.execute(delete_query)


def check_deleted_note(note_id):
    with sqlite3.connect("database/notes.db") as db:
        cursor = db.cursor()
        check_deleted_id = cursor.execute(
            """SELECT note_id FROM notes WHERE note_id = {}""".format(note_id))
        try:
            check_deleted_id.fetchone()[0]
        except:
            return True


def change_note(note_id, note_name, note_description, tags):
    with sqlite3.connect("database/notes.db") as db:
        cursor = db.cursor()
        change_note_name_query = """UPDATE notes 
                                    SET note_name = "{}", 
                                    note_description = "{}",  
                                    tags = "{}"
                                    WHERE note_id = {} """.format(note_name, note_description, tags, note_id)
        changed_note = cursor.execute(change_note_name_query)
        return changed_note


def get_all_notes():
    with sqlite3.connect("database/notes.db") as db:
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM notes""")
        get_all_notes_query = cursor.fetchall()
        result_dict = []
        for row in get_all_notes_query:
            get_all_notes_dict = {"note_id": row[0],
                                  "note_name": row[1],
                                  "note_date": row[2],
                                  "note_description": row[3],
                                  "tags": row[4]}
            result_dict.append(get_all_notes_dict)
        return result_dict


def get_note_by_id(note_id):
    with sqlite3.connect("database/notes.db") as db:
        cursor = db.cursor()
        get_note_by_id_query = cursor.execute(
            """SELECT * FROM notes WHERE note_id = {}""".format(note_id))
        for row in get_note_by_id_query:
            single_note_dict = {"note_id": row[0],
                                "note_name": row[1],
                                "note_date": row[2],
                                "note_description": row[3],
                                "tags": row[4]}
        return single_note_dict


def get_id_note():
    with sqlite3.connect("database/notes.db") as db:
        cursor = db.cursor()
        get_id_note_query = cursor.execute(
            """SELECT note_id FROM notes ORDER BY note_id DESC LIMIT 1""")
        return get_id_note_query.fetchone()[0]

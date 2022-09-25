import sqlite3
import time
import uuid
from server.utils.read_config import config

DB_PATH = config["server"]["db_path"]

db_connection = sqlite3.connect(DB_PATH)


def does_table_exist(table_name):
    db = db_connection.cursor()
    result = db.execute(
        f"SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{table_name}';"
    ).fetchone()
    db.close()
    return result[0] == 1


def create_messages_table():
    db = db_connection.cursor()
    result = db.execute(
        """CREATE TABLE Messages
    (id text, text text, date integer, user_id text, conversation_id text)"""
    )
    db_connection.commit()
    db.close()


def create_users_table():
    db = db_connection.cursor()
    result = db.execute(
        """CREATE TABLE Users
    (id text, name text)"""
    )
    db_connection.commit()
    db.close()


def ensure_tables_exist():
    db = db_connection.cursor()
    if not does_table_exist("Messages"):
        create_messages_table()
    if not does_table_exist("Users"):
        create_users_table()
    db.close()


def get_messages():
    db = db_connection.cursor()
    result = db.execute("SELECT * FROM Messages")
    for row in result:
        print(row)
    db.close()


def get_conversation_messages(conversation_id, top: int = 1000):
    db = db_connection.cursor()
    query = f' \
    SELECT * FROM ( \
      SELECT * FROM Messages WHERE conversation_id="{conversation_id}" ORDER BY date DESC LIMIT {top} \
    ) ORDER BY date ASC \
  '
    result = db.execute(query)
    list = []
    for row in result:
        dict = {}
        dict["id"] = row[0]
        dict["text"] = row[1]
        dict["date"] = row[2]
        dict["user_id"] = row[3]
        dict["conversation_id"] = row[4]
        list.append(dict)
    db.close()
    return list


def add_message(text, user_id, conversation_id):
    db = db_connection.cursor()

    current_time_ms = int(time.time_ns() / 1000)
    id = str(uuid.uuid4())
    # need to escape text for it to be correctly inserted into the db
    escaped_text = text.replace("'", "''")
    db.execute(
        f"INSERT INTO Messages VALUES ('{id}','{escaped_text}',{current_time_ms},'{user_id}','{conversation_id}')"
    )
    db_connection.commit()
    db.close()

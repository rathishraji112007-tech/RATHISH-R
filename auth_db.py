import sqlite3
import hashlib


def connect_db():
    return sqlite3.connect("pocketsmart.db")


def create_table():
    conn = connect_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()


def register_user(username, password):
    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    try:
        conn = connect_db()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        conn.close()
        return True

    except sqlite3.IntegrityError:
        return False


create_table()

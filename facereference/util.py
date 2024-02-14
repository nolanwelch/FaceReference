import sqlite3
from flask import current_app, g
from facereference import app


class Cursor:
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


def withCursor(func):
    """cursor must be the first argument in the header
    of a function decorated with this wrapper.

    This should be the final decorator before the function."""

    def wrapper(*args, **kwargs):
        with Cursor(get_db()) as cursor:
            return func(cursor, *args, **kwargs)

    return wrapper


# database methods guide: https://flask.palletsprojects.com/en/3.0.x/tutorial/database/


def get_db() -> sqlite3.Connection:

    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db():
    db = g.pop("db", None)
    if db:
        db.close()


@withCursor
def queryUser(cursor: sqlite3.Cursor, name):
    q = """SELECT * FROM users
                   WHERE username=?"""
    user = cursor.execute(q, (name,)).fetchone()
    return user

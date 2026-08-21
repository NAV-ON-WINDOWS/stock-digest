import sqlite3

DB_PATH = "subscribers.db"


def init_db():
    """Creates the subscribers table if it doesn't already exist."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL
            )
        """)


def add_subscriber(email):
    """Adds an email to the database. Ignores it if already present."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO subscribers (email) VALUES (?)",
            (email,)
        )


def get_all_subscribers():
    """Returns a list of all subscribed email addresses."""
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("SELECT email FROM subscribers").fetchall()
    return [row[0] for row in rows]
import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/jobs.db")


def get_connection():
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT NOT NULL,
            title TEXT NOT NULL,
            location TEXT,
            source TEXT,
            url TEXT,

            ai_score INTEGER DEFAULT 0,
            recommendation TEXT,
            matched_skills TEXT,

            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("✅ Database initialized successfully.")
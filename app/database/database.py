import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/jobs.db")


def get_connection():

    DATABASE_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)

    conn.row_factory = sqlite3.Row

    return conn


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    # ---------------- USERS ----------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT NOT NULL UNIQUE,

            password TEXT NOT NULL,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP

        )

    """)

    # ---------------- USER PROFILE ----------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS profiles (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            resume_path TEXT,

            profile_json TEXT,

            experience INTEGER DEFAULT 0,

            FOREIGN KEY(user_id)

            REFERENCES users(id)

        )

    """)

    # ---------------- JOBS ----------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,

            title TEXT,

            location TEXT,

            source TEXT,

            url TEXT,

            ai_score INTEGER,

            recommendation TEXT,

            matched_skills TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP

        )

    """)

    # ---------------- SAVED JOBS ----------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS saved_jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            job_id INTEGER,

            saved_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)

            REFERENCES users(id),

            FOREIGN KEY(job_id)

            REFERENCES jobs(id)

        )

    """)

    conn.commit()

    conn.close()

    print("✅ Database initialized.")
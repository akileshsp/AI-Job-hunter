import sqlite3
from app.database.database import get_connection


class SavedJobsService:

    def __init__(self):
        self.create_table()

    def create_table(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS saved_jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            company TEXT,

            title TEXT,

            location TEXT,

            source TEXT,

            url TEXT,

            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    def save(self, user_id, job):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""

        INSERT INTO saved_jobs
        (
            user_id,
            company,
            title,
            location,
            source,
            url
        )

        VALUES (?,?,?,?,?,?)

        """, (

            user_id,

            job.company,

            job.title,

            job.location,

            job.source,

            job.url

        ))

        conn.commit()
        conn.close()

    def get_saved_jobs(self, user_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""

        SELECT

        company,
        title,
        location,
        source,
        url

        FROM saved_jobs

        WHERE user_id=?

        ORDER BY saved_at DESC

        """, (user_id,))

        rows = cur.fetchall()

        conn.close()

        return rows
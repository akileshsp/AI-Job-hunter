import os
import sqlite3
from datetime import datetime

DB = "data/jobs.db"

os.makedirs("data", exist_ok=True)


def get_connection():

    conn = sqlite3.connect(DB)

    conn.execute("""

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

            created_at TEXT
        )

    """)

    return conn


def save_job(job):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        INSERT INTO jobs (

            company,
            title,
            location,
            source,
            url,
            ai_score,
            recommendation,
            matched_skills,
            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        job.company,
        job.title,
        job.location,
        job.source,
        job.url,
        getattr(job, "match_score", 0),
        getattr(job, "recommendation", ""),
        ", ".join(getattr(job, "matched_skills", [])),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    conn.commit()
    conn.close()


def get_all_jobs():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        SELECT

            company,
            title,
            location,
            source,
            url,
            ai_score,
            recommendation,
            matched_skills,
            created_at

        FROM jobs

        ORDER BY id DESC

    """)

    rows = cur.fetchall()

    conn.close()

    return rows


def total_jobs():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM jobs")

    total = cur.fetchone()[0]

    conn.close()

    return total
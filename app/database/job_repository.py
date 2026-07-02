import os
import sqlite3
from datetime import datetime

DB = "data/jobs.db"

os.makedirs("data", exist_ok=True)


def get_connection():

    conn = sqlite3.connect(DB)

    conn.row_factory = sqlite3.Row

    conn.execute("""
    CREATE TABLE IF NOT EXISTS jobs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company TEXT NOT NULL,

        title TEXT NOT NULL,

        location TEXT,

        source TEXT,

        url TEXT UNIQUE,

        ai_score INTEGER DEFAULT 0,

        recommendation TEXT,

        matched_skills TEXT,

        created_at TEXT

    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS saved_jobs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        job_id INTEGER NOT NULL,

        saved_date TEXT,

        UNIQUE(user_id, job_id)

    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS applied_jobs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        job_id INTEGER NOT NULL,

        status TEXT DEFAULT 'Applied',

        notes TEXT,

        applied_date TEXT,

        UNIQUE(user_id, job_id)

    )
    """)

    return conn


def save_job(job):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    INSERT OR IGNORE INTO jobs (

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

    VALUES (?,?,?,?,?,?,?,?,?)

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

    row = conn.execute(
        "SELECT id FROM jobs WHERE url=?",
        (job.url,)
    ).fetchone()

    conn.close()

    return row["id"] if row else None


def get_all_jobs():

    conn = get_connection()

    rows = conn.execute("""

    SELECT *

    FROM jobs

    ORDER BY ai_score DESC,
             created_at DESC

    """).fetchall()

    conn.close()

    return rows


def total_jobs():

    conn = get_connection()

    total = conn.execute(

        "SELECT COUNT(*) FROM jobs"

    ).fetchone()[0]

    conn.close()

    return total


# ----------------------------------------------------
# SAVED JOBS
# ----------------------------------------------------

def save_for_user(user_id, job_id):

    conn = get_connection()

    conn.execute("""

    INSERT OR IGNORE INTO saved_jobs

    (user_id, job_id, saved_date)

    VALUES (?,?,?)

    """, (

        user_id,

        job_id,

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    conn.commit()

    conn.close()


def get_saved_jobs(user_id):

    conn = get_connection()

    rows = conn.execute("""

    SELECT jobs.*

    FROM jobs

    JOIN saved_jobs

    ON jobs.id = saved_jobs.job_id

    WHERE saved_jobs.user_id=?

    ORDER BY saved_jobs.saved_date DESC

    """, (user_id,)).fetchall()

    conn.close()

    return rows


# ----------------------------------------------------
# APPLIED JOBS
# ----------------------------------------------------

def apply_job(user_id, job_id, notes=""):

    conn = get_connection()

    conn.execute("""

    INSERT OR IGNORE INTO applied_jobs

    (user_id, job_id, status, notes, applied_date)

    VALUES (?,?,?,?,?)

    """, (

        user_id,

        job_id,

        "Applied",

        notes,

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    conn.commit()

    conn.close()


def get_applied_jobs(user_id):

    conn = get_connection()

    rows = conn.execute("""

    SELECT jobs.*,
           applied_jobs.status,
           applied_jobs.applied_date

    FROM jobs

    JOIN applied_jobs

    ON jobs.id = applied_jobs.job_id

    WHERE applied_jobs.user_id=?

    ORDER BY applied_jobs.applied_date DESC

    """, (user_id,)).fetchall()

    conn.close()

    return rows


def dashboard_stats(user_id):

    conn = get_connection()

    total = conn.execute(

        "SELECT COUNT(*) FROM jobs"

    ).fetchone()[0]

    saved = conn.execute(

        "SELECT COUNT(*) FROM saved_jobs WHERE user_id=?",

        (user_id,)

    ).fetchone()[0]

    applied = conn.execute(

        "SELECT COUNT(*) FROM applied_jobs WHERE user_id=?",

        (user_id,)

    ).fetchone()[0]

    conn.close()

    return {

        "total_jobs": total,

        "saved_jobs": saved,

        "applied_jobs": applied

    }
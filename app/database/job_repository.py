from app.database.database import get_connection


def job_exists(url):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM jobs WHERE url = ?",
        (url,)
    )

    result = cursor.fetchone()
    conn.close()

    return result is not None


def save_job(job):
    if job_exists(job.url):
        print(f"⚠️ Already Exists: {job.company}")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO jobs
        (company, title, location, source, url, match_score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        job.company,
        job.title,
        job.location,
        job.source,
        job.url,
        job.match_score
    ))

    conn.commit()
    conn.close()

    print(f"✅ Saved: {job.company}")


def total_jobs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM jobs")

    total = cursor.fetchone()[0]

    conn.close()

    return total
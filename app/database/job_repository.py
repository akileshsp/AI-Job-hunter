from app.database.database import get_connection


def save_job(job):
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
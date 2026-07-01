from app.database.database import get_connection


class AppliedJobsService:

    def __init__(self):

        self.create_table()

    def create_table(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS applied_jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            company TEXT,

            title TEXT,

            location TEXT,

            source TEXT,

            url TEXT,

            status TEXT DEFAULT 'Applied',

            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        conn.commit()

        conn.close()

    def apply(self, user_id, job):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""

        INSERT INTO applied_jobs
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

    def get_applied_jobs(self, user_id):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""

        SELECT
            id,
            company,
            title,
            location,
            source,
            status,
            applied_at,
            url

        FROM applied_jobs

        WHERE user_id=?

        ORDER BY applied_at DESC

        """, (user_id,))

        rows = cur.fetchall()

        conn.close()

        return rows

    def update_status(self, job_id, status):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(

            """

            UPDATE applied_jobs

            SET status=?

            WHERE id=?

            """,

            (status, job_id)

        )

        conn.commit()

        conn.close()

    def delete(self, job_id):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(

            """

            DELETE FROM applied_jobs

            WHERE id=?

            """,

            (job_id,)

        )

        conn.commit()

        conn.close()
import sqlite3

from app.database.database import get_connection


class UserRepository:

    def create_user(self, name, email, password):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(

            """
            INSERT INTO users
            (
                name,
                email,
                password
            )
            VALUES
            (?, ?, ?)
            """,

            (
                name,
                email.lower(),
                password
            )

        )

        conn.commit()

        conn.close()

    def get_user_by_email(self, email):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(

            """
            SELECT *
            FROM users
            WHERE email=?
            """,

            (
                email.lower(),
            )

        )

        user = cur.fetchone()

        conn.close()

        return user

    def get_user(self, user_id):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(

            """
            SELECT *
            FROM users
            WHERE id=?
            """,

            (
                user_id,
            )

        )

        user = cur.fetchone()

        conn.close()

        return user
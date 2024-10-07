# app/models/user_model.py
import psycopg2
from database import get_db_connection

class UserModel:
    @staticmethod
    def create_user(username, hashed_password):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, password) VALUES (%s, %s)',
                (username, hashed_password)
            )
            conn.commit()
        except psycopg2.IntegrityError:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def find_user_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, password FROM users WHERE username = %s', (username,)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def update_user(username, new_username, hashed_password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE users SET username = %s, password = %s WHERE username = %s',
            (new_username, hashed_password, username)
        )
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated

    @staticmethod
    def partial_update_user(username, fields):
        conn = get_db_connection()
        cursor = conn.cursor()

        set_clause = ", ".join(f"{key} = %s" for key in fields)
        values = list(fields.values())
        values.append(username)

        cursor.execute(
            f'UPDATE users SET {set_clause} WHERE username = %s',
            tuple(values)
        )
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated

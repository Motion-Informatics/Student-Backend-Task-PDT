# models/db_connection.py
import sqlite3
import os

class DBConnection:
    def __init__(self, db_name="SSMD.db"):
        # Resolve the absolute path to the mounted database
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.abspath(os.path.join(base_dir, "..", "database", db_name))

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # So we get dictionary-like row access
        return conn

    def execute(self, query, params=(), fetchone=False, fetchall=False, commit=False):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute(query, params)
            result = None
            if fetchone:
                result = cursor.fetchone()
            elif fetchall:
                result = cursor.fetchall()

            if commit:
                conn.commit()

            return result
        finally:
            conn.close()
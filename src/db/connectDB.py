import sqlite3


# This class if for db connection and different operations with that database
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    # method to close the connection
    def close(self):
        self.conn.close()

    # below are methods to work with the database
    def create_user_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def insert_user(self, first_name, last_name):
        self.cursor.execute(
            "INSERT INTO users (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def drop_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.conn.commit()

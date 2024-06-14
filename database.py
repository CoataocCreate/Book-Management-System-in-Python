# database.py

import sqlite3

class Database:
    def __init__(self, db_name="books.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                genre TEXT,
                year INTEGER
            )
        """)
        self.conn.commit()

    def add_book(self, book):
        self.cursor.execute("""
            INSERT INTO books (title, author, genre, year)
            VALUES (?, ?, ?, ?)
        """, (book.title, book.author, book.genre, book.year))
        self.conn.commit()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

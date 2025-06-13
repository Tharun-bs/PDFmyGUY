import sqlite3
import os

DB_FILE = 'database/summaries.db'

def init_db():
    os.makedirs('database', exist_ok=True)
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS summaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                summary TEXT
            )
        ''')
        conn.commit()

def save_summary(filename, summary):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO summaries (filename, summary) VALUES (?, ?)", (filename, summary))
        conn.commit()

def get_all_summaries():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT filename, summary FROM summaries")
        return c.fetchall()
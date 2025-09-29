import sqlite3

def init_db():
    conn = sqlite3.connect("customer_queries.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            query_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            email TEXT NOT NULL,
            query_description TEXT NOT NULL,
            status TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()
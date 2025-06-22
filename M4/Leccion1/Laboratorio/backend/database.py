import sqlite3

def init_db():
    conn = sqlite3.connect("vulnerable.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT
        )
    """)
    cursor.execute("INSERT INTO users (email, password) VALUES ('admin@example.com', 'admin123')")
    cursor.execute("INSERT INTO products (name, description) VALUES ('XSS Sample', '<script>alert(\"XSS\")</script>')")
    conn.commit()
    conn.close()

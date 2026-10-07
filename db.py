"""
Database Handler for Agency AI Lead Automation System
Uses SQLite to store REAL lead records, generated sites, outreach history, and analytics.
Zero demo/sample data - only real agent-discovered leads.
"""
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Leads Table (Starts 100% empty for real agent data)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        city TEXT NOT NULL,
        phone TEXT,
        address TEXT,
        rating REAL DEFAULT 0.0,
        reviews INTEGER DEFAULT 0,
        demo_url TEXT,
        status TEXT DEFAULT 'NEW',
        pitch_sent_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        notes TEXT
    )
    """)

    # Settings Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    # Default Settings
    default_settings = {
        "is_running": "true",
        "start_hour": "10",
        "end_hour": "18",
        "manish_phone": "+918299206433"
    }

    for k, v in default_settings.items():
        cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (k, v))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized (100% clean for real leads).")

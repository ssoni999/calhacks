#!/usr/bin/env python3
"""
Add is_rejected column to candidates table
"""
import sqlite3

def migrate():
    conn = sqlite3.connect('recruitai.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('ALTER TABLE candidates ADD COLUMN is_rejected BOOLEAN DEFAULT 0')
        conn.commit()
        print("✅ Added is_rejected column to candidates table")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e):
            print("✅ Column already exists, skipping migration")
        else:
            raise
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()

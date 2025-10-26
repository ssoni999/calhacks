#!/usr/bin/env python3
"""
Migrate database to add cultural_fit_score column
"""
import sqlite3

def migrate():
    conn = sqlite3.connect('recruitai.db')
    cursor = conn.cursor()
    
    try:
        # Add cultural_fit_score column
        cursor.execute('ALTER TABLE candidates ADD COLUMN cultural_fit_score FLOAT')
        conn.commit()
        print("✅ Added cultural_fit_score column to candidates table")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e):
            print("✅ Column already exists, skipping migration")
        else:
            raise
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()

#!/usr/bin/env python3
"""
Database migration script
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
            print("✅ cultural_fit_score column already exists")
        else:
            raise
    
    try:
        # Add is_rejected column
        cursor.execute('ALTER TABLE candidates ADD COLUMN is_rejected BOOLEAN DEFAULT 0')
        conn.commit()
        print("✅ Added is_rejected column to candidates table")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e):
            print("✅ is_rejected column already exists")
        else:
            raise
    
    conn.close()

if __name__ == "__main__":
    migrate()

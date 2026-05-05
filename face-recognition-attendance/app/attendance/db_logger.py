import sqlite3
from datetime import datetime

# Init database 
def init_db(db_path):
    # Create database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    
def mark_attendance(name, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
        
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
        
    # Prevent duplicate (same name, date) entries
    cursor.execute('''
        SELECT * FROM attendance WHERE name = ? AND date = ?
    ''', (name, date_str))
        
    result = cursor.fetchone()
    if result is None:
        cursor.execute('''
            INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)
        ''', (name, date_str, time_str))
        
        conn.commit()
        print(f"[DB] Marked attendance for {name} at {date_str} {time_str}")
    else:
        print(f"[DB] Attendance for {name} on {date_str} already marked.")
        
    conn.close()
            
# Fetch all records 
def fetch_all_records(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
        
    cursor.execute('SELECT * FROM attendance ORDER BY date DESC, time DESC')
    records = cursor.fetchall()
        
    conn.close()
    return records
    
# Fetch today's records
def fetch_today_records(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
        
    today_str = datetime.now().strftime("%Y-%m-%d")
    cursor.execute('''
        SELECT * FROM attendance WHERE date = ? ORDER BY time DESC
    ''', (today_str,))
    records = cursor.fetchall()
        
    conn.close()
    return records

# Reset database 
def reset_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
        
    cursor.execute('DROP TABLE IF EXISTS attendance')
    conn.commit()
    conn.close()
    print("[DB] Attendance records reset.")

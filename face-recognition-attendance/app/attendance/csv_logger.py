import csv 
import os 
from datetime import datetime

# Init CSV file
def init_csv(file_path):
    """
    Create CSV file with headers if it doesn't exist.
    """
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Time"])
        print(f"[CSV] Created new CSV file at {file_path}")
    else:
        print(f"[CSV] CSV file already exists at {file_path}")

# Mark attendance in CSV
def mark_attendance(name, file_path):
    """
    Append attendance record to CSV file.
    """
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    # Ensure file exists
    init_csv(file_path)
    
    # Read existing records
    already_marked = False  
    
    # Check for duplicate (same name, date) entries
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        
        for row in reader:
            if len(row) >= 2:
                existing_name, existing_date = row[0], row[1]
                if existing_name == name and existing_date == date_str:
                    already_marked = True
                    print(f"[CSV] Attendance for {name} on {date_str} already marked.")
                    break
        
    if not already_marked:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, date_str, time_str])
        print(f"[CSV] Marked attendance for {name} at {date_str} {time_str}")
    else:
        print(f"[CSV] Attendance for {name} on {date_str} already marked.")
        
# Fetch all records from CSV
def read_all(file_path):
    """
    Read all attendance records from CSV file.
    """
    if not os.path.exists(file_path):
        print(f"[CSV] No CSV file found at {file_path}")
        return []
    
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        records = list(reader)
    
    return records

# Get today's records from CSV
def read_today(file_path):
    """
    Read today's attendance records from CSV file.
    """
    if not os.path.exists(file_path):
        print(f"[CSV] No CSV file found at {file_path}")
        return []
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_records = []
    
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        
        for row in reader:
            if len(row) >= 2:
                existing_date = row[1]
                if existing_date == today_str:
                    today_records.append(row)
    
    return today_records

# Reset CSV file (delete all records)
def reset_csv(file_path):
    """
    Reset CSV file by deleting all records (keep header).
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])
    print(f"[CSV] Reset CSV file at {file_path}")
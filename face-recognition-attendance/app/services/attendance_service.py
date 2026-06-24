import csv 
import os 
from datetime import datetime

class AttendanceService:
    def __init__(self, file_path = "data/attendance.csv"):
        self.file_path = file_path
        self.marked_names = set()
        
        # Create file if it doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Date", "Time"])
                
    def mark_attendance(self, name):
        """
        Marks attendance for a given name.
        If the name has already been marked, it won't be added again.
        """
        if name in self.marked_names:
            return  # Already marked
        
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, date_str, time_str])
        
        self.marked_names.add(name)
        
        print(f"Attendance marked for {name} at {date_str} {time_str}")
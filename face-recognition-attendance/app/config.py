import os 

# Base paths 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGES_DIR = os.path.join(DATA_DIR, "images")
LOGS_DIR = os.path.join(DATA_DIR, "logs")
DB_DIR = os.path.join(DATA_DIR, "db")

# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)

# File paths 
CSV_FILE = os.path.join(LOGS_DIR, "Attendance.csv")
DB_FILE = os.path.join(DB_DIR, "attendance.db")

# Camera settings
CAMERA_INDEX = 0
FRAME_SCALE = 0.25
WINDOW_NAME = "Face Recognition Attendance"

# Face recognition settings
TOLERANCE = 0.6
MODEL = "hog"  # or "cnn" for GPU acceleration

# Confifence calculation tweak
MIN_CONFIDENCE = 70                 # Reject if below (%)

# Liveliness (Anti-spoofing) settings
LIVELINESS_THRESHOLD = 50000        # Lower = more sensitive 

# UI settings
FONT = 0 # cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.8
FONT_COLOR = (255, 255, 255) # White

BOX_COLOR = (0, 255, 0) # Green
BOX_COLOR_UNKNOWN = (0, 0, 255) # Red

# Performance 
SHOW_FPS = True

# Debug mode 
DEBUG = True 
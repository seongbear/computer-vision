# Face Recognition Attendance System

A real-time face recognition system for automated attendance tracking with anti-spoofing detection using computer vision.

## Features

- **Real-time Face Recognition**: Detects and recognizes faces from webcam input using MediaPipe and scikit-learn
- **Anti-Spoofing Detection**: Motion-based liveliness detection to prevent spoofing attacks with static images
- **Dual Logging**: Records attendance to both CSV files and SQLite database
- **Confidence Scoring**: Validates recognized faces with configurable confidence thresholds
- **Performance Monitoring**: Built-in FPS counter for performance tracking
- **Docker Support**: Containerized deployment with Docker and Docker Compose
- **Modular Architecture**: Separated concerns with dedicated modules for face detection, encoding, and recognition

## Project Structure

```
face-recognition-attendance/
├── app/                          # Main application package
│   ├── main.py                  # Application entry point
│   ├── config.py                # Configuration settings
│   ├── face/                    # Face recognition modules
│   │   ├── detector.py          # Face detection
│   │   ├── encoder.py           # Face encoding
│   │   └── recognizer.py        # Face recognition
│   ├── attendance/              # Attendance logging modules
│   │   ├── csv_logger.py        # CSV logging
│   │   └── db_logger.py         # Database logging
│   ├── liveliness/              # Anti-spoofing module
│   │   └── motion_detector.py   # Motion detection for liveliness
│   ├── services/                # Business logic services
│   │   ├── recognition_service.py   # Recognition service
│   │   └── attendance_service.py    # Attendance service
│   ├── ui/                      # User interface
│   │   └── display.py           # Video display and rendering
│   └── utils/                   # Utility functions
│       ├── drawing.py           # Drawing utilities
│       ├── fps.py               # FPS counter
│       └── image_loader.py      # Image loading utilities
├── data/                        # Data directory
│   ├── images/                  # Known face images for encoding
│   ├── logs/                    # Attendance logs (CSV)
│   ├── db/                      # Database files (SQLite)
│   └── attendance.csv           # Attendance records
├── scripts/                     # Utility scripts
│   ├── encode_faces.py          # Face encoding script
│   └── reset_db.py              # Database reset script
├── tests/                       # Unit tests
│   ├── face/                    # Face recognition tests
│   │   ├── detector_test.py
│   │   ├── encoder_test.py
│   │   └── recognizer_test.py
│   └── liveliness/              # Liveliness detection tests
│       └── motion_detector_test.py
├── Dockerfile                   # Docker container definition
├── docker-compose.yml           # Docker Compose configuration
├── pyproject.toml              # Project metadata and dependencies
└── requirements.txt            # Python dependencies
```

## Requirements

- **Python**: >= 3.11
- **OpenCV**: 4.13.0 or later
- **MediaPipe**: 0.10.9
- **Scikit-learn**: 1.8.0 or later
- **NumPy**: 2.4.4 or later
- **CVZone**: 1.6.1 or later
- **Webcam**: USB or built-in camera device

## Installation

### Option 1: Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd face-recognition-attendance
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Docker Installation

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Docker image with all dependencies
   - Mount your local `data/` directory for persistence
   - Run the application in a container

## Quick Start

### 1. Prepare Face Images

Place face images in the `data/images/` directory with the following structure:
```
data/images/
├── person1/
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── ...
├── person2/
│   ├── photo1.jpg
│   └── ...
└── ...
```

Use clear, front-facing photos for best results.

### 2. Run the Application

```bash
python -m app.main
```

Or if you prefer to run as a module from the project root:
```bash
cd app
python main.py
```

### 3. Monitor Attendance

- **CSV Logs**: Check `data/logs/Attendance.csv` for attendance records
- **Database**: SQLite database stored in `data/db/attendance.db`

## Configuration

All settings can be modified in [app/config.py](app/config.py):

```python
# Camera settings
CAMERA_INDEX = 0              # Webcam index (0 = default)
FRAME_SCALE = 0.25           # Frame downscaling for performance
WINDOW_NAME = "Face Recognition Attendance"

# Face recognition settings
TOLERANCE = 0.6              # Face recognition tolerance
MODEL = "hog"                # Detection model: "hog" or "cnn"
MIN_CONFIDENCE = 70          # Minimum confidence threshold (%)

# Liveliness (Anti-spoofing) settings
LIVELINESS_THRESHOLD = 50000 # Motion sensitivity (lower = more sensitive)

# UI settings
FONT = 0                      # Font selection
FONT_SCALE = 0.8            # Font size
BOX_COLOR = (0, 255, 0)      # Green for known faces
BOX_COLOR_UNKNOWN = (0, 0, 255)  # Red for unknown faces

# Performance
SHOW_FPS = True              # Display FPS counter
DEBUG = True                 # Enable debug mode
```

## Usage

### Basic Operation

1. **Start the application** - The webcam feed will display with real-time face detection
2. **Face Detection** - Known faces are highlighted with green boxes, unknown faces with red boxes
3. **Attendance Logging** - Recognized faces are automatically logged to CSV and database
4. **Motion Detection** - Anti-spoofing system ensures live faces only

### Controls

- **Press 'Q'** or **ESC** to exit the application
- **FPS Display** - Shows performance metrics in top-left corner

### Utility Scripts

**Encode known faces** (if needed):
```bash
python scripts/encode_faces.py
```

**Reset the database**:
```bash
python scripts/reset_db.py
```

## Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/face/detector_test.py
python -m pytest tests/face/encoder_test.py
python -m pytest tests/face/recognizer_test.py
python -m pytest tests/liveliness/motion_detector_test.py

# Run with verbose output
python -m pytest tests/ -v
```

## Performance Tips

1. **Use "hog" model** for CPU-based systems (default)
2. **Use "cnn" model** if you have GPU support for faster detection
3. **Adjust FRAME_SCALE** in config to balance quality vs. speed (lower values = faster)
4. **Increase LIVELINESS_THRESHOLD** if experiencing false positives
5. **Optimize face images** - Use high-quality, well-lit photos in training data

## Troubleshooting

### Camera Not Opening
- Check camera permissions
- Verify camera is not in use by another application
- Try changing `CAMERA_INDEX` in config (0, 1, 2, etc.)

### Poor Face Recognition
- Add more training images per person
- Ensure images are clear and well-lit
- Adjust `TOLERANCE` value (lower = stricter matching)
- Check that `MIN_CONFIDENCE` threshold is appropriate

### Liveliness False Positives/Negatives
- Adjust `LIVELINESS_THRESHOLD` value in config
- Ensure adequate lighting in the environment
- Verify camera has good framerate

### Docker Issues
- Ensure Docker and Docker Compose are installed
- Check that `/dev/video0` is accessible (Linux)
- For Windows/Mac, verify Docker Desktop is running with proper device forwarding

## Dependencies

- **opencv-python**: Computer vision and image processing
- **mediapipe**: Face detection and hand tracking
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms for face recognition
- **cvzone**: Computer vision convenience functions

## License

[Add your license information here]

## Contributing

[Add contributing guidelines here]

## Support

For issues, questions, or suggestions, please open an issue in the repository.

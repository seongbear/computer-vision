# Virtual Drag and Drop

A computer vision application that enables virtual drag-and-drop functionality using hand gestures. This project uses OpenCV and MediaPipe to track hand movements and allows users to interact with virtual objects on screen through pinch gestures.

## Features

- **Hand Tracking**: Real-time hand detection and landmark tracking using MediaPipe
- **Gesture Recognition**: Pinch gesture detection for drag-and-drop operations
- **Virtual Objects**: Interactive colored rectangles that can be dragged around the screen
- **Real-time Processing**: Smooth 720p video processing at high frame rates
- **Cross-platform**: Works on Windows, Linux, and macOS
- **Docker Support**: Containerized deployment with webcam access

## Demo

The application captures video from your webcam and displays virtual objects that can be dragged using pinch gestures (thumb and index finger).

## Installation

### Prerequisites

- Python 3.10 or higher
- Webcam
- For Docker: Docker and Docker Compose

### Option 1: Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/seongbear/computer-vision.git
   cd virtual-drag-drop
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/macOS:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Docker Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/seongbear/computer-vision.git
   cd virtual-drag-drop
   ```

2. For Linux users, ensure X11 forwarding is set up.

3. For Windows/WSL2 users, install VcXsrv or Xming and set DISPLAY accordingly.

4. Run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Usage

### Running Locally

```bash
python main.py
```

### Running with Docker

```bash
docker-compose up
```

### Controls

- **Pinch Gesture**: Bring thumb and index finger close together to grab and drag objects
- **Release**: Separate thumb and index finger to release the object
- **Quit**: Press 'q' to exit the application

## Project Structure

```
virtual-drag-drop/
├── main.py                 # Main application entry point
├── pyproject.toml          # Project configuration and dependencies
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container configuration
├── docker-compose.yml      # Docker Compose setup
├── app/
│   ├── __init__.py
│   ├── hand_tracking.py    # Hand detection and tracking module
│   └── drag_object.py      # Virtual object management
└── README.md               # This file
```

## Dependencies

- **OpenCV**: Computer vision library for image processing
- **MediaPipe**: Google's ML pipeline for hand tracking
- **NumPy**: Numerical computing library
- **cvzone**: Computer vision utilities

## How It Works

1. **Hand Detection**: Uses MediaPipe's hand tracking model to detect and track hand landmarks in real-time
2. **Gesture Recognition**: Calculates distance between thumb and index finger tips to detect pinch gestures
3. **Object Interaction**: Checks if the cursor (index finger tip) is within object bounds during pinch
4. **Drag Operation**: Updates object position to follow the cursor while pinching
5. **Visual Feedback**: Changes object color to green when being dragged

## Configuration

The application is configured for 1280x720 resolution. You can modify the camera settings in `main.py`:

```python
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height
```

## Troubleshooting

### Docker Issues

- **Display Issues on Linux**: Ensure X11 forwarding is enabled
- **Display Issues on Windows**: Install and configure VcXsrv or Xming
- **Webcam Access**: Make sure `/dev/video0` is accessible and not in use by other applications

### Performance Issues

- Lower camera resolution if experiencing lag
- Ensure good lighting for better hand tracking
- Close other applications using the webcam

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Acknowledgments

- MediaPipe for hand tracking capabilities
- OpenCV community for computer vision tools
- cvzone for additional CV utilities
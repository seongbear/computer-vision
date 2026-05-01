# Gesture Volume Control (Hand Tracking)

A real-time computer vision app that adjusts Windows system volume using thumb and index finger gestures. It uses OpenCV for video capture, MediaPipe for hand landmark detection, and `pycaw` to control audio volume.

---

## 🚀 Features

* ✋ Real-time hand tracking with MediaPipe
* 🎚️ Volume control by thumb-index distance
* 🔊 System volume adjustment on Windows
* 📊 On-screen volume bar and percentage indicator
* 🧩 Clean modular Python structure

---

## 🧩 Prerequisites

* Python 3.10 or 3.11
* Windows for full volume control support
* Webcam or built-in camera

> MediaPipe may not work properly on Python 3.12 or later.

---

## ⚙️ Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

> If you use Command Prompt, run `.
venv\Scripts\activate.bat` instead.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify MediaPipe installation

```python
python -c "import mediapipe as mp; print(mp.__version__); print('solutions' in dir(mp))"
```

Expected output:

```
0.10.9
True
```

---

## ▶️ Run the App

```bash
python main.py
```

---

## 🎮 Controls

| Gesture           | Action                |
| ----------------- | --------------------- |
| Fingers close     | Decrease volume       |
| Fingers far apart | Increase volume       |
| Very close        | Click-style visual    |

Press **ESC** to exit.

---

## 🪟 Platform Support

| Feature        | Windows | macOS | Linux |
| -------------- | ------- | ----- | ----- |
| Webcam         | ✅      | ✅    | ✅    |
| Volume Control | ✅      | ❌    | ⚠️    |

---

## 🧠 How It Works

1. Capture webcam frames with OpenCV
2. Detect 21 hand landmarks using MediaPipe
3. Track thumb tip (landmark 4) and index tip (landmark 8)
4. Compute the distance between the two fingertips
5. Map distance to system volume and update audio level

---

## 📁 Project Structure

* `main.py` — app entry point and main loop
* `requirements.txt` — Python dependency list
* `README.md` — project documentation

---

## 💡 Notes

* Works best in good lighting with a clear hand view
* Keep your hand centered and stable for smoother tracking
* On Windows, `pycaw` is required for volume control

---

## 🚀 Troubleshooting

* If the webcam does not start, verify your camera is available and not used by another app
* If MediaPipe fails, confirm Python version is 3.10 or 3.11
* If volume control is not working, ensure you are on Windows and `pycaw` is installed

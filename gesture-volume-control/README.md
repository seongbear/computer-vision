# Gesture Volume Control (Hand Tracking)

A real-time computer vision project that controls system volume using hand gestures (thumb + index finger distance). Built with OpenCV, MediaPipe, and Python.

---

# 🚀 Features

* ✋ Hand tracking using MediaPipe
* 🎯 Distance-based gesture control
* 🔊 Real-time system volume adjustment (Windows)
* 📊 Visual volume bar + percentage
* 🧱 Modular architecture (clean code structure)

# ⚙️ 1. Setup Virtual Environment

## ✅ Step 1 — Check Python version

```bash
python --version
```

👉 MUST be:

* Python **3.10 or 3.11**

⚠️ MediaPipe does NOT work properly with Python 3.12+

---

## ✅ Step 2 — Create virtual environment

```bash
python -m venv venv
```

---

## ✅ Step 3 — Activate environment

### 🪟 Windows (PowerShell)

```bash
venv\Scripts\activate
```

### 🐧 macOS / Linux

```bash
source venv/bin/activate
```

---

## ✅ Step 4 — Install dependencies

Create `requirements.txt`:

```
opencv-python
mediapipe==0.10.9
numpy
pycaw
comtypes
```

Then install:

```bash
pip install -r requirements.txt
```

---

# 🧪 Verify MediaPipe (IMPORTANT)

```bash
python
```

```python
import mediapipe as mp
print(mp.__version__)
print("solutions" in dir(mp))
```

Expected:

```
0.10.9
True
```

---

# ▶️ 2. Run the Project

```bash
python -m app.main
```

---

# 🎥 Controls

| Gesture           | Action                |
| ----------------- | --------------------- |
| Fingers close     | Volume ↓              |
| Fingers far apart | Volume ↑              |
| Very close        | Click effect (visual) |

Press **ESC** to exit.

---

# 🪟 Platform Support

| Feature        | Windows   | macOS | Linux |
| -------------- | --------- | ----- | ----- |
| Webcam         | ✅         | ✅     | ✅     |
| Volume Control | ✅ (pycaw) | ❌     | ⚠️    |

---

# ❗ Common Issues & Fixes

## 1. `No module named app`

```bash
python -m app.main
```

---

## 2. `mp.solutions not found`

Fix:

```bash
pip install mediapipe==0.10.9
```

---

## 3. Camera not opening

Change:

```python
cv2.VideoCapture(1)
```

---

## 4. Volume not working

Install:

```bash
pip install pycaw comtypes
```

Ensure:

* Windows OS
* Run terminal as Administrator (if needed)

---

# 🧠 How It Works

1. Detect 21 hand landmarks
2. Extract thumb (4) and index finger (8)
3. Compute distance
4. Map distance → volume
5. Update system volume

---
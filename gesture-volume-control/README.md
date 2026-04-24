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

## ✅ Step 2 — Install uv (fast package manager)

```bash
pip install uv
```

Verify:

```bash 
uv --version
```

---

## ✅ Step 3 — Create virtual environment

```bash
uv venv
```

---

## ✅ Step 4 — Activate environment

### 🪟 Windows (PowerShell)

```bash
venv\Scripts\activate
```

### 🐧 macOS / Linux

```bash
source venv/bin/activate
```

---

## ✅ Step 5 — Install dependencies

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
uv add -r requirements.txt
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
uv run main.py
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

# 🧠 How It Works

1. Detect 21 hand landmarks
2. Extract thumb (4) and index finger (8)
3. Compute distance
4. Map distance → volume
5. Update system volume

---
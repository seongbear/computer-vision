
import cv2
import time
import numpy as np
import math
from pycaw.pycaw import AudioUtilities
from . import hand_tracking as ht

def run_volume_control():
    # Initialize Camera
    w_cam, h_cam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, w_cam)
    cap.set(4, h_cam)
    p_time = 0

    # Initialize Hand Tracker
    detector = ht.HandTracker()

    # Initialize Windows Audio 
    devices = AudioUtilities.GetSpeakers()
    volume = devices.EndpointVolume
    
    vol_range = volume.GetVolumeRange() # Typically (-65.25, 0.0, 0.03125)
    min_vol, max_vol = vol_range[0], vol_range[1]
    
    vol_bar, vol_per = 400, 0

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to grab frame from camera.")
            break

        img = detector.find_hands(img)
        lm_list = detector.find_position(img)

        if len(lm_list) != 0:
            # Tip of Thumb (ID 4) and Tip of Index Finger (ID 8)
            x1, y1 = lm_list[4][1], lm_list[4][2]
            x2, y2 = lm_list[8][1], lm_list[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            # Draw visual markers
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 8, (255, 0, 255), cv2.FILLED)

            # Calculate distance between fingers
            length = math.hypot(x2 - x1, y2 - y1)

            # Convert hand distance range [50, 300] to volume range [-65, 0]
            vol = np.interp(length, [50, 300], [min_vol, max_vol])
            vol_bar = np.interp(length, [50, 300], [400, 150])
            vol_per = np.interp(length, [50, 300], [0, 100])

            # Set system volume
            volume.SetMasterVolumeLevel(vol, None)

            # Change center color if fingers are touching (button press effect)
            if length < 50:
                cv2.circle(img, (cx, cy), 11, (0, 255, 0), cv2.FILLED)

        # Draw UI Elements
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(vol_per)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        # Calculate and draw FPS
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        cv2.imshow("Gesture Volume Control", img)
        
        # Press 'q' to safely exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
import cv2 
import numpy as np


class MotionDetector:
    def __init__(self, min_area=5000):
        """
        min_area:
        - Mininum contour area to be considered as motion. Adjust this value based on the size of the objects you want to detect.
        """
        self.min_area = min_area
        self.prev_frame = None

    def detect_motion(self, frame):
        """
        Input:
        - current frame 
        
        Returns:
        - motion_detected (True or False)
        - processed frame (for visualization, optional)
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_frame is None:
            self.prev_frame = gray
            return False, frame

        # Compute difference 
        frame_diff = cv2.absdiff(self.prev_frame, gray)
        
        # Threshold 
        thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]
        
        # Dilate to fill gaps 
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # Find contours
        contours, _ = cv2.findContours(
            thresh, 
            cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE
        )
        
        motion_detected = False
        
        for contour in contours:
            if cv2.contourArea(contour) < self.min_area:
                continue
            
            motion_detected = True
            # Draw bounding box around detected motion
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Update previous frame
        self.prev_frame = gray
        
        return motion_detected, frame
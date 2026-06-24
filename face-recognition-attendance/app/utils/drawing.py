import cv2 

class Drawer:
    def __init__(self):
        pass

    def draw_box(self, frame, box, color=(0, 255, 0), thickness=2):
        """
        Draws a rectangle around the detected face.
        
        Parameters:
        - frame: The image frame on which to draw.
        - box: A tuple (x, y, w, h) representing the bounding box.
        - color: The color of the rectangle (default is green).
        - thickness: The thickness of the rectangle border (default is 2).
        """
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
    
    def draw_label(self, img, text, position, color = (0, 255, 0)):
        x, y = position
        
        cv2.putText(
            img, 
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )
        
    def draw_fps(self, img, fps):
        cv2.putText(
            img,
            f"FPS: {fps:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
    
    def draw_status(self, img, text):
        cv2.putText(
            img,
            text,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )
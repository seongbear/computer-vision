import cv2 
import numpy as np


class FaceEncoder:
    def __init__(self, size=(100, 100)):
        self.size = size
       

    def encode(self, img, box):
        """
        Input: 
        - img: Original image (BGR)
        - box: Bounding box (x, y, w, h)
        
        Output:
        - 1D embedding vector (flattened pixel values)
        """
        x, y, w, h = box 
        
        face = img[y:y+h, x:x+w]
        
        if face.size == 0:
            return None

        # Resize to standard size
        face = cv2.resize(face, self.size)
        
        # Convert to grayscale
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
        # Normalize pixel values
        face = face / 255.0
        
        # Flatten to 1D vector
        embedding = face.flatten()
        
        return embedding
import sys 
import os 
import cv2
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.face.encoder import FaceEncoder

class FaceEncoderTest:
    def main():
        print("Testing FaceEncoder...")
        
        dummy_img = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)
        dummy_box = (100, 100, 200, 200)  # x, y, w, h
        
        encoder = FaceEncoder(size=(100, 100))
        
        embedding = encoder.encode(dummy_img, dummy_box)
        
        if embedding is not None:
            print("Success! Face was encoded.")
            print("Data type:", type(embedding))
            
            # A 100 x 100 image flattened should equal an array of 10,000 numbers
            print(f"Array shape: {embedding.shape} (Expected: (10000,))")
            
            # Check normalization (values should be between 0 and 1)
            print(f"Max pixel value: {np.max(embedding):.2f} (Expected: <= 1.0)")
            print(f"Min pixel value: {np.min(embedding):.2f} (Expected: >= 0.0)")
            
            # Show a tiny snippet of the actual array 
            print("Sample of embedding values:", embedding[:5])
        else:
            print("Failed to encode face. Check if the bounding box is valid.")
            
if __name__ == "__main__":
    FaceEncoderTest.main()
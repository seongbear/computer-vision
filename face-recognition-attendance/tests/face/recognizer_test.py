import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.face.recognizer import FaceRecognizer

class FaceRecognizerTest:
    def main():
        print("Testing FaceRecognizer...")
        
        recognizer = FaceRecognizer(threshold=0.7)
        
        person_0 = np.array([1.0, 0.9, 0.1, 0.0, 0.0])
        person_1 = np.array([0.0, 0.1, 0.9, 1.0, 0.0])
        
        known_embeddings = [person_0, person_1] 
        
        # Positive Match 
        print("\nTest Case 1: Positive Match")
        target_match = np.array([0.95, 0.85, 0.15, 0.0, 0.0])  # Similar to person_0
        
        idx, conf = recognizer.recognize(known_embeddings, target_match)
        
        if idx == 0:
            print(f"Success! Recognized as person_0 with confidence {conf:.2f}%")
        else:
            print(f"Failed to recognize person_0. Got index {idx} with confidence {conf:.2f}%")
            
        # Negative Match
        print("\nTest Case 2: Negative Match")
        
        target_stranger = np.array([0.0, 0.0, 0.0, 0.1, 1.0])  # Dissimilar to both
        
        idx, conf = recognizer.recognize(known_embeddings, target_stranger)
        
        if idx is None:
            print(f"Success! No match found as expected. Confidence: {conf:.2f}%")
        else:
            print(f"Failed! Unexpected match found at index {idx} with confidence {conf:.2f}%")
            
        # Empty Database / No Target 
        print("\nTest Case 3: Empty Database / No Target")
        idx, conf = recognizer.recognize([], target_match)
        if idx is None and conf == 0.0:
            print("Success! No known embeddings, so no match found.")

if __name__ == "__main__":
    FaceRecognizerTest.main()
          
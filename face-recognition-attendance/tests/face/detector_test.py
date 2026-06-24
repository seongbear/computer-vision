import cv2 
import mediapipe as mp
import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.face.detector import FaceDetector


class FaceDetectorTest:
    def main():
        cap = cv2.VideoCapture(0)
        detector = FaceDetector(min_detection_confidence=0.6)
        
        print("Starting face detection. Press 'q' to quit.")
        
        while True:
            success, img = cap.read()
            if not success:
                print("Failed to capture image")
                break
            
            boxes = detector.detect_faces(img)
            
            for (x, y, w, h) in boxes:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
            cv2.imshow("Face Detection Test", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    FaceDetectorTest.main()
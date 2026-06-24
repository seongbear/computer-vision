from app.face.detector import FaceDetector
from app.face.encoder import FaceEncoder
from app.face.recognizer import FaceRecognizer

class RecognitionService:
    def __init__(self, known_encodings, known_names):
        self.detector = FaceDetector()
        self.encoder = FaceEncoder()
        self.recognizer = FaceRecognizer()
        
        self.known_encodings = known_encodings
        self.known_names = known_names
        
        print(f"[INFO] Loaded {len(known_names)} known faces for recognition.")
        
    def process_frame(self, frame):
        """
        Runs full pipeline:
        - detect faces 
        - encode 
        - recognize 
        
        Returns:
        [
            {
                "box": (x, y, w, h),
                "name": str,
                "confidence": float
            }
        ]
        """
        
        results = []
        
        boxes = self.detector.detect_faces(frame)
        
        if not boxes:
            return results
        
        for box in boxes:
            try:
                embedding = self.encoder.encode(frame, box)
                
                if embedding is None:
                    continue
                
                if len(self.known_encodings) > 0:
                    match_idx, confidence = self.recognizer.recognize(self.known_encodings, embedding)
                else:
                    match_idx, confidence = None, 0.0
                
                if match_idx is not None:
                    name = self.known_names[match_idx]
                else:
                    name = "Unknown"
                    
                results.append({
                    "box": box,
                    "name": name,
                    "confidence": confidence
                })
                
            except Exception as e:
                print(f"[ERROR] Recognition failed for box {box}: {e}")
                continue
                
        return results
                    
                    
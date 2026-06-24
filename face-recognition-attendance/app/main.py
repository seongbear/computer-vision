import cv2 

# Load modules 
from app.utils.image_loader import load_images
from app.services.recognition_service import RecognitionService
from app.services.attendance_service import AttendanceService
from app.liveliness.motion_detector import MotionDetector
from app.utils.drawing import Drawer
from app.utils.fps import FPS

def main():
    # --- Load known faces ---
    known_encodings, known_names = load_images("data/images")
    
    # --- Initialize services ---
    recognition_service = RecognitionService(known_encodings, known_names)
    attendance_service = AttendanceService()
    motion_detector = MotionDetector()
    
    fps_counter = FPS()
    drawer = Drawer()
    
    # --- Start camerq ---
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True:
        success, frame = cap.read()
        
        if not success:
            print("Error: Could not read frame.")
            break
        
        # --- Motion detection ---
        motion, frame = motion_detector.detect_motion(frame)
        
        if motion:
            # --- Face recognition ---
            results = recognition_service.process_frame(frame)
            
            for result in results:
                box = result["box"]
                name = result["name"]
                confidence = result["confidence"]
                
                # --- Attendance ---
                attendance_service.mark_attendance(name)
                
                # --- UI ---
                x, y, w, h = box
                
                if name != "Unknown":
                    color = (0, 255, 0)  # Green for recognized
                    label = f"{name} ({confidence:.2f})"
                else:
                    color = (0, 0, 255)  # Red for unknown
                    label = "Unknown"
                
                drawer.draw_box(frame, box, color)
                drawer.draw_label(frame, label, (x, y - 10), color)
                
        # --- FPS ---
        fps = fps_counter.update()
        drawer.draw_fps(frame, fps)
        
        # Status
        if motion: 
            drawer.draw_status(frame, "Motion Detected")
        else:
            drawer.draw_status(frame, "No Motion")
        
        # --- Display ---
        cv2.imshow("Face Recognition Attendance", frame)
        
        # --- Exit ---
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # --- Cleanup ---
    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main() 
       
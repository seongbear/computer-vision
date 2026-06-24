import cv2
from app.face.detector import FaceDetector
from app.face.encoder import FaceEncoder
from app.face.recognizer import FaceRecognizer
from app.liveliness.motion_detector import MotionDetector

# Initialize modules 
detector = FaceDetector()
encoder = FaceEncoder()
recognizer = FaceRecognizer() 
motion_detector = MotionDetector()


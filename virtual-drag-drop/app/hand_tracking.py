import cv2 
import mediapipe as mp

class HandTracker:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.7, trackCon=0.5):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode = mode, 
            max_num_hands = maxHands, 
            min_detection_confidence = detectionCon, 
            min_tracking_confidence = trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils
        
    def find_hands(self, img, draw=True):
        # Mediapipe processes RGB images, so we need to convert the BGR image to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # Draw hand landmarks on the original image
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def find_position(self, img, handNo=0):
        lmList = []

        if self.results and self.results.multi_hand_landmarks:
            if handNo < len(self.results.multi_hand_landmarks):
                myHand = self.results.multi_hand_landmarks[handNo]

                h, w, _ = img.shape

                for lm in myHand.landmark:
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append((cx, cy))  

        return lmList
import cv2
from app import hand_tracking as ht
from app import drag_object as do
import numpy as np

p_time = 0
cap = cv2.VideoCapture(0)
cap.set(3, 1280) # Set width
cap.set(4, 720)  # Set height
    
detcetor = ht.HandTracker()


# Create multiple boxes 
objects = [
    do.DragObject(posCenter=(300, 200)),
    do.DragObject(posCenter=(600, 300)),
    do.DragObject(posCenter=(900, 400))
]
colorR = (255, 0, 255) # Initial color for the rectangle (magenta)

while True:
    success, img = cap.read()
    if not success:
        continue
    
    img = cv2.flip(img, 1) # Mirror the image for a more natural interaction
    img = detcetor.find_hands(img)
    lmList = detcetor.find_position(img)
    
    cursor = None
    isPinching = False
    
    if lmList and len(lmList) >= 8:
        cursor = lmList[8][:2] # index finger tip
        
        # Get thumb tip 
        thumb = lmList[4][:2] # thumb tip (x, y)
        
        # Distance between thumb and index 
        length = np.hypot(thumb[0] - cursor[0], thumb[1] - cursor[1])
        
        # Pinch threshold 
        if length < 40: 
            isPinching = True
            cv2.circle(img, (cursor[0], cursor[1]), 15, (0, 255, 0), cv2.FILLED)
            
    # Update and draw all objects 
    for obj in objects:
        obj.update(cursor, isPinching)
        obj.draw(img)
        
    cv2.imshow("Virtual Drag and Drop", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
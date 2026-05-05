import cv2



cap = cv2.VideoCapture(0)
cap.set(3, 1280) # Set width
cap.set(4, 720) # Set height

while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Camera Test", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to access the camera.")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2


class DragObject:
    def __init__(self, posCenter, size=(200, 200), color=(255, 0, 255)):
        self.posCenter = posCenter
        self.size = size
        self.color = color
        self.isDragging = False
        
    def update(self, cursor, isPinching):
        if cursor is None:
            return
        
        cx, cy = self.posCenter
        w, h = self.size
        
        # Collision detection math: is the cursor within the bounds of the object?
        inside = (cx - w // 2 < cursor[0] < cx + w // 2 and
            cy - h // 2 < cursor[1] < cy + h // 2)
        
        # Start dragging 
        if inside and isPinching:
            # Update position (dragging effect)
            self.isDragging = True

        # Stop dragging 
        if not isPinching:
            self.isDragging = False
        
        # Move object 
        if self.isDragging:
            self.posCenter = cursor
            
    def draw(self, img):
        cx, cy = self.posCenter
        w, h = self.size
        
        top_left = (cx - w // 2, cy - h // 2)
        bottom_right = (cx + w // 2, cy + h // 2)
        
        color = (0, 255, 0) if self.isDragging else self.color
        cv2.rectangle(img, top_left, bottom_right, color, cv2.FILLED)

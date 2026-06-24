import cv2 
import os 
from app.face.encoder import FaceEncoder

def load_images(folder_path):
    encoder = FaceEncoder()
    
    known_embeddings = []
    known_names = []
    
    for file_name in os.listdir(folder_path):
        path = os.path.join(folder_path, file_name)
        
        # Skip non-image files 
        if not file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        
        img = cv2.imread(path)
        
        if img is None:
            continue
        
        # Use whole image as face 
        h, w, _ = img.shape
        box = (0, 0, w, h)
        
        embedding = encoder.encode(img, box)
        
        if embedding is not None:
            name = os.path.splitext(file_name)[0]
            known_embeddings.append(embedding)
            known_names.append(name)
            
            print(f"Loaded and encoded {name} from {file_name}")
    
    return known_embeddings, known_names
            
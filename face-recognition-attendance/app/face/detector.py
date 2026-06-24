import cv2
import mediapipe as mp


class FaceDetector:
    def __init__(self, min_detection_confidence=0.6):
        self.mp_face_detection = mp.solutions.face_detection
        self.detector = self.mp_face_detection.FaceDetection(
            model_selection=0,
            min_detection_confidence=min_detection_confidence
        )

    def detect_faces(self, img):
        """
        Returns:
        - List of bounding boxes (x, y, w, h)
        """
        h, w, _ = img.shape
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = self.detector.process(rgb)

        boxes = []

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                bw = int(bbox.width * w)
                bh = int(bbox.height * h)

                # Ensure valid bounds
                x = max(0, x)
                y = max(0, y)
                bw = min(w - x, bw)
                bh = min(h - y, bh)

                boxes.append((x, y, bw, bh))

        return boxes
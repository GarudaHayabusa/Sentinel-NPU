import cv2
import onnxruntime as ort
import numpy as np

class VisionProtector:
    def __init__(self, model_path="models/yolov8_face.onnx"):
        # Explicitly target the Snapdragon NPU via ONNX execution providers
        self.session = ort.InferenceSession(
            model_path, 
            providers=['QNNExecutionProvider', 'CPUExecutionProvider']
        )
        self.cap = cv2.VideoCapture(0) # Open laptop webcam

    def monitor_background(self):
        """Monitors webcam feed and returns True if shoulder-surfing is detected."""
        ret, frame = self.cap.read()
        if not ret:
            return False
            
        # Preprocess frame for YOLOv8
        input_data = self.preprocess(frame)
        
        # Run inference on the Snapdragon NPU
        outputs = self.session.run(None, {"images": input_data})
        
        # Logic: If more than 1 face is detected,  we trigger the screen blur
        faces_detected = self.postprocess(outputs)
        if faces_detected > 1:
            return True #  If Unauthorized person in frame
        return False
        
    def preprocess(self, frame):
        # Resize and normalize image for YOLOv8
        img = cv2.resize(frame, (640, 640))
        img = img.transpose((2, 0, 1))
        img = np.expand_dims(img, axis=0).astype(np.float32) / 255.0
        return img

    def postprocess(self, outputs):
        # Placeholder for YOLO bounding box parsing
        # Returns number of detected faces
        return 1
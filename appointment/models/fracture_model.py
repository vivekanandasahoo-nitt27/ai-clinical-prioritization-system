from ultralytics import YOLO
import numpy as np

MODEL_PATH = "appointment/models/best.pt"

model = YOLO(MODEL_PATH)


def predict_fracture(image_path):

    results = model(image_path)

    boxes = results[0].boxes

    if boxes is None or len(boxes) == 0:
        return "No Fracture", 0.0

    # get highest confidence detection
    conf = boxes.conf.cpu().numpy()

    confidence = float(np.max(conf))

    return "Bone Fracture", confidence
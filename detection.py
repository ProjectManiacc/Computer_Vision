import cv2
from typing import List, Dict, Any
import numpy as np
from ultralytics import YOLO


def process_detections(model: YOLO, results: List, image: np.ndarray, image_name: str) -> List[Dict[str, Any]]:
    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            label = model.names[int(box.cls)]
            confidence = float(box.conf)
            detections.append({
                'image': image_name,
                'box': (x1, y1, x2, y2),
                'label': label,
                'confidence': confidence
            })
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0),
                        2)
    return detections

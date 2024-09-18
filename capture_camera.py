from connection import process_and_send_results
import cv2
from ultralytics import YOLO
from pathlib import Path
from detection import process_detections

model_path = Path.cwd() / 'runs/detect/train3/weights/best.pt'

model = YOLO(model=model_path)


def capture_and_process_frames(model: YOLO) -> None:
    cap = cv2.VideoCapture(0)
    server_ip = '127.0.0.1'
    server_port = 65432

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        detections = process_detections(model, results, frame, "camera_frame")
        
        cv2.imshow('Object Detection', frame)

        process_and_send_results(detections, server_ip, server_port)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

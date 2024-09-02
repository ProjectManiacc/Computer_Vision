import cv2
import os
from pathlib import Path
from ultralytics import YOLO
from typing import List, Dict, Any
import numpy as np

data_path = Path('dataset/data.yaml')
curr_dir = Path.cwd()
trained_model_path = Path('runs/detect/train4/weights/best.pt')
test_images_dir = Path('dataset/test/images')
output_images_dir = Path('output/test_with_detections')
test_image_path = Path('assets/valid.jpg')
output_image_path = Path('output/valid.jpg')


def train_model(dataset_path: Path) -> List:
    model = YOLO(model='yolov9t.pt')
    model.info()
    results = model.train(data=Path(curr_dir, dataset_path), epochs=10)
    return results


def evaluate_model(dataset_path: Path) -> Dict:
    model = YOLO(model=Path(curr_dir, trained_model_path))
    model.info()
    metrics = model.val(data=Path(curr_dir, dataset_path))
    print(f"Precision: {metrics.results_dict.get('metrics/precision(B)'):.4f}")
    print(f"Recall: {metrics.results_dict.get('metrics/recall(B)'):.4f}")
    print(f"mAP@0.5: {metrics.results_dict.get('metrics/mAP50(B)'):.4f}")
    print(f"mAP@0.5:0.95: {metrics.results_dict.get('metrics/mAP50-95(B)'):.4f}")
    print(f"fitness: {metrics.results_dict.get('fitness'):.4f}")
    return metrics


def test_model_on_single_image(image_path: Path, output_path: Path) -> list[dict[str, Any]]:
    model = YOLO(model=Path(curr_dir, trained_model_path))
    image = cv2.imread(str(image_path))
    results = model(image)
    image_name = os.path.basename(image_path)
    detections = process_detections(model, results, image, image_name)
    cv2.imwrite(str(output_path), image)
    return detections


def test_model_on_multiple_images(images_dir: Path, output_dir: Path) -> list[dict[str, Any]]:
    model = YOLO(model=Path(curr_dir, trained_model_path))
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    detections = []
    for image_path in images_dir.iterdir():
        image = cv2.imread(str(image_path))
        results = model(image)
        detections.extend(process_detections(model, results, image, image_path.name))
        output_image_path = Path(output_dir, image_path.name)
        cv2.imwrite(str(output_image_path), image)

    return detections


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


if __name__ == '__main__':
    # model_training = train_model(data_path)
    # model_metrics = evaluate_model(data_path)
    test_results_single = test_model_on_single_image(test_image_path, output_image_path)
    print(test_results_single)

    test_results = test_model_on_multiple_images(test_images_dir, output_images_dir)
    for detection in test_results:
        print(detection)

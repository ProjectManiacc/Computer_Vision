import os
from ultralytics import YOLO

data_path = r'dataset/data.yaml'
curr_dir = os.getcwd()
trained_model_path = r'runs/detect/train4/weights/best.pt'


def train_model(dataset_path: str):
    model = YOLO(model='yolov9t.pt')
    model.info()
    results = model.train(data=os.path.join(curr_dir, dataset_path), epochs=10)

    return results


def evaluate_model(dataset_path):
    model = YOLO(model=os.path.join(curr_dir, trained_model_path))
    model.info()
    metrics = model.val(data=os.path.join(curr_dir, dataset_path))
    print(f"Precision: {metrics.results_dict.get('metrics/precision(B)'):.4f}")
    print(f"Recall: {metrics.results_dict.get('metrics/recall(B)'):.4f}")
    print(f"mAP@0.5: {metrics.results_dict.get('metrics/mAP50(B)'):.4f}")
    print(f"mAP@0.5:0.95: {metrics.results_dict.get('metrics/mAP50-95(B)'):.4f}")
    print(f"fitness: {metrics.results_dict.get('fitness'):.4f}")
    return metrics


if __name__ == '__main__':
    # model_training = train_model(data_path)
    model_metrics = evaluate_model(data_path)

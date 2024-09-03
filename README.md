# Computer_Vision
# YOLO Object Detection Project

This project demonstrates object detection using the YOLO (You Only Look Once) model. It includes scripts for training, evaluating, and testing the model on images, as well as capturing and processing frames from a camera in real-time.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ProjectManiacc/Computer_Vision.git
    cd Computer_Vision
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

To train the model, use the `train_model` function in `main.py`. You can uncomment the relevant lines in the `if __name__ == '__main__':` block to train the model.

### Evaluating the Model

To evaluate the model, use the `evaluate_model` function in `main.py`. Uncomment the relevant lines in the `if __name__ == '__main__':` block to evaluate the model.

### Testing the Model on Images

To test the model on a single image or multiple images, use the `test_model_on_single_image` and `test_model_on_multiple_images` functions in `main.py`. Uncomment the relevant lines in the `if __name__ == '__main__':` block to test the model.

### Running the Camera Capture Script

To capture and process frames from the camera in real-time, use the `capture_and_process_frames` function. This script uses the `process_detections` function from `detection_utils.py` to process the detections.

You can run the camera capture script by uncommenting the relevant lines in the `if __name__ == '__main__':`

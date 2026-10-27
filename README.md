
# Real-Time Face Detection Using OpenCV

A Python project that detects human faces in real time using a webcam and OpenCV's Haar Cascade classifier.

## Features

- Real-time face detection through a webcam
- Uses grayscale image processing
- Draws green rectangles around detected faces
- Press `q` to exit the application

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier
- Computer Vision

## Project Files

- `face_detection.py` - Main Python application
- `haarcascade_frontalface_default.xml` - Pretrained face detection model
- `requirements.txt` - Required Python dependency

## Installation

1. Clone the repository:

   git clone https://github.com/YOUR_USERNAME/FaceDetection.git

2. Navigate to the project folder:

   cd FaceDetection

3. Install dependencies:

   pip install -r requirements.txt

## How to Run

Execute:

python face_detection.py

Allow webcam access if prompted. The application displays detected faces in a window.

Press `q` to close the window.

## Limitations

- Detection accuracy depends on lighting, face angle, and camera quality.
- Haar Cascade may miss faces or detect false positives.
- The application requires a working webcam.

## Author

AKSHATA GURNALE

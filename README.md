# yunet-face-detection

# YuNet Face Detection 🧑‍💻👀

A simple **face detection demo** using [OpenCV YuNet].  
This project loads the **YuNet ONNX model** and detects faces in an image with bounding boxes.

---

## 📌 Features
- Uses **OpenCV's FaceDetectorYN** (YuNet model).
- Detects faces in static images.
- Draws bounding boxes around detected faces.
- Easy to extend for **real-time webcam detection**.

---

## Project Structure
yunet-face-detection/
│── face_detection_yunet.py   # Main script
│── face_detection_yunet.onnx # Model file (downloaded)
│── test_pics/                # Test images
│── README.md                 # Project documentation

## 🛠️ Installation

Install required dependencies:
pip install opencv-contrib-python

## Download the YuNet ONNX model:
curl -L -o face_detection_yunet.onnx https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx

## Usage
Place your test image inside the project folder (e.g., test_pics/selfie640.png).
Run the script:
python face_detection_yunet.py
A window will pop up showing the detected faces.

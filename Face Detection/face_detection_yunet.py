import cv2 as cv

# Load YuNet from contrib
face_detector = cv.FaceDetectorYN.create(
    model="face_detection_yunet.onnx",
    config="",
    input_size=(320, 320),
    score_threshold=0.9,
    nms_threshold=0.3,
    top_k=5000,
    backend_id=cv.dnn.DNN_BACKEND_OPENCV,
    target_id=cv.dnn.DNN_TARGET_CPU
)

# Load image
img = cv.imread("test_pics/selfie640.png")
h, w, _ = img.shape
face_detector.setInputSize((w, h))

# Run detection
success, faces = face_detector.detect(img)

if success:
    for face in faces:
        x, y, w, h = map(int, face[:4])  # bounding box
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Detected Faces", img)
cv.waitKey(0)
cv.destroyAllWindows()

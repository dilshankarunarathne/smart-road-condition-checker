import cv2
from ultralytics import YOLO

model = YOLO('best.pt')

cap = cv2.VideoCapture('video.mp4')

ret, frame = cap.read()
height, width, _ = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

while cap.isOpened():
    results = model.predict(frame)

    for result in results:
        if len(result.boxes.xyxy) > 0:  # Check if there are any detections
            x1, y1, x2, y2 = map(int, result.boxes.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    out.write(frame)

    ret, frame = cap.read()

    if not ret:
        break

cap.release()
out.release()

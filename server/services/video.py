import cv2
from ultralytics import YOLO

model = YOLO('best.pt')

cap = cv2.VideoCapture('http://192.168.43.219/cam-hi.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    results = model.predict(frame)

    for result in results:
        if len(result.boxes.xyxy) > 0:
            x1, y1, x2, y2 = map(int, result.boxes.xyxy[0])
            print(f"Pothole detected at coordinates: {(x1, y1, x2, y2)}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

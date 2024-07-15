import cv2
import numpy as np
import urllib.request
from ultralytics import YOLO

url = 'http://192.168.43.219/cam-hi.jpg'

cap = cv2.VideoCapture(url)

# Load the YOLO model trained on potholes
model = YOLO('best.pt')

while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    im = cv2.imdecode(imgnp, -1)
    sucess, img = cap.read()

    # Apply the model's prediction to the frame
    results = model.predict(im)

    for result in results:
        print(result)
        for box, conf in zip(result.boxes.xyxy[0], result.boxes.conf[0]):
            x1, y1, x2, y2 = map(int, box)
            if conf > 0.6:  # Check the confidence score
                cv2.rectangle(im, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(im, f'POTHOLE {int(conf * 100)}%', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('Image', im)
    cv2.waitKey(1)

import cv2
from ultralytics import YOLO

# Load the model
model = YOLO('best.pt')

# Load the video
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    # Read the video frame by frame
    ret, frame = cap.read()

    if not ret:
        break

    # Apply the model's prediction to the frame
    results = model.predict(frame)

    # Draw the bounding boxes on the frame
    for result in results:
        if len(result.boxes.xyxy) > 0:  # Check if there are any detections
            x1, y1, x2, y2 = map(int, result.boxes.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for a key press to move to the next frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video and close the windows
cap.release()
cv2.destroyAllWindows()
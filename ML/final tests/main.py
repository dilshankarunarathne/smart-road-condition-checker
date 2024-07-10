import cv2
from ultralytics import YOLO

# Load the model
model = YOLO('best.pt')

# Load the video
cap = cv2.VideoCapture('video.mp4')

# Get the dimensions of the frame
ret, frame = cap.read()
height, width, _ = frame.shape

# Define the codec and create a VideoWriter object with the correct dimensions
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

while cap.isOpened():
    # Apply the model's prediction to the frame
    results = model.predict(frame)

    # Draw the bounding boxes on the frame
    for result in results:
        if len(result.boxes.xyxy) > 0:  # Check if there are any detections
            x1, y1, x2, y2 = map(int, result.boxes.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Write the frame into the file 'output.avi'
    out.write(frame)

    # Read the next frame
    ret, frame = cap.read()

    if not ret:
        break

# Release the video and close the windows
cap.release()
out.release()

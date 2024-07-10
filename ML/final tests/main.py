from ultralytics import YOLO

model = YOLO('best.pt')

results = model.predict(source='video.mp4', conf=0.25)

for result in results:
    print(result.boxes.xyxy)

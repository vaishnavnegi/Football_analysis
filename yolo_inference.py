from ultralytics import YOLO

#model = YOLO('yolov8x')
#Using now our new trained model from colab
model = YOLO('models/best.pt')

results = model.predict('input_videos/08fd33_4.mp4', save = True)
print(results[0])
print("=====================================")
for box in results[0].boxes:
    print(box)
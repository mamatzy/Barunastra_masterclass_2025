import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('yolov8n.pt')

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform object detection
    results = model(frame)
    height, width, *channels = frame.shape

    annotated_frame = results[0].plot()


    biggest_object = None
    max_area = 0

    # Collect bounding boxes and class names
    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        label = model.names[int(cls)].lower()
        x1, y1, x2, y2 = map(int, box)

        # Calculate area of the bounding box
        area = (x2 - x1) * (y2 - y1)

        # Find the biggest object
        if area > max_area:
            max_area = area
            biggest_object = label

    # Display the biggest object name at the bottom-left corner
    if biggest_object:
        cv2.putText(
            annotated_frame,
            f"Biggest object: {biggest_object}",
            (10, height - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2,
            cv2.LINE_AA
        )

    # Show the result
    cv2.imshow('YOLOv8 Object Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

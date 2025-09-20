# ngukur jarak antar bounding box
import cv2
import math
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
    centers = []  # list of detected centers

    # Collect bounding boxes and class names
    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        label = model.names[int(cls)].lower()

        if label in ('person','cell phone'):  # add other classes if needed
            x1, y1, x2, y2 = map(int, box)

            # Calculate center point of the object
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            centers.append((cx, cy))

            # Draw the center
            cv2.circle(annotated_frame, (cx, cy), 5, (0, 255, 0), -1)

    # If there are at least 2 objects, calculate distance between the first two
    if len(centers) >= 2:
        (xA, yA), (xB, yB) = centers[0], centers[1]

        # Draw line between objects
        cv2.line(annotated_frame, (xA, yA), (xB, yB), (0, 0, 255), 2)

        # Calculate Euclidean distance in pixels
        distance = int(math.sqrt((xB - xA)**2 + (yB - yA)**2))

        # Display distance text at midpoint of the line
        midX, midY = (xA + xB) // 2, (yA + yB) // 2
        cv2.putText(annotated_frame, f"Dist: {distance}px", (midX, midY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)

    # Show the result
    cv2.imshow('YOLOv8 Object Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

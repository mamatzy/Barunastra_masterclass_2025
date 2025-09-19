import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

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


    #====Mulai buat kode dari sini===##
    biggest_object = None
    max_area = 0

    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        label = model.names[int(cls)].lower()
        x1, y1, x2, y2 = map(int, box)

        # Kalkulasi area bounding box
        area = 

        # Cari objek dengan area terbesar
        if  :
            max_area = 
            biggest_object = label

    # Tampilkan nama objek terbesar di frame
    if biggest_object:
        

    # Tampilkan hasil
    cv2.imshow( )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

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

    results = model(frame)

    height, width, *channels = frame.shape

    annotated_frame = results[0].plot()

    ##====Mulai buat kode dari sini===##

    # buat garis vertikal di tengah kamera
    cv2.

    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls) :
        label = model.names[int(cls)].lower()

        if label in ('person') :
            x1, y1, x2, y2 = map (int,box)

            # buat titik tengah, 
            # x1 adalah koordinat paling kiri bounding box
            # x2 adalah titik paling kanan bounding box
            titik_tengah = 
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            # buat logika if else jika annotated_frame di kanan atau di kiri kamera

                cv2.putText(annotated_frame, 'Objek di kiri', (10, 30), font, 1, (0,0,0), 2, cv2.LINE_AA)
            
                cv2.putText(annotated_frame, 'Objek di kanan', (10, 30), font, 1, (0,0,0), 2, cv2.LINE_AA)

    ##====Sampai sini saja===##

    cv2.imshow('YOLOv8 Object Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
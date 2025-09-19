# ngukur jarak antar bounding box
import cv2
import math
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

    #====Mulai buat kode dari sini===##
    centers = []  

    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        label = model.names[int(cls)].lower()

        #Filter dengan class yang diinginkan seperti 'person' dengan 'cell phone'
        if label in (' '):
            x1, y1, x2, y2 = map(int, box)

            # Kalkulasi titik tengah dari objek
            cx, cy = 
            centers.append((cx, cy))

            # Gambar titik tengah
            cv2.circle( )

    # Kalau ada 2 objek atau lebih, hitung jarak antara dua objek pertama
    if len(centers) >= 2:
        (xA, yA), (xB, yB) = centers[ ], centers[ ]

        # Gambar garis antar objek
        cv2.

        # Kalkulasi jarak Euclidean dalam pixel
        distance = int(math.sqrt((xB - xA)**2 + (yB - yA)**2))

        # Tampilkan teks jarak di titik tengah garis
        midX, midY = (xA + xB) // 2, (yA + yB) // 2
        cv2.

    # Tampilkan hasil
    cv2.imshow( )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO


model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

ret, frame = cap.read()

height = frame.shape[0]
width = frame.shape[1]

garis_1   = height *2 // 5
garis_2  = height * 3 // 5

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    annotated = results.plot()

    for box, cls in zip(results.boxes.xyxy, results.boxes.cls):

        label = model.names[int(cls)].lower()
        #====Mulai buat kode dari sini===##

        #Filter dengan class yang diinginkan seperti 'person' atau 'cell phone'
        if label in ('person'):
            x1, y1, x2, y2 = map(int, box)

            # buat titik tengah, 
            # x1 adalah koordinat paling kiri bounding box
            # x2 adalah titik paling kanan bounding box
            center_x = int ()
            center_y = int ()
            
            # buat garis plus di dalam bounding box
            cv2.line(annotated, (, ),   (, ),  (255, 100, 0), 2)
            cv2.line(annotated, (, ),   (, ),  (255, 100, 0), 2)
            # buat lingkaran di tengah bounding box
            cv2.circle(annotated, (, ), 7, (0, 0, 255), -1)

    ##====Sampai sini saja===##
    cv2.imshow('Object Detection', annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


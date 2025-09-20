import cv2
from ultralytics import YOLO

# Load YOLOv8 model (YOLOv8n is the nano version, faster for real-time detection)
model = YOLO('yolov8n.pt')  # You can use other models like 'yolov8s.pt', 'yolov8m.pt', etc.

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Perform object detection using YOLOv8
    results = model(frame)

    # Get frame's height and width
    height, width, *channels = frame.shape

    # Draw bounding boxes and labels on the frame
    annotated_frame = results[0].plot()

    ##====Mulai buat kode dari sini===##

    # buat garis vertikal di tengah kamera
    cv2.line(annotated_frame, (width//2, 0), (width//2, height), (255,255,0), 5)

    # memuat list dari koordinat bounding box dan nama kelas
    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls) :
        # memasukkan nama model ke dalam label
        label = model.names[int(cls)].lower()

        # menentukan objek mana yang ingin diberi logika
        if label in ('person') : ## tambahkan class lain jika kalian mau
            # mengambil koordinat dari bounding box
            x1, y1, x2, y2 = map (int,box)

            # buat titik tengah, 
            # x1 adalah koordinat paling kiri bounding box
            # x2 adalah titik paling kanan bounding box
            titik_tengah = (x1+x2)//2

            font = cv2.FONT_HERSHEY_SIMPLEX
            # buat logika if else jika annotated_frame di kanan atau di kiri kamera
            if titik_tengah < width//2 :
                cv2.putText(annotated_frame, 'Objek di kiri', (10, 30), font, 1, (0,0,0), 2, cv2.LINE_AA)
            else :
                cv2.putText(annotated_frame, 'Objek di kanan', (10, 30), font, 1, (0,0,0), 2, cv2.LINE_AA)
            
    ##====Sampai sini saja===##

    # Display the resulting frame with bounding boxes and labels
    cv2.imshow('YOLOv8 Object Detection', annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
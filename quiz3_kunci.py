import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    ## Gambar garis silang dan lingkaran di tengah kamera

    height, width, *channels = frame.shape

    # Menggambar lingkaran
    cv2.circle(frame, (width//2, height//2), 50, (0, 0, 255), -1)

    # Menggambar garis
    cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)
    cv2.line(frame, (width, 0), (0, height), (255, 0, 0), 5)

    # Menampilkan video dengan shape
    cv2.imshow('Video Streaming with Shapes', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
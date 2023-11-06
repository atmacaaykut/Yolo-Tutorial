import cv2

# YOLOv8 modelini yükle
from ultralytics import YOLO

#Initialize YOLO with the Model Name
model = YOLO("yolov8n.pt")

# Kamera bağlantısını sağlayın (0, birinci kamera)
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir çerçeve alın
    ret, frame = cap.read()

    # resized_frame = cv2.resize(frame, (640, 640))

    # YOLOv8 ile nesne tespiti yapın
    results = model(frame)


    # Sonuçları çerçeveye çizin
    frame = results.show()[0]

    # Çerçeveyi göster
    cv2.imshow('YOLOv8 Realtime', frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Kamera bağlantısını serbest bırakın ve pencereyi kapatın
cap.release()
cv2.destroyAllWindows()

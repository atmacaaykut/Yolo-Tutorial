## Yolo pip install

pip install ultralytics==8.0.0

pip3 install torch torchvision torchaudio

yolo task=detect mode=predict model=yolov8n.pt source=image.jpg //dosya dizinindeki image.jpg adlı görsel üzerindeki nesnelerin etiketlerini geriye döndürür.

yolo task=detect mode=predict model=yolov8n.pt source=image.jpg conf=0.8//dosya dizinindeki image.jpg adlı görsel üzerindeki nesnelerin etiketlerini confident değeri 0.8'den büyükse geriye döndürür.

yolo task=detect mode=predict model=yolov8n.pt source=image.jpg save_txt=True//dosya dizinindeki image.jpg adlı görsel üzerindeki nesnelerin etiketlerini txt dosyasına yazar.

yolo task=detect mode=predict model=yolov8n.pt source=image.jpg save_txt=True save_crop=True//dosya dizinindeki image.jpg adlı görsel üzerindeki nesnelerin etiketlerini txt dosyasına yazar, bounding box'ları kırpıp ayrı ayrı kaydeder.

yolo task=detect mode=predict model=yolov8n.pt source=image.jpg save_txt=True save_crop=True hide_labels=True hide_conf=True  //dosya dizinindeki image.jpg adlı görsel üzerindeki nesnelerin etiketlerini txt dosyasına yazar, görsel üzerinde etiketleri ve güven değerlerini gizler.
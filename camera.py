from picamera2 import Picamera2, Preview
from time import sleep
import cv2

class Camera:

    def __init__(self):
        #Inizializzo la camera
        self.camera = Picamera2()
        #Setto alcune impostazioni
        #In particolare setto la preview ad un formato a 24-bit ordinato in B-G-R
        camera_config = self.camera.create_preview_configuration(lores={'format': 'RGB888'})
        self.camera.configure(camera_config)
        self.camera.start_preview(Preview.QTGL)
        self.camera.start()
        #Faccio caricare la camera
        print("Camera caricata!")

    def capture(self):
        #Catturo immagini di continuo dalla camera
           while True: 
            #Acquisisco il frame come un array numpy
            frame = self.camera.capture_array()
            #Mostro l'immagine: Nome_finestra, Immagine
            cv2.imshow("Frame", frame)
            #Controllo che non si voglia chiudere la finestra, 0xFF è una maschera
            #Controllo se si vuole terminare
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

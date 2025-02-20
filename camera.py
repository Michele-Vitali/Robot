from picamera2 import PiCamera2
from time import sleep
import cv2

class Camera:

    def __init__(self):
        #Inizializzo la camera
        self.camera = PiCamera2()
        #Setto alcune impostazioni
        self.camera.preview_Resolution.main.size = (640, 480)
        self.camera.preview_configuration.main.format = "RGB888"
        self.camera.configure("preview")
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

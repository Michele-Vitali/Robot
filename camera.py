from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2

class Camera:

    def __init__(self):
        #Inizializzo la camera
        self.camera = PiCamera()
        #Setto alcune impostazioni
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        #Faccio caricare la camera
        print("Camera caricata!")

    def capture(self):
         #Creo un array tridimensionale R-G-B
        self.videoraw = PiRGBArray(self.camera, size=(self.camera.resolution))
        #Catturo immagini di continuo dalla camera
        #I parametri sono:
        # - Output
        # - Format, salva la foto raw in un file con formato 24 bit BGR
        # - Use_video_port, dice di usare la porta per il video sulla camera
        for frame in self.camera.capture_continuous(self.videoraw, format="bgr", use_video_port=True):
            #Trasformo il frame in un array
            immagine = frame.array 
            #Mostro l'immagine: Nome_finestra, Immagine
            cv2.imshow("Frame", immagine)
            #Controllo che non si voglia chiudere la finestra, 0xFF è una maschera
            #per leggere solo gli ultimi 8 bit
            key = cv2.waitKey(1) & 0xFF
            #"Accorcio" la variabile a 0 (pulisco) per il prossimo frame
            self.videoraw.truncate(0)
            #Controllo se si è premuto q
            if key == ord("q"):
                break

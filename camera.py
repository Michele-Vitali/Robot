from picamzero import Camera
from time import sleep

class Cam:

    def __init__(self):
        self.cam = Camera()
        print("Camera caricata!")
        self.cam = cam.start.preview()
        sleep(5)
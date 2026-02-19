from gpiozero import Robot as rb
from time import sleep
from camera import Camera
from controller import Controller

class Robot:
    def __init__(self, left, right):
        self.bot = rb(left, right)
        self.camera = Camera()
        self.controller = Controller(self.bot)
        self.inizializza()
        print("Tutto caricato!")

    def botRun(self):
        try:
            '''self.botForward(duration=2.0)
            sleep(2)
            self.botBackward(duration=2.0)
            sleep(2)
            self.botRight(duration=2.0)
            sleep(2)
            self.botLeft(duration=2.0)
            sleep(2)'''
            print("Try block!")
        except KeyboardInterrupt:
            print("Esecuzione terminata!")

    def inizializza(self):
        self.camera.capture()
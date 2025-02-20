from gpiozero import Robot as rb
from time import sleep
from camera import Cam
from controller import Controller

class Robot:
    def __init__(self, left, right):
        self.bot = rb(left, right)
        self.camera = Cam()
        self.controller = Controller(self.bot)
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
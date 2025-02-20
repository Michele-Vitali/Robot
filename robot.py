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

    def botForward(self, speed=1.0, duration=1.0):
        self.bot.forward(speed)
        sleep(duration)
        self.bot.stop()

    def botBackward(self, speed=1.0, duration=1.0):
        self.bot.backward(speed)
        sleep(duration)
        self.bot.stop()

    def botRight(self, speed=1.0, duration=1.0):
        self.bot.right(speed)
        sleep(duration)
        self.bot.stop()

    def botLeft(self, speed=1.0, duration=1.0):
        self.bot.left(speed)
        sleep(duration)
        self.bot.stop()

    def botStop(self):
        self.bot.stop()

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
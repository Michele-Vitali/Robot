import math
from bluedot import BlueDot
from gpiozero import Robot as rb
from time import sleep

class Controller:

    def __init__(self, bot):
        self.bot = bot
        self.bd = BlueDot()
        #Chiamata a funzione quando viene cliccato il bottone
        self.bd.when_pressed = self.move
        #Parametri default per il movimento
        self.duration = 2.0
        self.speed = 1.0
        #Soglia per decidere la direzione
        self.dead_zone = 0.2
        #self.bd.when_realease = stop
        #self.bd.when_moved = 


    def move(self, pos):
        distanza = math.sqrt(pos.x**2 + pos.y**2)
        if distanza < self.dead_zone:
            self.bot.stop()
        else:
            if abs(pos.x) > abs(pos.y):
                if pos.x > 0:
                    print("Destra")
                    self.botRight()
                else:
                    self.botLeft()
                    print("Sinistra")
            else:
                if pos.y > 0:
                    self.botForward()
                    print("Avanti")
                else:
                    self.botBackward()
                    print("Indietro")
        print(pos.x)
        print(pos.y)

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
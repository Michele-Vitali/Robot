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
                    self.bot.right(self.speed)
                    print("Destra")
                else:
                    self.bot.left(self.speed)
                    print("Sinistra")
            else:
                if pos.y > 0:
                    self.bot.forward(self.speed)
                    print("Avanti")
                else:
                    self.bot.backward(self.speed)
                    print("Indietro")
        print(pos.x)
        print(pos.y)
        sleep(self.duration)

    '''def stop():
        pass'''
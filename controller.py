from bluedot import BlueDot
from gpiozero import Robot as rb

class Controller:

    def __init__(self, bot):
        self.bot = bot
        self.bd = BlueDot()
        #Chiamata a funzione quando viene cliccato il bottone
        self.bd.when_pressed = self.move
        #Parametri default per il movimento
        self.speed = 1.0
        #Soglia per decidere la direzione
        self.dead_zone = 0.2
        #self.bd.when_realease = stop
        #self.bd.when_moved = 


    def move(self, pos):
        if pos.y > self.dead_zone:
            self.bot.forward(self.speed)
        elif pos.y < -self.dead_zone:
            self.bot.backward(self.speed)
        else:
            self.bot.stop()

        if pos.x > self.dead_zone:
            self.bot.right(self.speed)
        elif pos.x < -self.dead_zone:
            self.bot.left(self.speed)
        else:
            self.bot.stop()

        print(pos.x)
        print(pos.y)

    '''def stop():
        pass'''
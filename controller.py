from bluedot import Bluedot

class Controller:

    def __init__(self):
        self.bd = Bluedot()
        self.bd.when_pressed = move
        self.bd.when_realease = stop
        #self.bd.when_moved = 

    def move(pos):
        print(pos.x)
        print(pos.y)
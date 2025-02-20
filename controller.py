from bluedot import BlueDot

class Controller:

    def __init__(self):
        self.bd = BlueDot()
        self.bd.when_pressed = self.move
        #self.bd.when_realease = stop
        #self.bd.when_moved = 

    def move(pos):
        print(pos.x)
        print(pos.y)

    '''def stop():
        pass'''
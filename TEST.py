from gpiozero import Robot
from time import sleep

robby = Robot(left=(7,8), right=(9,10))

robby.forward()
sleep(3)
print("Fine!")
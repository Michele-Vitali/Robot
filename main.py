import robot
from bluedot import BlueDot

if __name__ == "__main__":
    bd = BlueDot()
    bd.wait_for_press()
    print("You pressed the blue dot!")
    #bot = robot.Robot(left=(7,8), right=(9,10))
    #bot.botRun()

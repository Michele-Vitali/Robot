import logging
import time
from motor import Motor
from robot import Robot

logging.basicConfig(
    level=logging.INFO,
    filename="../../logs/robot.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

## Components ##

components = {}  #Dict

# 1. Motors
lf_motor = Motor("LF Motor")
lb_motor = Motor("LB Motor") 
rf_motor = Motor("RF Motor")
rb_motor = Motor("RB Motor")


components.update({
    lf_motor.get_name(): lf_motor,
    lb_motor.get_name(): lb_motor,
    rf_motor.get_name(): rf_motor,
    rb_motor.get_name(): rb_motor
})

# 2. Sensors

robot = Robot(components)
robot.initialize()

try:
    for i in range(50):
        lf_motor.set_pwm(i*2)
        rf_motor.set_pwm(i*2)
        lb_motor.set_pwm(i*2)
        rb_motor.set_pwm(i*2)
        time.sleep(0.2)
finally:
    robot.stop()
    print("Robot stopped")
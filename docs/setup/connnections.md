# Motor drivers

To reduce the number of GPIO pins used we "merged" same pins into 1 on a breadboard.
For each motor driver (that drives both motors from one side):
- PWMA and PWMB into PWM and connected to GPIO 25 (color <span style="color: orange">Orange</span>) and 22 for the other driver (color <span style="color: white"> White</span>)
- INA1 and INB1 into IN1 and connected to GPIO 24 (color <span style="color: yellow"> Yellow </span>) and 27 (color <span style="color: royalblue"> Blue</span>)
- INA2 and INB2 into IN2 and connected to GPIO 23 (color <span style="color: green"> Green</span>) and 17 (color <span style="color: purple"> Purple</span>)

Then since the STDBY pins of the drivers are kind of useless (their only use is to switch off the driver) we merged them together into a single one connected to GPIO 2 (color <span style="color: Brown">Brown</span>)
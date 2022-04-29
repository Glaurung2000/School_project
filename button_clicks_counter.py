# Untitled - By: ArinAdmin - Tue Aug 24 2021

import sensor, image, time
from pyb import I2C, Servo, Pin, Timer, millis


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)-

clock = time.clock()

button = Pin('P0', Pin.IN)
button_state = False
last_click_time = 0
i = 0
while(True):
    button_state = button.value()
    if button_state and (millis() > last_click_time):
        i+=1
        print(str(i)+" Click!")
        last_click_time = millis() + 1000

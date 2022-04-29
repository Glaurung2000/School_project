from pyb import Pin, Timer

#p = Pin('P4')
#tim = Timer(4, freq=50)
#ch = tim.channel(1, Timer.PWM, pin=p)
#ch.pulse_width_percent(40)

timer = Timer(2, freq=1000)         # freq in Hz = 1 * s^(-1) => freq = 1000 ~ 1 per ms
IN3 = timer.channel(3, Timer.PWM, pin=Pin('P4'))
IN4 = Pin('P5', Pin.OUT_PP)#timer.channel(4, Timer.PWM, pin=Pin('P5'))

while True:
    IN3.pulse_width_percent(50)
    #IN4.pulse_width_percent(40)
    #IN3.value(0)
    IN4.value(1)

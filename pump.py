from machine import Pin
from machine import PWM


#Peltier Pump Cycle
forward = PWM(Pin(12), freq=5)

def pwm(d):
    if d == 0:
        forward.duty(0)
    else:
        duty=round(1023 * (d/100))
        forward.duty(duty)



#Algae Pump Cycle
algeaforward = Pin(14, Pin.OUT)
algeabackward = Pin(15, Pin.OUT)

def forward():
    algeaforward.value(1)
    algeabackward.value(0)

def backward():
    algeaforward.value(0)
    algeabackward.value(1)



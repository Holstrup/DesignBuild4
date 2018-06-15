from machine import Pin
from machine import PWM
from ldr import intensity
import time


#Peltier Pump Cycle
forward = PWM(Pin(27), freq=5)

def pwm(d):
    if d == 0:
        forward = PWM(Pin(27), freq=5)
        forward.duty(1)
    else:
        forward = PWM(Pin(27), freq=5)
        dd = round(1023 * (d/100))
        forward.duty(dd)




#Algae Pump Cycle
algeaforward = Pin(14, Pin.OUT)
algeabackward = Pin(15, Pin.OUT)

def forward():
    algeaforward.value(1)
    algeabackward.value(0)

def backwards():
    algeaforward.value(0)
    algeabackward.value(1)




def getIntensity():
    pwmpump=forward.duty()
    if pwmpump!=1:
        forward.duty(1)
        inten=intensity()
        time.sleep(1)
        forward.duty(pwmpump)

    else:
        inten = intensity()
    return inten




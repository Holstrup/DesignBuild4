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

def forwards():
    algeaforward.value(1)
    algeabackward.value(0)

def backwards():
    algeaforward.value(0)
    algeabackward.value(1)

def off():
    algeaforward.value(0)
    algeabackward.value(0)




def getIntensity():
    pwmpump=forward.duty()
    print(pwmpump)
    if pwmpump!=1:
        print("Stopping pump")
        forward.duty(1)
        print("intensity")
        time.sleep(1)
        inten=intensity()
        print(inten)

        forward.duty(pwmpump)
        print(forward.duty())

    else:
        inten = intensity()
    return inten




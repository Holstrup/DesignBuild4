from machine import Pin
from machine import PWM
from ldr import intensity


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


def off():
    algeaforward.value(0)
    algeabackward.value(0)


def getIntensity():
    if algeaforward.value()==1:
        off()
        inten=intensity()
        time.sleep(0.5)
        algeaforward.value(1)

    else:
        inten = intensity()
    return inten




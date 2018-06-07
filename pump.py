from machine import Pin
from machine import PWM
import time
forward = PWM(Pin(12, Pin.OUT))
backwards=PWM(Pin(27,Pin.OUT))


def pwm(p):
    freq=p*10
    forward.freq(freq)






from machine import Pin
from machine import PWM


def setLight(freq,duty):
    light = PWM(Pin(21), freq=freq, duty=duty)

light.duty()




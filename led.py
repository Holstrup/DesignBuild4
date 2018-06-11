from machine import Pin
from machine import PWM


light = PWM(Pin(21), freq=10000)

light.duty()
light.freq()




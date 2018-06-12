from machine import Pin
from machine import PWM


light = PWM(Pin(21), freq=50000)

light.duty()
light.freq()




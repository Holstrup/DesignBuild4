from machine import Pin
from machine import PWM


light = PWM(Pin(21), freq=50000, duty=512)

light.duty()




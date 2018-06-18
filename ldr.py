from machine import Pin
from machine import ADC
#lightsensor
import time
#  is  gpio 33
lSens = ADC(Pin(33, Pin.IN))
lSens.width(ADC.WIDTH_12BIT)

def intensity():
    adc_read=[]
    for i in range(50):
        time.sleep(0.001)
        adc_read.append(lSens.read())
    adc_read = sorted(adc_read)
    intens = sum(adc_read[20:30])/10
    return intens

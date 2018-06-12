from machine import Pin
from machine import ADC
#lightsensor is  gpio 33
lSens = ADC(Pin(33, Pin.IN))

def intensity():
    adc_read=[]
    for i in range(10):
        adc_read.append(lSens.read())
    adc_read = sorted(adc_read)
    intens= adc_read[4]
    return intens

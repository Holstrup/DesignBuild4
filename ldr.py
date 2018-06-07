from machine import Pin
from machine import ADC
#lightsensor is  gpio 33
lSens = ADC(Pin(33, Pin.IN))

def intensity():
    adc_read=[]
    for i in range(5):
        adc_read.append(lSens.read())
    intens=sum(adc_read)/5
    return intens


def sensor():
    intensity=lSens.read
    #client.subscribe(topic="abho/feeds/lightIntensity")
    client.publish(topic="abho/feeds/lightIntensity", msg= str(intensity))



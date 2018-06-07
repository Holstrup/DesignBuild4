from machine import Pin
cooler=Pin(13,Pin.OUT)

def coolerHigh():
    cooler.value(0)

def coolerLow():
    cooler.value(1)

import math
import machine
import time
#adcT is port A3 //GPIO 39
adcT= machine.ADC(machine.Pin(32))
T0=298.15
B=3950
#R0 the resistor.
R0=10000
#Steinhart hart
def Temp():
    R=R0/((4095/adcT.read())-1)
    T=(T0*B/(math.log(R/R0)*T0+B))-273.15
    return T

#Should have a function in main, that calls this every x second/minute
def sendTemp():
    temp=Temp()
    try:
        client.publish(topic="abho/feeds/temperature", msg=str(temp))
        print("DONE")
    except Exception as e:
        print("FAILED")

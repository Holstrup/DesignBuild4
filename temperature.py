import math
import board
import analogio
#adcT is port A1
adcT= analogio.AnalogIn(board.A1)
T0=298.15
B=3950
#R0 the resistor.
R0=10000
#Steinhart hart
def Temp():
    R=R0/((4095/adcT.read())-1)
    T=(T0*B/(math.log(R/R0)*T0+B))-273.15
    return T

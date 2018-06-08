#import of files
import time
import utime
from read_temp import getTemp
#import pump
from ldr import intensity
from oled import OLEDMessage
import webUpload
from PID import TempPID
from pidMapping import pidMap


pastError = 0
integralTerm = [0,0,0,0,0,0,0,0,0,0]



def main():
    PIDOut, pastError, currentIntegralTerm = TempPID(0, 0, integralTerm)
    while True:
        time = utime.localtime()[5]
        if time % 30 == 0:
            temp = getTemp()
            inten = intensity()



            PIDOut, pastError, currentIntegralTerm = TempPID(temp,pastError,integralTerm)

            integralTerm.append(currentIntegralTerm)
            integralTerm.pop(0)


            OLEDMessage(temp, inten, PIDOut)
            webUpload.both(temp, inten, PIDOut)


            pidMap(PIDOut)

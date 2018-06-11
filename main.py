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

P = 0.0


pastError = 0
integralTerm = [0,0,0,0,0,0,0,0,0,0]




def main():
    PIDOut, pastError, currentIntegralTerm = TempPID(0, 0, integralTerm)
    while True:
        timed = utime.localtime()[5]
        if timed % 30 == 0:
            temp = getTemp()
            inten = intensity()


            #PID Controls
            PIDOut, pastError, currentIntegralTerm = TempPID(temp,pastError,integralTerm)
            integralTerm.append(pastError)
            integralTerm.pop(0)
            pidMap(PIDOut)

            #Webupload and Oled
            OLEDMessage(temp, inten, PIDOut)
            webUpload.both(temp, inten, PIDOut)

        time.sleep(1)

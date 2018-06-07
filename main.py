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
integralTerm = 0


def main():
    while True:
        time = utime.localtime()[5]
        if time % 5 == 0:
            temp = getTemp()
            inten = intensity()

            OLEDMessage(temp,inten)
            webUpload.both(temp, inten)

            PIDOut, pastError, integralTerm = TempPID(temp,pastError,integralTerm)

            #pidMap(PIDOut)

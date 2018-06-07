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
    PIDOut, pastError, integralTerm = TempPID(0, 0, 0)
    while True:
        time = utime.localtime()[5]
        if time % 30 == 0:
            temp = getTemp()
            inten = intensity()

            PIDOut, pastError, integralTerm = TempPID(temp,pastError,integralTerm)

            OLEDMessage(temp, inten, PIDOut)
            webUpload.both(temp, inten)


            pidMap(PIDOut)

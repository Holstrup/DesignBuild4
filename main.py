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


def main():
    # Target Temperature
    targetTemp = 19
    P = 1
    I = 1
    D = 0.3

    # PID Parameters
    pastError = 0
    integralTerm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]




    #Initial PID measures
    webUpload.targetTempUpload(targetTemp)
    PIDOut, pastError, currentIntegralTerm = TempPID(0, 0, integralTerm, targetTemp, P, I, D)
    webUpload.pidUpload(P, I, D)

    #Setop download
    webUpload.targetTempDownload()
    webUpload.PDownload()
    webUpload.IDownload()

    while True:
        #Each cycle is 30 seconds
        timed = utime.localtime()[5]
        if timed % 30 == 0:
            #Measure
            temp = getTemp()
            inten = intensity()

            #Functions to change P, I, D and targetTemp



            #PID Controls
            PIDOut, pastError, currentIntegralTerm = TempPID(temp,pastError,integralTerm, targetTemp, P, I, D)
            integralTerm.append(pastError)
            integralTerm.pop(0)
            pwmpump, cooler = pidMap(PIDOut)


            #Webupload and Oled
            OLEDMessage(temp, inten, PIDOut, pwmpump, cooler)
            webUpload.both(temp, inten, PIDOut, pwmpump, cooler)

        elif timed % 15 == 0:
            print("Starting Downloads... \n")

            try:
                targetTemp = webUpload.targetTempDownload2()
                P = webUpload.PDownload2()
                I = webUpload.IDownload2()
            except OSError:
                print("Error")

            print("Current target temperature is: " + str(targetTemp))
            print("Current P is: " + str(P))
            print("Current I is: " + str(I))
            print("\n")

        time.sleep(1)

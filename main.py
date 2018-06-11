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

    #Setup download
    webUpload.targetTempDownload()
    webUpload.PDownload()
    webUpload.IDownload()
    webUpload.DDownload()

    while True:
        #Each cycle is 30 seconds
        timed = utime.localtime()[5]
        if timed % 30 == 0:
            #Measure
            temp = getTemp()
            inten = intensity()

            #PID Controls
            PIDOut, pastError, currentIntegralTerm = TempPID(temp,pastError,integralTerm, targetTemp, P, I, D)
            integralTerm.append(pastError)
            integralTerm.pop(0)
            pwmpump, cooler = pidMap(PIDOut)


            try:
                # Webupload and Oled
                OLEDMessage(temp, inten, PIDOut, pwmpump, cooler)
                webUpload.both(temp, inten, PIDOut, pwmpump, cooler)
            except OSError:
                print("PID Upload Error")


        elif timed % 15 == 0:
            print("Starting Downloads... \n")

            try:
                targetTemp = webUpload.targetTempDownload2()
                P = webUpload.PDownload2()
                I = webUpload.IDownload2()
                D = webUpload.DDownload2()
            except OSError:
                print("Error")

            print("Current target temperature is: " + str(targetTemp))
            print("Current P is: " + str(P))
            print("Current I is: " + str(I))
            print("Current D is: " + str(D))
            print("\n")

        time.sleep(1)

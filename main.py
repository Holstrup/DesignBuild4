#import of files
import time
import utime
from read_temp import getTemp
import pump
from ldr import intensity
from oled import OLEDMessage
import webUpload
from PID import TempPID, odpid
from pidMapping import pidMap, pidMapOD



def main():
    # Target Temperature
    targetTemp = 18.0
    #Target intentensity:
    targetInten=600
    pumpBack=0
    pumpTime=0


    P = 2.0
    I = 1.0
    D = 2.0

    # PID Parameters
    pastError = 0
    integralTerm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    integralTermOd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]




    #Initial PID measures
    webUpload.targetTempUpload(targetTemp)
    PIDOut, pastError= TempPID(0, 0, integralTerm, targetTemp, P, I, D)
    PIDOutOd, pastErrorOd= odpid(0, 0, integralTermOd, targetInten, P, I, D)
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


            #PID Controls
            PIDOut, pastError = TempPID(temp,pastError,integralTerm, targetTemp, P, I, D)
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
           targetTemp, P, I, D = webUpload.downloads()


        if utime.localtime()[4] % 4 == 0 and timed == 20:
            webUpload.refresh(P, I, D)


        if timed % 12 == 0:
            print("pumptime: %s" % pumpTime)
            if pumpTime < 12:
                if pumpBack == 0:
                    inten = intensity()
                    PIDOutOd, pastErrorOd = odpid(inten, pastErrorOd, integralTermOd, targetInten, P, I, D)
                    integralTermOd.append(pastErrorOd)
                    integralTermOd.pop(0)
                    pumpTime = pidMapOD(PIDOut)
                    print("New pumptime: %s" % pumpTime)
                    if pumpTime==0:
                        pump.off()
                    else:
                        pump.forward()
                        pumpBack+=1
                        pumpTime-=12

                else:
                    pump.backwards()

                    pumpBack -= 1

                    print("going back x%s" % pumpBack)
            else:
                pumpTime -= 12
                pumpBack += 1
                print("pumpback: %s" % pumpBack)


        time.sleep(1)

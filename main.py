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




def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Internet_of_Mussels', 'Feather_HUZZAH32')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def main():
    # Target Temperature
    targetTemp = 19
    #Target intentensity:
    targetInten=600
    pumpBack=0
    pumpTime=0



    P = 1.2
    I = 1
    D = 0.4

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
            print("Starting Downloads... \n")

            try:
                targetTemp = webUpload.targetTempDownload2()
                P = webUpload.PDownload2()
                I = webUpload.IDownload2()
                D = webUpload.DDownload2()

            except OSError:
                print("Error in download")
                break

            print("Current target temperature is: " + str(targetTemp))
            print("Current P is: " + str(P))
            print("Current I is: " + str(I))
            print("Current D is: " + str(D))
            print(utime.localtime())
            print("\n")


        if utime.localtime()[4] % 4 == 0 and timed == 20:
            do_connect()
            print("Refreshing...")
            webUpload.targetTempdisconnect()
            webUpload.PDisconnect()
            webUpload.IDisconnect()
            webUpload.DDisconnect()

            time.sleep(1)
            webUpload.pidUpload(P,I,D)
            time.sleep(1)

            webUpload.targetTempDownload()
            webUpload.PDownload()
            webUpload.IDownload()
            webUpload.DDownload()
            print("Done \n")

        if timed % 12 == 0:
            print("pumptime: %s" % pumpTime)
            if pumpTime < 12:
                if pumpBack == 0:
                    inten = intensity()
                    PIDOutOd, pastErrorOd = odpid(inten, pastErrorOd, integralTermOd, targetInten, P, I, D)
                    integralTermOd.append(pastErrorOd)
                    integralTermOd.pop(0)
                    pumpTime = pidMapOD(PIDOutOd)
                    print("PID OD: %s" % PIDOutOd)
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


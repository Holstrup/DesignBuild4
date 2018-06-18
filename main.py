#import of files
import time
import utime
from read_temp import getTemp
import pump
from led import setLight
from oled import OLEDMessage
import webUpload
from PID import TempPID, odpid
from pidMapping import pidMap, pidMapOD
from ldr import intensity
import os
import sys

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
    setLight(50000,512)
    # Target Temperature
    targetTemp = 19.0

    #Target intentensity:
    pumpState = 0
    pumpTime = 12

    P = 1.2
    I = 1
    D = 0.4

    # PID Parameters
    pastError = 0
    integralTerm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #integralTermOd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    #Initial PID measures
    print("targetTemp: %s " %targetTemp)

    PIDOut, pastError= TempPID(0, 0, integralTerm, targetTemp, P, I, D)

    intenArr = []
    for i in range(100):
        intenArr.append(intensity())

    targetIntensity = (sum(intenArr) / 100)*1.005
    print("Target Intensity: ")
    print(targetIntensity)

    #Setup download
    webUpload.targetTempDownload()
    webUpload.PDownload()
    webUpload.IDownload()
    webUpload.DDownload()

    webUpload.targetTempUpload(targetTemp)

    webUpload.pUpload(P)
    webUpload.iUpload(I)
    webUpload.dUpload(D)


    inten = intensity()

    while True:
        #Each cycle is 30 seconds
        setLight(50000, 512)
        timed = utime.localtime()[5]
        minute = utime.localtime()[4]
        print(utime.localtime())
        if timed % 30 == 0:

            #Measure
            pump.pwm(0)
            setLight(50000, 512)

            time.sleep(0.5)

            inten = intensity()
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
            except Exception as e:
                print("Error: " + str(e))
                print("Pump: " + pwmpump)
                print("Cooler: " + cooler)


        elif timed % 15 == 0:
            print("Starting Downloads... \n")

            try:
                targetTemp = webUpload.targetTempDownload2()
                P = webUpload.PDownload2()
                I = webUpload.IDownload2()
                D = webUpload.DDownload2()

            except OSError as e:
                print(e)
                print("Error in download")

            print("Current target temperature is: " + str(targetTemp))
            print("Current P is: " + str(P))
            print("Current I is: " + str(I))
            print("Current D is: " + str(D))
            print(utime.localtime())
            print("\n")


        if utime.localtime()[4] % 4 == 0 and timed == 20:
            try:
                do_connect()
                print("Refreshing...")
                webUpload.targetTempdisconnect()
                webUpload.PDisconnect()
                webUpload.IDisconnect()
                webUpload.DDisconnect()

                time.sleep(1)

                webUpload.targetTempDownload()
                webUpload.PDownload()
                webUpload.IDownload()
                webUpload.DDownload()

                time.sleep(1)


                webUpload.pUpload(P)
                webUpload.iUpload(I)
                webUpload.dUpload(D)

                print("Done \n")
            except Exception as e:
                print(e)
                print("Refreshing Error")


        if inten > targetIntensity and pumpState == 0 and timed == pumpTime:
            print("Transfering water from algae to mussels")
            pump.forwards()
            pumpState = 1
        elif pumpState == 1 and timed == pumpTime:
            print("Algae pump off")
            pump.off()
            pumpState = 2
        elif pumpState == 2 and timed == pumpTime:
            print("Transfering water from mussels to algae")
            pump.backwards()
            pumpState = 3
        elif pumpState == 3 and timed == pumpTime:
            print("Algae pump off")
            pump.off()
            pumpState = 0

        time.sleep(1)
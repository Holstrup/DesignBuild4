#import of files
import time
from read_temp import getTemp
#import pump
from ldr import intensity
from oled import OLEDMessage
import webUpload



def main():
    while True:
        temp = getTemp()
        inten = intensity()

        OLEDMessage(temp,inten)

        webUpload.temperature(temp)
        #webUpload.intensityUpload(inten)


        time.sleep(5)



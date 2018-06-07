#import of files
import time
from read_temp import getTemp
import pump as pump
from ldr import intensity
from oled import  OLEDMessage





while True:
    OLEDMessage(getTemp(),intensity())
    time.sleep(5)

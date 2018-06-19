import pump
import cooler
import time


def pidMap(pid):
    if pid <= -10:
        pump.pwm(100)

        cooler.coolerHigh()
        return "100","High"
    
    elif pid <= -8:
        pump.pwm(80)
        cooler.coolerHigh()
        return "100", "High"
     
    elif pid <= -6:
        pump.pwm(100)
        cooler.coolerLow()
        return "100", "Low"

    elif pid <= -4:
        pump.pwm(60)
        cooler.coolerLow()
        return "60", "Low"
      
    elif pid <= -2:
        pump.pwm(50)
        cooler.coolerLow()
        return "40", "Low"
       
    else:
        pump.pwm(0)
        cooler.coolerLow()
        return "0", "Low"

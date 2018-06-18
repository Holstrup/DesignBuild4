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


def pidMapOD(pid):
    #time that it takes water to run through.. can vary
    defaultTime=12
    if pid <= -10:
        return (defaultTime+48)

    elif pid <= -8:
        return (defaultTime + 36)



    elif pid <= -6:
        return (defaultTime + 24)

    elif pid <= -4:
        return (defaultTime + 12)

    else:
        return (0)
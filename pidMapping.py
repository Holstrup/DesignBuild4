import pump
import cooler

def pidMap(pid):
    if pid <= -10:
        #PWM
        cooler.coolerHigh()
    elif pid <= -8:
        # PWM
        cooler.coolerHigh()
    elif pid <= -6:
        # PWM
        cooler.coolerLow()
    elif pid <= -4:
        # PWM
        cooler.coolerLow()
    elif pid <= -2:
        # PWM
        cooler.coolerLow()
    else:
        # Off
        cooler.coolerLow()

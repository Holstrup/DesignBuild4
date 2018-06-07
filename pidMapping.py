import pump
import cooler

def pidMap(pid):
    if pid <= -10:
        pump.pwm(100)
        cooler.coolerHigh()
    elif pid <= -8:
        pump.pwm(80)
        cooler.coolerHigh()
    elif pid <= -6:
        pump.pwm(100)
        cooler.coolerLow()
    elif pid <= -4:
        pump.pwm(60)
        cooler.coolerLow()
    elif pid <= -2:
        pump.pwm(40)
        cooler.coolerLow()
    else:
        pump.pwm(0)
        cooler.coolerLow()

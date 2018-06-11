import pump
import cooler
import oled

def pidMap(pid):
    if pid <= -10:
        pump.pwm(100)
        cooler.coolerHigh()
        return ("100%","High")
        #oled.status_pump_cooler("100%","On")
    elif pid <= -8:
        pump.pwm(80)
        cooler.coolerHigh()
        return ("100%", "High")
        #oled.status_pump_cooler("80%", "On")
    elif pid <= -6:
        pump.pwm(100)
        cooler.coolerLow()
        return ("100%", "Off")
        #oled.status_pump_cooler("100%", "Off")
    elif pid <= -4:
        pump.pwm(60)
        cooler.coolerLow()
        return ("60%", "Off")
        #oled.status_pump_cooler("60%", "Off")
    elif pid <= -2:
        pump.pwm(40)
        cooler.coolerLow()
        return ("40%", "Off")
       # oled.status_pump_cooler("40%", "Off")
    else:
        pump.pwm(0)
        cooler.coolerLow()
        return ("0%", "Off")
        #oled.status_pump_cooler("0%", "Off")

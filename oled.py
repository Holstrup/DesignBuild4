import sys
import  machine
sys.path.insert(0, '/lib')
import ssd1306



def status_pump_cooler(pwmpump,cooler):
    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    pumpCoolText = ("cool pump: %s" % pwmpump)
    coolText=("cooler: %s" % cooler)
    display.text(pumpCoolText, 0, 30)
    display.text(coolText, 0, 40)
    display.show()

def algiepump(pump):
    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    pumpstatus=("algie pump: %s" %pump)
    display.text(pumpstatus, 0, 50)
    display.show()

def OLEDMessage(temperature, intensity, pidVal,pwmpump,cooler):
    i2c = machine.I2C(scl = machine.Pin(22), sda = machine.Pin(23))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    tempText = "Temp is: "
    odText = "OD is: "
    pidText = "PID is: "
    pumpCoolText = ("cool pump: %s" % pwmpump)
    coolText = ("cooler: %s" % cooler)
    display.text(pumpCoolText, 0, 30)
    display.text(coolText, 0, 40)
    display.text(tempText + str(temperature), 0, 0)
    display.text(odText + str(intensity), 0, 10)
    display.text(pidText + str(pidVal), 0, 20)
    display.text(" ", 0, 30)
    display.show()




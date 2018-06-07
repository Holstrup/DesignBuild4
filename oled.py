import sys
import  machine
sys.path.insert(0, '/lib')
import ssd1306



def OLEDMessage(temperature, intensity):
    i2c = machine.I2C(scl = machine.Pin(22), sda = machine.Pin(23))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    tempText = "Temp is: "
    odText = "OD is: "
    display.text(tempText + str(temperature), 0, 0)
    display.text(odText + str(intensity), 0, 10)
    display.show()

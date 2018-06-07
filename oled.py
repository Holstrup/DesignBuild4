import sys
sys.path.insert(0, '/lib')
import ssd1306

def OLEDMessage(message):
    i2c = machine.I2C(scl = machine.Pin(22), sda = machine.Pin(23))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.text(str(message), 0, 0)
    display.show()

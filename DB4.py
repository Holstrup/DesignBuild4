
#/////////////////////  Imports  //////////////////////////////////////////////
import time
import machine
from machine import Pin
from machine import ADC
from machine import DAC
from math import log
import network
#Import MQTT
import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient
import ssd1306
#//////////////////////////////////////////////////////////////////////////////

class Pump:
    """ Point class represents and manipulates x,y coords. """
    
     # constructor
    def __init__(self):
        self.direction = '+'
        self.state = "off"
        self.frequency = 0.0
        self.forward =Pin(14, Pin.OUT)
        self.backward=Pin(32,Pin.OUT)
        
    def set_direction(self,direction):
        self.direction = direction
        if direction == '+':
            self.forward.value(1)
            self.backward.value(0)
        elif direction == '-':
            self.forward.value(0)
            self.backward.value(1)
        
    def get_direction(self):
        return self.direction 
    
    def set_state(self,state):
        self.state = state
        
    def get_state(self):
        return self.state
        
    def set_frequency(self,fq):
        self.frequency = fq
        
    def get_frequency(self):
        return self.frequency 
        
    def move(self):
        while True:
            if self.forward.value()==1:
                self.direction = '+'
            else:
                self.direction = '-'
            time.sleep(2)
        
# /////////////////     Therlistor class   ////////////////////////////
        
class Thermistor: 
    def __init__(self):
        self.resistance = 0
        self.temperature = 0.0
        self.state = "off"
        
    def set_resistance(self,resis):
        self.resistance = resis
        
    def get_resistance(self):
        return self.resistance 
    
    def set_state(self,state):
        self.state = state
        
    def get_state(self):
        return self.state
 
    def get_temperature(self):
        return self.temperature  
        
    def set_temperature(self,tmpr):
        self.temperature = tmpr
        
#/////////////////  Mussel beacker class //////////////////////////        
        
        
class Mussel_beacker:
    def __init__(self):
        self.temperature = 0.0
        self.initial_OD = 0.0
        self.current_OD = 0.0
        self.biomass = 0
        self.max_amonia = 0
        self.filteration_rate = 0.0
        self.feeding_frequency = 0.0
        
    def set_initial_OD(self,in_od):
        self.initial_OD = in_od
        
    def get_initial_OD(self):
        return self.initial_OD
        
    def set_current_OD(self,cur_od):
        self.current_OD = cur_od
        
    def get_current_OD(self):
        return self.current_OD 
        
    def get_biomass(self):
        return self.biomass  
        
    def set_biomass(self,biom):
        self.biomass = biom  
    
    def get_temperature(self):
        return self.temperature  
        
    def set_temperature(self,tmpr):
        self.temperature = tmpr
        
    def get_max_amonia(self):
        return self.max_amonia  
        
    def set_max_amonia(self,max_am):
        self.max_amonia = max_am
        
    def get_filteration_rate(self):
        return self.filteration_rate  
        
    def set_filteration_rate(self,fil_rate):
        self.filteration_rate = fil_rate   
   
#//////////////////// Algae beacker class  ////////////////////////////     
        
class Algae_beacker:
    def __init__(self):
        self.temperature = 0.0
        self.initial_OD = 0.0
        self.current_OD = 0.0
        self.biomass = 0
        self.max_amonia = 0
        self.filteration_rate = 0.0
        self.feeding_frequency = 0.0
        
    def set_initial_OD(self,in_od):
        self.initial_OD = in_od
        
    def get_initial_OD(self):
        return self.initial_OD
        
    def set_current_OD(self,cur_od):
        self.current_OD = cur_od
        
    def get_current_OD(self):
        return self.current_OD 
        
    def get_biomass(self):
        return self.biomass  
        
    def set_biomass(self,biom):
        self.biomass = biom  
    
    def get_temperature(self):
        return self.temperature  
        
    def set_temperature(self,tmpr):
        self.temperature = tmpr
        
    def get_max_amonia(self):
        return self.max_amonia  
        
    def set_max_amonia(self,max_am):
        self.max_amonia = max_am
        
    def get_filteration_rate(self):
        return self.filteration_rate  
        
    def set_filteration_rate(self,fil_rate):
        self.filteration_rate = fil_rate        

#*///////////////////////////////    Diode class /////////////////
        
class Diode:
    
    def __init__(self):
        self.state = "off"
        self.pwm  = 0.0
        self.pin = Pin(12, Pin.OUT)
        
    def set_state(self , state):
        self.state = state
        if state == "off":
            self.pin.value(0)
        elif state == "on":
            self.pin.value(1)
        
    def get_state(self):
        return self.state
        
    def set_pwm(self,pwm):
        self.frequency = pwm
        
    def get_pwm(self):
        return self.pwm 
        
#////////////////////  Light sensor  //////////////////////////////////////////////

class LightSensor:
    
    def __init__(self):
        self.state = "off"
        self.pin = machine.ADC(machine.Pin(26))
        self.intensity = self.pin.read()
        
    def set_state(self , state):
        self.state = state
        
    def get_state(self):
        return self.state
    
    def server_send(self):
        self.client.publish(topic="abho/feeds/lightIntensity", msg= str(self.intensity))
        
class Cooler:
    
    def __init__(self):
        self.state = "off"
        self.pin = Pin(13,Pin.OUT)
        self.intensity = self.pin.read()
        
    def set_state(self , state):
        self.state = state
        if state == "on":
            self.pin.value(1)
        elif state == "off":
            self.pin.value(0)
        else:
            print("invalid value")
            
        
    def get_state(self):
        return self.state
    
        
    def sub_cb(self,topic, msg):          # sub_cb means "callback subroutine"
        print((topic, msg))          # Outputs the message that was received. Debugging use.
        if msg == b"ON":             # If message says "ON" ...
            self.pin.value(1)       # ... turns on 5V
        elif msg == b"OFF":          # If message says "OFF" ...
            self.pin.value(0)           # ... turns on 12V
        else:                        # If any other message is received ...
            print("Unknown message") # ... do nothing but output that it happened.
        
        # Subscribed messages will be delivered to this callback
        self.client.set_callback(self.sub_cb())
        self.client.subscribe(topic="abho/feeds/cool")
        self.client.check_msg()    
        
#///////////////////////////////    ///  Main code   //////////////////////////////        
#CallBack Message
def sub_cb(topic, msg):
    print(msg)

#IsConnected
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Internet_of_Mussels', 'Feather_HUZZAH32')
        while not sta_if.isconnected():
            pass
        print('network config:', sta_if.ifconfig())

#Publish value
client = MQTTClient("device_id", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
client.set_callback(sub_cb)


def temperature(Temperature):
    client.connect()
    client.subscribe(topic="abho/feeds/Temperature")
    client.publish(topic="abho/feeds/Temperature", msg= str(Temperature))
    client.disconnect()



def getPParameter():
    client.connect()
    client.subscribe(topic="abho/feeds/PParameter")
    p = client.check_msg()
    client.disconnect()
    return p


def getIParameter():
    client.connect()
    client.subscribe(topic="abho/feeds/IParameter")
    i = client.check_msg()
    client.disconnect()
    return i


def getDParameter():
    client.connect()
    client.subscribe(topic="abho/feeds/DParameter")
    d = client.check_msg()
    client.disconnect()
    return d


def OLEDMessage(message):
    i2c = machine.I2C(scl = machine.Pin(22), sda = machine.Pin(23))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.text(str(message), 0, 0)
    display.show()



def lightSensor():
    adc = ADC(Pin(34, Pin.IN))
    return adc.read()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
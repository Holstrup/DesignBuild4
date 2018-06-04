#Basic Imports
import network

#Import MQTT
import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient


#CallBack Message
def sub_cb(topic, msg):
    print(msg)

#IsConnected
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Weidekampsgade 37 5 tv', 'CPHPAATOPPEN')
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



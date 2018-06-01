import network
from mqtt import MQTTClient
import machine
import time

def sub_cb(topic, msg):
    print(msg)

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(True)
sta_if.connect('Internet_of_Mussels', 'Feather_HUZZAH32')
#wlan = WLAN(mode=WLAN.STA)
#wlan.connect("Internet_of_Mussels", auth=(WLAN.WPA2, "Feather_HUZZAH32"), timeout=5000)

#while not wlan.isconnected():
#    machine.idle()
print("Connected to Wifi\n")

client = MQTTClient(client_id="example_client", server="io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="abho/feeds/lights")
while True:
    print("Sending ON")
    client.publish(topic="abho/feeds/lights", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="abho/feeds/lights", msg="OFF")
    
    time.sleep(1)

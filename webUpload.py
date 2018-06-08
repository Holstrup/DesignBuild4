import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient

def sub_cb(topic,msg):
    print(msg)

#Publish value
client = MQTTClient("device_id", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
client.set_callback(sub_cb)


def temperature(Temperature):
    client.connect()
    client.subscribe(topic="abho/feeds/Temperature")
    client.publish(topic="abho/feeds/Temperature", msg= str(Temperature))
    client.disconnect()

def intensityUpload(intensity):
    client.connect()
    client.subscribe(topic="abho/feeds/lightIntensity")
    client.publish(topic="abho/feeds/lightIntensity", msg= str(intensity))
    client.disconnect()
    
def both(Temperature,intensity,pid):
    client.connect()
    client.subscribe(topic="abho/feeds/Temperature")
    client.publish(topic="abho/feeds/Temperature", msg= str(Temperature))
    client.subscribe(topic="abho/feeds/lightIntensity")
    client.publish(topic="abho/feeds/lightIntensity", msg=str(intensity))
    client.subscribe(topic="abho/feeds/pid")
    client.publish(topic="abho/feeds/pid", msg= str(pid))
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

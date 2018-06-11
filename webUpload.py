import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient
import time

P = 0.0
I = 0.0


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
    
def both(Temperature,intensity,pid,pwmpump,cooler):
    client.connect()
    client.subscribe(topic="abho/feeds/Temperature")
    client.publish(topic="abho/feeds/Temperature", msg= str(Temperature))
    client.subscribe(topic="abho/feeds/lightIntensity")
    client.publish(topic="abho/feeds/lightIntensity", msg=str(intensity))
    client.subscribe(topic="abho/feeds/pid")
    client.publish(topic="abho/feeds/pid", msg= str(pid))
    client.subscribe(topic="abho/feeds/cooler-pump")
    client.publish(topic="abho/feeds/cooler-pump", msg= pwmpump)
    client.subscribe(topic="abho/feeds/cooler")
    client.publish(topic="abho/feeds/cooler", msg= cooler)
    client.disconnect()


def PCallBack(topic,msg):
    print("Here")
    global P
    P = float(msg.decode("utf-8"))


pclient = MQTTClient("device_id", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
pclient.set_callback(PCallBack)


def getP():
    pclient.connect()
    pclient.subscribe(topic="abho/feeds/PParameter")

def getPParameter():
    pclient.check_msg()
    return P



def ICallBack(topic,msg):
    print("Here")
    global I
    I = float(msg.decode("utf-8"))

Iclient = MQTTClient("device_id", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
Iclient.set_callback(ICallBack)

def getI():
    Iclient.connect()
    Iclient.subscribe(topic="abho/feeds/IParameter")

def getIParameter():
    Iclient.check_msg()
    return I

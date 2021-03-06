import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient
import time


Usr = "abho"
AIOKey = "bbd0c066695243c2b7d30dbc94614a94"



P = 1.0
i = 1.0
D = 0.3
targetTemp = 19.0


def sub_cb(topic,msg):
    print("Data " + msg.decode("utf-8") + " uploaded")

#Publish value
client = MQTTClient("device_id", "io.adafruit.com", user=Usr, password=AIOKey, port=1883)
client.set_callback(sub_cb)



def both(Temperature,intensity,PIDVal,pwmpump,cooler):
    client.connect()
    client.subscribe(topic=Usr + "/feeds/Temperature")
    client.publish(topic=Usr + "/feeds/Temperature", msg= str(Temperature))
    client.subscribe(topic=Usr + "/feeds/lightintensity")
    client.publish(topic=Usr + "/feeds/lightIntensity", msg=str(intensity))
    client.subscribe(topic=Usr + "/feeds/pid")
    client.publish(topic=Usr + "/feeds/pid", msg= str(PIDVal))
    client.subscribe(topic=Usr + "/feeds/cooler-pump")
    client.publish(topic=Usr + "/feeds/cooler-pump", msg= pwmpump)
    client.subscribe(topic=Usr + "/feeds/cooler")
    client.publish(topic=Usr + "/feeds/cooler", msg= cooler)
    client.disconnect()



#Target Temp
def targetTempUpload(temp):
    client.connect()
    client.subscribe(topic=Usr + "/feeds/targettemp")
    client.publish(topic=Usr + "/feeds/targettemp", msg=str(temp))
    client.disconnect()

def targetTempUpload2(temp):
    client.publish(topic=Usr + "/feeds/targettemp", msg=str(temp))


def targetTempCallBack(topic,msg):
    print("Change in target temp registered")
    global targetTemp
    targetTemp = float(msg.decode("utf-8"))

tempClient = MQTTClient("ESP32", "io.adafruit.com", user=Usr, password=AIOKey, port=1883)
tempClient.set_callback(targetTempCallBack)

def targetTempDownload():
    tempClient.connect()
    tempClient.subscribe(topic=Usr + "/feeds/targettemp")
    return targetTemp

def targetTempDownload2():
    tempClient.check_msg()
    return targetTemp

def targetTempdisconnect():
    tempClient.disconnect()



#P Parameter
def PCallBack(topic,msg):
    print("Change in P registered")
    global P
    P = float(msg.decode("utf-8"))

pclient = MQTTClient("PValue", "io.adafruit.com", user=Usr, password=AIOKey, port=1883)
pclient.set_callback(PCallBack)

def PDownload():
    pclient.connect()
    pclient.subscribe(topic=Usr + "/feeds/pparameter")
    return P

def PDownload2():
    pclient.check_msg()
    return P

def PDisconnect():
    pclient.disconnect()



#I Parameter
def ICallBack(topic,msg):
    print("Change in I registered")
    global i
    i = float(msg.decode("utf-8"))

iclient = MQTTClient("IValue", "io.adafruit.com", user=Usr, password=AIOKey, port=1883)
iclient.set_callback(ICallBack)

def IDownload():
    iclient.connect()
    iclient.subscribe(topic=Usr + "/feeds/iparameter")
    return i

def IDownload2():
    iclient.check_msg()
    return i


def IDisconnect():
    iclient.disconnect()


#D Parameter
def DCallBack(topic,msg):
    print("Change in D registered")
    global D
    D = float(msg.decode("utf-8"))

dclient = MQTTClient("DValue", "io.adafruit.com", user=Usr, password=AIOKey, port=1883)
dclient.set_callback(DCallBack)

def DDownload():
    dclient.connect()
    dclient.subscribe(topic=Usr + "/feeds/dparameter")
    return D

def DDownload2():
    dclient.check_msg()
    return D


def DDisconnect():
    dclient.disconnect()


#PID Upload

def pUpload(Ppara):
    pclient.subscribe(topic=Usr + "/feeds/pparameter")
    pclient.publish(topic=Usr + "/feeds/pparameter", msg=str(Ppara))


def iUpload(Ipara):
    iclient.subscribe(topic=Usr + "/feeds/iparameter")
    iclient.publish(topic=Usr + "/feeds/iparameter", msg=str(Ipara))

def dUpload(Dpara):
    dclient.subscribe(topic=Usr + "/feeds/dparameter")
    dclient.publish(topic=Usr + "/feeds/dparameter", msg=str(Dpara))
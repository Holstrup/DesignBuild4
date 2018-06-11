import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient
import time

P = 1.0
i = 1.0
D = 0.3
targetTemp = 19.0


def sub_cb(topic,msg):
    print("Data " + msg.decode("utf-8") + " uploaded")

#Publish value
client = MQTTClient("device_id", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
client.set_callback(sub_cb)


def both(Temperature,intensity,pid,pwmpump,cooler):
    client.connect()
    client.subscribe(topic="abho/feeds/Temperature")
    client.publish(topic="abho/feeds/Temperature", msg= str(Temperature))
    client.subscribe(topic="abho/feeds/lightintensity")
    client.publish(topic="abho/feeds/lightIntensity", msg=str(intensity))
    client.subscribe(topic="abho/feeds/pid")
    client.publish(topic="abho/feeds/pid", msg= str(pid))
    client.subscribe(topic="abho/feeds/cooler-pump")
    client.publish(topic="abho/feeds/cooler-pump", msg= pwmpump)
    client.subscribe(topic="abho/feeds/cooler")
    client.publish(topic="abho/feeds/cooler", msg= cooler)
    client.disconnect()



#Target Temp
def targetTempUpload(targetTemp):
    client.connect()
    client.subscribe(topic="abho/feeds/targettemp")
    client.publish(topic="abho/feeds/targettemp", msg=str(targetTemp))
    client.disconnect


def targetTempCallBack(topic,msg):
    print("Change in target temp registered")
    global targetTemp
    targetTemp = float(msg.decode("utf-8"))

tempClient = MQTTClient("ESP32", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
tempClient.set_callback(targetTempCallBack)

def targetTempDownload():
    tempClient.connect()
    tempClient.subscribe(topic="abho/feeds/targettemp")
    return targetTemp

def targetTempDownload2():
    tempClient.check_msg()
    return targetTemp



#P Parameter
def PCallBack(topic,msg):
    print("Change in P registered")
    global P
    P = float(msg.decode("utf-8"))

pclient = MQTTClient("PValue", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
pclient.set_callback(PCallBack)

def PDownload():
    pclient.connect()
    pclient.subscribe(topic="abho/feeds/pparameter")
    return P

def PDownload2():
    pclient.check_msg()
    return P



#I Parameter
def ICallBack(topic,msg):
    print("Change in I registered")
    global i
    i = float(msg.decode("utf-8"))

iclient = MQTTClient("IValue", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
iclient.set_callback(ICallBack)

def IDownload():
    iclient.connect()
    iclient.subscribe(topic="abho/feeds/iparameter")
    return i

def IDownload2():
    iclient.check_msg()
    return i


#D Parameter
def DCallBack(topic,msg):
    print("Change in D registered")
    global D
    D = float(msg.decode("utf-8"))

dclient = MQTTClient("DValue", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
dclient.set_callback(DCallBack)

def DDownload():
    dclient.connect()
    dclient.subscribe(topic="abho/feeds/dparameter")
    return D

def DDownload2():
    dclient.check_msg()
    return D



#PID Upload
def pidUpload(P,i,D):
    client.connect()

    client.subscribe(topic="abho/feeds/pparameter")
    client.publish(topic="abho/feeds/pparameter", msg=str(P))

    client.subscribe(topic="abho/feeds/dparameter")
    client.publish(topic="abho/feeds/dparameter", msg=str(D))

    client.subscribe(topic="abho/feeds/iparameter")
    client.publish(topic="abho/feeds/iparameter", msg=str(i))

    client.disconnect



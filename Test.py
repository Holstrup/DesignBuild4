import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient
import time

P = 1.0
i = 1.0
D = 0.3
targetTemp = 19.0



def targetTempCallBack(topic,msg):
    print("Change in target temperature registered")
    global targetTemp
    targetTemp = float(msg.decode("utf-8"))

tempClient = MQTTClient("TargetTemp", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
tempClient.set_callback(targetTempCallBack)
tempClient.connect()
tempClient.subscribe(topic="abho/feeds/targettemp")


def targetTempDownload():
    tempClient.check_msg()
    return targetTemp





#P Parameter
def PCallBack(topic,msg):
    print("Change in P registered")
    global P
    P = float(msg.decode("utf-8"))

pclient = MQTTClient("PValue", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
pclient.set_callback(PCallBack)
pclient.connect()
pclient.subscribe(topic="abho/feeds/pparameter")


def PDownload():
    pclient.check_msg()
    return P

def PUpload():
    pclient.publish(topic="abho/feeds/pparameter", msg=str(P))





#I Parameter
def ICallBack(topic,msg):
    print("Change in I registered")
    global i
    i = float(msg.decode("utf-8"))

iclient = MQTTClient("IValue", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
iclient.set_callback(ICallBack)
iclient.connect()
iclient.subscribe(topic="abho/feeds/iparameter")


def IDownload():
    iclient.check_msg()
    return i

def IUpload():
    iclient.publish(topic="abho/feeds/iparameter", msg=str(i))




#D Parameter
def DCallBack(topic,msg):
    print("Change in D registered")
    global D
    D = float(msg.decode("utf-8"))

dclient = MQTTClient("DValue", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
dclient.set_callback(DCallBack)
dclient.connect()
dclient.subscribe(topic="abho/feeds/dparameter")


def DDownload():
    dclient.check_msg()
    return D


def DUpload():
    dclient.publish(topic="abho/feeds/dparameter", msg=str(D))

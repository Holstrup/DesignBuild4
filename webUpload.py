import sys
sys.path.insert(0, '/lib')
from simple import MQTTClient
import time

Usr = "abho"
UsrFeed = Usr + "/feeds"
AIOKey = "bbd0c066695243c2b7d30dbc94614a94"
portNo = 1883

P = 2.0
i = 1.0
D = 2.0
targetTemp = 18.0

#Callback Functions

def clientCallBack(topic, msg):
    print("Data " + msg.decode("utf-8") + " uploaded")


def targetTempCallBack(topic,msg):
    print("Change in target temp registered")
    global targetTemp
    targetTemp = float(msg.decode("utf-8"))

def PCallBack(topic,msg):
    print("Change in P registered")
    global P
    P = float(msg.decode("utf-8"))

def ICallBack(topic,msg):
    print("Change in I registered")
    global i
    i = float(msg.decode("utf-8"))

def DCallBack(topic,msg):
    print("Change in D registered")
    global D
    D = float(msg.decode("utf-8"))


#Clients used
client = MQTTClient("MainClient", "io.adafruit.com", user = Usr, password= AIOKey, port=portNo)
client.set_callback(clientCallBack)

tempClient = MQTTClient("ESP32", "io.adafruit.com", user = Usr, password= AIOKey, port=portNo)
tempClient.set_callback(targetTempCallBack)

pclient = MQTTClient("PValue", "io.adafruit.com", user = Usr, password=AIOKey, port=portNo)
pclient.set_callback(PCallBack)

iclient = MQTTClient("IValue", "io.adafruit.com", user = Usr, password=AIOKey, port=portNo)
iclient.set_callback(ICallBack)

dclient = MQTTClient("DValue", "io.adafruit.com", user = Usr, password=AIOKey, port=portNo)
dclient.set_callback(DCallBack)

def both(Temperature,intensity,pid,pwmpump,cooler):
    client.connect()
    client.subscribe(topic= UsrFeed + "/Temperature")
    client.publish(topic= UsrFeed   + "/Temperature", msg= str(Temperature))
    client.subscribe(topic= UsrFeed + "/lightintensity")
    client.publish(topic= UsrFeed   + "/lightIntensity", msg=str(intensity))
    client.subscribe(topic= UsrFeed + "/pid")
    client.publish(topic= UsrFeed   + "/pid", msg= str(pid))
    client.subscribe(topic= UsrFeed + "/cooler-pump")
    client.publish(topic= UsrFeed   + "/cooler-pump", msg= pwmpump)
    client.subscribe(topic= UsrFeed + "/cooler")
    client.publish(topic= UsrFeed   + "/cooler", msg= cooler)
    client.disconnect()


#Target Temp
def targetTempUpload(targetTemp):
    client.connect()
    client.subscribe(topic= UsrFeed + "/targettemp")
    client.publish(topic= UsrFeed   + "/targettemp", msg=str(targetTemp))
    client.disconnect


def targetTempDownload():
    tempClient.connect()
    tempClient.subscribe(topic= UsrFeed + "/targettemp")
    return targetTemp

def targetTempDownload2():
    tempClient.check_msg()
    return targetTemp

#PID Upload
def pidUpload(P,i,D):
    client.connect()

    client.subscribe(topic=UsrFeed + "/pparameter")
    client.publish(topic= UsrFeed   + "/pparameter", msg=str(P))

    client.subscribe(topic=UsrFeed + "/iparameter")
    client.publish(topic=UsrFeed + "/iparameter", msg=str(i))

    client.subscribe(topic= UsrFeed + "/dparameter")
    client.publish(topic= UsrFeed   + "/dparameter", msg=str(D))

    client.disconnect


#P Parameter
def PDownload():
    pclient.connect()
    pclient.subscribe(topic= UsrFeed + "/pparameter")
    return P

def PDownload2():
    pclient.check_msg()
    return P

#I Parameter
def IDownload():
    iclient.connect()
    iclient.subscribe(topic= UsrFeed + "/iparameter")
    return i

def IDownload2():
    iclient.check_msg()
    return i


#D Parameter
def DDownload():
    dclient.connect()
    dclient.subscribe(topic= UsrFeed + "/dparameter")
    return D

def DDownload2():
    dclient.check_msg()
    return D



def refresh(P, I, D):
    print("Refreshing...")
    disconnect(client)
    disconnect(pclient)
    disconnect(iclient)
    disconnect(dclient)

    time.sleep(1)
    pidUpload(P, I, D)
    time.sleep(1)

    targetTempDownload()
    PDownload()
    IDownload()
    DDownload()
    print("Done \n")


def disconnect(MqttClient):
    MqttClient.disconnect()


def downloads():
    print("Starting Downloads... \n")
    try:
        targetTemp = targetTempDownload2()
        P = PDownload2()
        I = IDownload2()
        D = DDownload2()

        return targetTemp, P, I, D
    except OSError:
        print("Error in download \n")


import time
import machine
from simple import MQTTClient



def sub_cb(topic, msg):
        value = float(str(msg,'utf-8'))
        print("subscribed value = {}".format(value))
        return value

#
# connect ESP to Adafruit IO using MQTT
#client = MQTTClient("device_id", "io.adafruit.com", user="abho", password="bbd0c066695243c2b7d30dbc94614a94", port=1883)
myMqttClient = "device_id"  # replace with your own client name
adafruitUsername = "abho"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "bbd0c066695243c2b7d30dbc94614a94"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
adafruitFeed = adafruitUsername + "/feeds/pparameter" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.set_callback(sub_cb)
c.connect()
c.subscribe(bytes(adafruitFeed,'utf-8'))


while True:
    c.wait_msg()
    c.check_msg()
    print("waiting...")
    time.sleep(0.5)

c.disconnect()

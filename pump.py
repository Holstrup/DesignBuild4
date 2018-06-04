from machine import Pin
import time
forward =Pin(14, Pin.OUT)
backwards=Pin(32,Pin.Out)





def forward_go():
    backwards.value(0)
    forward.value(1)

def backwards_go():
    forward.value(0)
    backwards.value(1)

while True:
    if forward.value()==1:
        backwards_go()
    else:
        forward_go()
    time.sleep(2)






# Function to respond to messages from Adafruit IO
#def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
 #   print((topic, msg))          # Outputs the message that was received. Debugging use.
  #  if msg == b"ON":             # If message says "ON" ...
   #    driver.value(1)       # ... turns on driver/pump LED on
    #elif msg == b"OFF":          # If message says "OFF" ...
    #    driver.value(0)           # ... turns off driver/pump LED on
    #else:                        # If any other message is received ...
    #    print("Unknown message") # ... do nothing but output that it happened.



# Subscribed messages will be delivered to this callback
#client.set_callback(sub_cb)
#client.subscribe(AIO_CONTROL_FEED)
#client.check_msg()

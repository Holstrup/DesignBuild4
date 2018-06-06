from machine import Pin
cooler=Pin(13,Pin.OUT)

# Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
       cooler.value(1)       # ... turns on 5V
    elif msg == b"OFF":          # If message says "OFF" ...
        cooler.value(0)           # ... turns on 12V
    else:                        # If any other message is received ...
        print("Unknown message") # ... do nothing but output that it happened.



# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.subscribe(topic="abho/feeds/cool")
client.check_msg()

import machine
driver = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

# Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
       driver.value(1)       # ... turns on driver/pump LED on
    elif msg == b"OFF":          # If message says "OFF" ...
        driver.value(0)           # ... turns off driver/pump LED on
    else:                        # If any other message is received ...
        print("Unknown message") # ... do nothing but output that it happened.



# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.subscribe(AIO_CONTROL_FEED)
client.check_msg()

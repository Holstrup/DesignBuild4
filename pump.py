from machine import Pin
import time
forward =Pin(12, Pin.OUT)
backwards=Pin(27,Pin.OUT)





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


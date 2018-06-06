import machine
#lightsensor is port A0 gpio 26
lSens = machine.ADC(machine.Pin(26))





def sensor():
    intensity=lSens.read
    #client.subscribe(topic="abho/feeds/lightIntensity")
    client.publish(topic="abho/feeds/lightIntensity", msg= str(intensity))



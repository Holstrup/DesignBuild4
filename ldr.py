import analogio
#lightsensor is port A0
lSens= analogio.AnalogIn(board.A0)


def sensor():
    client.connect()
    intensity=lSens.read
    client.subscribe(topic="abho/feeds/lightIntensity")
    client.publish(topic="abho/feeds/lightIntensity", msg= str(intensity))



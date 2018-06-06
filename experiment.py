from read_temp import getTemp
import time
#from pump import backwards_go


#cooler(0)

i = 0
temparr = []
while i < 300:
    temp = getTemp()
    temparr.append(str(temp))
    i += 5
    time.sleep(5)


file = open('tempreadings.txt', 'w')
for item in temparr:
    file.write("%s," % item)
file.close()

import smbus
import time
import math
address = 0x48
AIN1 = 0x41
bus = smbus.SMBus(1)

try : 
    while True:
        bus.write_byte(address, AIN1)
        value = bus.read_byte(address)
        print("value: {0}".format(value))
        voltage = value / 255 * 3.3
        Rt = 10* voltage / (3.3 - voltage)
        tempK = 1/(1/(273.15 +25) + math.log(Rt/10)/3950)
        tempC = tempK -273.15
        time.sleep(1)
        print("Temp : ", tempC)
except Exception as e:
    print (e)
    

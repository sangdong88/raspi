import smbus
import time
address = 0x48
AIN0 = 0x40

bus = smbus.SMBus(1)

try : 
    while True:
        bus.write_byte(address, AIN0)
        value = bus.read_byte(address)
        print("value: {0}".format(value))
        time.sleep(1)
except KeyboardInterrupt:
    pass


# 아토 플래닛
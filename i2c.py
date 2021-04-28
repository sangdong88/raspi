import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# check your PCF 8591 address by type in 'sudo i2cdetect -y -l in terminal.

def setup(Addr):
    global address
    address = Addr

def read(chn) : # channel
    try:
        if chn == 0:
            bus.write_byte(address, 0x40)
        if chn == 1:
            bus.write_byte(address, 0x41)
        if chn == 2:
            bus.write_byte(address, 0x42)
        if chn == 3:
            bus.write_byte(address, 0x43)
        return bus.read_byte(address) # dummy read to start conversion

    except Exception as e:
        print("Address : %s" % address)
        print(e)
        return bus.read_byte(address)

def write(val):
    try :
        temp = val # move string value to temp
        temp = int(temp) # change string to integer
        # print temp to see on terminal else comment out
        bus.write_byte_data(address, 0x40,temp)
    except Exception as e:
        print("Error : Device address : 0x%2X" % address)
        print(e)



if __name__ == "__main__" :
    setup(0x48)
    while True :
        print(' ')
        print('AIN0 = ', read(0)) # 조도센서 [Jumper P5 조도센서 CDS 엑세스 회로 선택]
        print('AIN1 = ', read(1)) # 써미스터 온도 [Jumper P4 서미스터 액세스 회로 선택]
        print('AIN2 = ', read(2)) # NONE
        print('AIN3 = ', read(3)) # 가변저항 [Jumper 6 가변저항 액세스 회로 선택]
        print(' ')
        tmp = read(0)
        tmp1 = tmp*(255-125)/255+125 # :LED won't light up below 125, so convert 0-255 to 125-255
        write(tmp1)
        time.sleep(0.5)
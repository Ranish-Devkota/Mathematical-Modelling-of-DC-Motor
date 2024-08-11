import serial
import time

ser =  serial.Serial('COM7',9600,timeout = 1)
time.sleep(2)
data = []
for i in range (100):
    line = ser.readline()
    if line:
        value = line.decode()
        num = value.split(" ")[1]
        num= float(num)
        data.append(num)

ser.close()
for i in range (100):   
    with open(r"F:/Research_self_balancing/data.txt",'w') as fp:
        fp.write("/n".join(str(item) for item in data))
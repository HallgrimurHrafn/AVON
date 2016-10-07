import time
import serial
serialPort = serial.serial("/dev/ttyS0", 9600, timeout=0.5, rtscts=False, dsrdtr=False, xonxoff=False, 
							bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE)
while True:
	serialPort.write("Hello world!")
	time.sleep(1)
	serialPort.flush()
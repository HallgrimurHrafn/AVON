import serial

ser=serial.Serial('/dev/ttyAMA0',31250)
def tm(cmd,note,val):
	msg=chr(cmd)+chr(note)+chr(val)
	ser.write(msg)

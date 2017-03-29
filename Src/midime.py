import serial


ser=serial.Serial('/dev/ttyAMA0',31250)
def tm(144,64,127):
	if note<0:
		note=0
	elif note>127:
		note=127
	msg=chr(cmd)+chr(note)+chr(val)
	print(msg)
	ser.write(msg)

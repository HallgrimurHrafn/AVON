def midime(cmd,note,val):
	ser=serial.Serial('/dev/ttyAMA0',31250)
	msg=chr(cmd)+chr(note)+chr(val)
	ser.write(msg)

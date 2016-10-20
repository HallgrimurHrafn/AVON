#taktmaelir begins
import time
FLASH=1
voice=0


def taktmaelir(dalkur) :
	global FLASH, status, voice						#global breytur, utskyrdar efst.
	for x in range (0,8):							#fyrir oll LED i 'dalkur'
		if status[dalkur][x][voice]==0:				#gert svo vid seum bara ad kveikja a led-um sem var slokkt a fyrir.
			trellis.setLED(x*8+dalkur)				#kveikja a LED!
		#print(x*8+dalkur,tfOut(x*8+dalkur), 'on')
	trellis.writeDisplay() 							#uppfaera led a bordi.. VERDI LJOS!
	time.sleep(FLASH) 								#bidtimi eftir taktmaelis flash.
	for x in range (0,8): 							#fyrir oll LED i 'dalkur'
		if status[dalkur][x][voice]==0: 			#gert svo vid seum bara ad slokkva a led-um sem ekki var kveikt a fyrir "taktmaelir".
			trellis.clrLED(x*8+dalkur) 				#slokkva a LED!
		#print(x*8+dalkur,tfOut(x*8+dalkur), 'off')
	trellis.writeDisplay()							#uppfaera led a bordi.. VERDI MYRKUR!
#taktmaelir end


#tfIn begins 		--- varpar ur trellis i okkar format.
def tfIn (a):
	f=a//16
	d=(a%16)%4
	l=(a%16)//4
	if f%2==0:
		b=16*f+8*l+d
	else:
	#	#b=16*(f+1)-1-(3-l)*8-3+d
		b=16*(f+1)-(3-l)*8+d-4

	#b=16*(f+f%2)+8*l+d -28*(f%2)
	return b
#tfIn ends	



#tfOut begins 		--- varpar ur okkar formati i trellis.
def tfOut (a):
	f=a//16
	d=(a%16)%8
	l=(a%16)//8
	if d<4:
		if f<2:
			b=8*f+4*l+d
		else:
			if f==2:
				b=32+4*l+d
			else:
				b=40+d+4*l
	else:
		if f%2==1:
			b=16*(f+1)+d-4*(3-l)
		else:
			b=16*(f+1)+d-4*(3-l)+8
	return b
#tfOut ends

for x in range (0,8):
	taktmaelir(x)
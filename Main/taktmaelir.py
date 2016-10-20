#taktmaelir begins
import time
FLASH=1
voice=0


def taktmaelir(dalkur) :
	global FLASH, status, voice						#global breytur, utskyrdar efst.
	for x in range (0,8):							#fyrir oll LED i 'dalkur'
		if status[dalkur][x][voice]==0:				#gert svo vid seum bara ad kveikja a led-um sem var slokkt a fyrir.
			trellis.setLED(tfOut(x*8+dalkur))				#kveikja a LED!
		#print(x*8+dalkur,tfOut(x*8+dalkur), 'on')
	trellis.writeDisplay() 							#uppfaera led a bordi.. VERDI LJOS!
	time.sleep(FLASH) 								#bidtimi eftir taktmaelis flash.
	for x in range (0,8): 							#fyrir oll LED i 'dalkur'
		if status[dalkur][x][voice]==0: 			#gert svo vid seum bara ad slokkva a led-um sem ekki var kveikt a fyrir "taktmaelir".
			trellis.clrLED(tfOut(x*8+dalkur)) 				#slokkva a LED!
		#print(x*8+dalkur,tfOut(x*8+dalkur), 'off')
	trellis.writeDisplay()							#uppfaera led a bordi.. VERDI MYRKUR!
#taktmaelir end



for x in range (0,8):
	taktmaelir(x)
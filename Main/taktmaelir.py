#taktmaelir begins
def taktmaelir(dalkur) :
	global FLASH, status, voice						#global breytur, útskýrðar efst.
	for x in range (0,8):							#fyrir öll LED í 'dálkur'
		if status[dalkur][x][voice]==0:				#gert svo við séum bara að kveikja a led-um sem var slökkt á fyrir.
			trellis.setLED(x*8+dalkur)				#kveikja á LED!
	trellis.writeDisplay() 							#uppfæra led á borði.. VERÐI LJÓS!
	time.sleep(FLASH) 								#biðtími eftir taktmælis flash.
	for x in range (0,8): 							#fyrir öll LED í 'dálkur'
		if status[dalkur][x][voice]==0: 			#gert svo við séum bara að slökkva á led-um sem ekki var kveikt á fyrir "taktmaelir".
			trellis.clrLED(x*8+dalkur) 				#slökkva á LED!
	trellis.writeDisplay()							#uppfæra led á borði.. VERÐI MYRKUR!
#taktmaelir end
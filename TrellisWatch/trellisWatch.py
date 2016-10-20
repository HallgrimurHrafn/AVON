#trellisWatch begins 	--- fylgist med tokkum a trellis. fyrir allt nema live mode, eins og er.


import time
import threading
import numpy as np 

tGo=0
lGO=0
mwGO=0
mcGo=0
clA=0
tempo=0.5
FLASH=0.1
lengd=0.1
status=np.zeros((8,8,16))
skali=np.array([60,62,64,65,67,69,71,72])
voice=0
stop=0

def trellisWatch():
	global tGO, status, voice, a, b, tStatus,clA,lGO,mwGO
	#if tGO==1 and lGO==0:							#-----------ATHUGA
	#	time.sleep(0.03) 							#bid sem var alltaf i synidaemum og gaeti kannski thurft ad auka.
	#												#ef sleep er aukid keyrir loop-an sjaldnar a minutu sem sparar resources i cpu. auka thetta til ad letta keyrslu ef tharf.
	#	status=tStatus 								#--------------utskyrt nedar-------
	#	if trellis.readSwitches():					#les hvort thad hafir verid ytt a EINHVERN takka 
	#		for x in range (0, 64):					#64 er fjoldi takka:
	#			if tGO==0 or lGO==1: 				
	#				break 							
	#			if trellis.justPressed(tfIn(x)): 	#spyr hvort thad hafi verid ytt a takka x.
	#				if status[x%8][x//8][voice]==0:	#les i fylkid hvort stadan hafi verid ovirkt adur. 	--- x%8 er gert rad fyrir ad se dalkur og x//8 lina. gaeti verid ofugt.
	#					status[x%8][x//8][voice]=1 	#setur stoduna sem virkt.
	#					trellis.setLED(tfOut(x)) 	#kveikir a ljosi a trellis undir takka x.
	#				else:
	#					status[x%8][x//8][voice]=0 	#her var x virkt svo nuna er thad gert ovirkt
	#					trellis.clrLED(tfOut(x)) 	#gert ovirkt svo vid slokkvum a LED-inu
	#	trellis.writeDisplay() 						#uppfaerir LED svo breytingarnar komi inn.
	#	tStatus=status 								#------------utskyring her fyrir nedan.
	#elif tGO==0 and lGO==0: 						#her eru 2 her um bil eins foll. eitt fyrir tStatus og eitt fyrir status.
	#	time.sleep(0.03) 							#ef ekki er haegt ad setja inn notur i status eins og er, tha er thad sett i
	#	if trellis.readSwitches():					#tStatus (temp) i stadinn. kveikt og slokkt er a ljosum sem skyldi.
	#		for x in range (0, 64): 				#thegar aftur ma setja i status tha veljum vid ad status=tStatus til ad allt sem
	#			if trellis.justPressed(tfin(x)): 	#gerdist a medan se inn i kerfinu. i lokin eftir ad vid hofum verid ad fylgjast med
	#				if tStatus[x%8][x//8][voice]==0:#status tha styllum vid tStatus=status. thetta tryggir ad tStatus er alltaf thad sama og status
	#					tStatus[x%8][x//8][voice]=1 #nema thegar thad ma ekki breyta status.
	#					trellis.setLED(tfOut(x)) 			
	#				else:
	#					tStatus[x%8][x//8][voice]=0 	
	#					trellis.clrLED(tfOut(x))
	time.sleep(0.03)

	if trellis.readSwitches():						#gerir alveg thad sama og gamla forritid i styttri koda.
		for x in range (0,64):				
			if trellis.justPressed(tfin(x)): 	
				if tStatus[x%8][x//8][voice]==0:
					tStatus[x%8][x//8][voice]=1 
					trellis.setLED(tfOut(x)) 			
				else:
					tStatus[x%8][x//8][voice]=0 	
					trellis.clrLED(tfOut(x))
		if tGO==1:
			status=tstatus
	if mwGO==1:
		modWatch()
	if lGO==1:
		livePlay() 									#trellisWatch thradurinn fer yfir i livePlay ef 
	if clA==1:
		clearAll()
	if load==1:										#load verdur fall til ad load inn gomlu status og mod.
		Load()										
	trellisWatch() 									#endurkvaemt fall svo thad heldur endalaust afram.
#trellisWatch ends 
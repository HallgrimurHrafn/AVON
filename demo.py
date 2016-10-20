#playcolumn begins --- spilar notur i dalk og takt maelinn lika.

import time
import threading
import numpy as np 
import Adafruit_Trellis


matrix0 = Adafruit_Trellis.Adafruit_Trellis()
matrix1 = Adafruit_Trellis.Adafruit_Trellis()
matrix2 = Adafruit_Trellis.Adafruit_Trellis()
matrix3 = Adafruit_Trellis.Adafruit_Trellis()


trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0, matrix1, matrix2, matrix3)

I2C_BUS = 1

trellis.begin((0x70,  I2C_BUS), (0x71, I2C_BUS), (0x72, I2C_BUS), (0x73, I2C_BUS))

lGO=0
mwGO=0
clA=0
tGo=0
mcGo=0
tempo=0.5
FLASH=0.05
lengd=0.1
status=np.zeros((8,8,16))
tStatus=np.zeros((8,8,16))
skali=np.array([72,71,69,67,65,64,62,60])
voice=0
stop=0


def playColumn(dalkur):
	global tempo, FLASH, status, tGO, mcGO,lengd	#global breytur, utskyrdar efst.
	tGO=0 											#slekkur a trellisWatch.
	for x in range (0,8):							#keyrir forlykkju fyrir allar mogulegar notur i gefnum dalki.
		for v in range (0,16): 						#gera forlykkju svo vid spilum allar voices (channels).
			if status[dalkur][x][v]==1: 			#spyr hvort nota med hnitin (dalkur,x) se virk.
				#midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x), velocity=100).bytes())  #velocity=mod(dalkur, x, v, 0)		
				print('on','channel er', v, 
					'notan er', skali[x], 'velocity er', 100)
				pass
													#ef svo er tha er sent midi-message gegnum midi pakkan mido med channel, 
													#notan er valin ur skala, og velocity ur fylkinu mod sem heldur utan um (x,y,z) thar sem (x,y) er 
													#hnit notunnar en z=1 heldur utan um velocity. svo (x,y,1) er velocity notunnar (x,y) 
	tGO=1
	mcGO=1 											#kveikir a modColumn
 	#ATHUGASEMD, svona er ekki haegt ad breyta 
 	#timasetningum fyrir note on eda off einstaklega. -expect some change.
	taktmaelir(dalkur) 								#herna kemur inn flash fra taktmaelir, ath thad lidur sma timi a medan sem er taknud FLASH.
	time.sleep(tempo-tempo*lengd-FLASH) 			#latum forritid bida med notuna i gangi. tempo timi milli upphaf notna. 
													#tempo*lengd er timinn sem notan lifir og FLASH er timinn sem taktmaelirinn notar.
	tGO=0
	mcGO=0 											#slekkur a modColumn
	for x in range (0,8): 						
		for v in range (0,16):
			if status[dalkur][x][v]==1:				#velur allar notur sem vid kveiktum a og slekkur a theim.
				#midiout.send_message(mido.Message('note_off', channel=voice, note=skali(x), velocity=0).bytes()) 		
				print('off','channel er', v,
					'notan er', skali[x], 'velocity er', 0)
				pass	
													#eini munurinn a thessu og sidasta er ad message-id er note_off og velocity er 0.
													#velocity er valid 0 vegna thess ad sum midi hljodfaeri nota ekki message-id note off heldur bara velocity 0.
	tGO=1 											#kveikir a trellisWatch.
	time.sleep(tempo*lengd) 						#timinn milli lok notu og upphaf naestu.
#playColumn ends		--- finna ut hvernig a ad deala vid mismunandi takta notna.



def taktmaelir(dalkur) :
	global FLASH, status, voice						#global breytur, utskyrdar efst.
	for x in range (0,8):							#fyrir oll LED i 'dalkur'
		#if status[dalkur][x][voice]==1:				#gert svo vid seum bara ad kveikja a led-um sem var slokkt a fyrir.
			#trellis.clrLED(tfOut(x*8+dalkur))
		#else:	
		trellis.setLED(tfOut(x*8+dalkur))				#kveikja a LED!
		#print(x*8+dalkur,tfOut(x*8+dalkur), 'on')
	trellis.writeDisplay() 							#uppfaera led a bordi.. VERDI LJOS!
	time.sleep(FLASH) 								#bidtimi eftir taktmaelis flash.
	for x in range (0,8): 							#fyrir oll LED i 'dalkur'
		if status[dalkur][x][voice]==0: 			#gert svo vid seum bara ad slokkva a led-um sem ekki var kveikt a fyrir "taktmaelir".
			trellis.clrLED(tfOut(x*8+dalkur))
		#else:
		#	trellis.clrLED(tfOut(x*8+dalkur)) 		#slokkva a LED!
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



#SEQUENCER LOOP, THIS IS IT YO GUYS:
def Sequencer():
	while True:									
		if stop == 0:									#ef ytt var a stopp tha leyfum vid sequencer-inum ekki ad spila.
			for dalkur in range (0,8): 					#fyrir alla dalka i sequencer.
				playColumn(dalkur) 						#spila notur dalks auk bid og taktmaelis.
				if stop == 1: 							#a ad stodva allt?
					break 								#ef svo er, stodvum vid loopuna.
		elif stop == 1: 								#ef sequencerinn var stoppadur er enginn astaeda til ad drepa orgjorvan. setjum sleep til ad 
			time.sleep(0.2)								#eyda minna afli orgjorvans.
		#BETRA ad gera event her.
					 									#annars/eftir ad spila i gegnum alla dalka, forum vid aftur i sequencer. "hala"endurkvaemt fall.
#SEQUENCER END, BOOOOOOOOOIIII	 			--- her tharf ekkert time.sleep thvi thad er nog af thvi i playcolumn svo vid braedum ekki kerfid.



#multithread starts		--- partur af main.
def multithread ():
	while True:
		t1=threading.Thread(target=trellisWatch)
		#t2=threading.Thread(target=myndavel)
		#t3=threading.Thread(target=menuWatch)
	
		t1.start()
		#t2.start()
		#t3.start()
	
		t1.join()
		#t2.join()
		#t3.join()
	
#multithread ends    --- breyta i function med if skilyrdum hvort thradur se daudur eda ekki.



#trellisWatch begins 	--- fylgist med tokkum a trellis. fyrir allt nema live mode, eins og er.
def trellisWatch():
	global tGO, status, voice, a, b, tStatus,clA,lGO,mwGO
	time.sleep(0.02)

	if trellis.readSwitches():						#gerir alveg thad sama og gamla forritid i styttri koda.
		for x in range (0,64):				
			if trellis.justPressed(x):
				y=tfIn(x) 	
				if tStatus[y%8][y//8][voice]==0:
					tStatus[y%8][y//8][voice]=1 
					trellis.setLED(x) 			
				else:
					tStatus[y%8][y//8][voice]=0 	
					trellis.clrLED(x)
		if tGO==1:
			status=tStatus
	if mwGO==1:
		modWatch()
	if lGO==1:
		livePlay() 									#trellisWatch thradurinn fer yfir i livePlay ef 
	if clA==1:
		clearAll()									
				 									#endurkvaemt fall svo thad heldur endalaust afram.
#trellisWatch ends 

t=threading.Thread(target=multithread)
t.start()
print('still running buddy')



#for x in range (0,8):
#	status[x][x][0]=1
#	print(status[x][x][0],x)

Sequencer()
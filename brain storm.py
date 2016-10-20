
from threading import thread
import time
import numpy as np 									#erum við ekki örugglega með numpy a pi? annars þurfum við að bæta þvi við.


#Startup only begin these should all be global variables.
trellis.readSwitches()								#man ekki af hverju eg setti thetta hingad. laet etta vera for now.
tempo=0.5											#tempo, timi milli byrjun notna.
lengd=0.1 											#notna lengd, hlutfall af tempo.
FLASH=0.1 											#styllir timalengd led flash i taktmaeli. ATH tempo>=tempo*lengd+FLASH
tGO=1 												#1 thydir ad trellisWatch er virkt, 0 thydir ovirkt.
cGO=0 												#-II- fyrir myndavel. tharf ad baeta fleiri breytum sem stjorna hvada parametrum er verid ad breyta.
mwGO=0  											#-II- fyrir hvort modWatch se virkt.
mcGO=0 												#-II- fyrir hvort modColumn se virkt.
lGO=0 												#-II- fyrir hvort liveplay se virkt.
velocity=100 										#50% af max.
voice=0 											#voice=channel. það channel sem er núna í notkun.
status=np.zeros((8,8,16))							#heldur utan um hvada notur eru merktar sem thekktar.
tStatus=np.zeros((8,8,16))					   		#heldur timabundid um breytur. t stendur fyrir temporary.
#dalkur,lina,channel.
mod=16*[8*[8*[8*[0]]]]np.zeros((8,8,16,8))			#mun halda utan um upplysingar hverrar notu sidar.
#dalkur,lina,channel,gildi.
skali=np.array([60,62,64,65,67,69,71,72]) 			#skali, nuna c dur. seinna a ad geta valid.
a=0 												
b=0 												#global breyturnar a og b eru hnit fyrir notu i modWatch.

#Startup only end  		--- þarf sennilega að breyta status í 8x8x16 fylki til að halda utan um voices.
#						--- Þarf sennilega amk 8x8x8 fyrir mod lika til að halda utan um nægar upplysingar. x,y hnit og z mod factor. fylki með gildum ekki 1 og 0.

	
   
#trellisWatch begins 	--- fylgist med tokkum a trellis. fyrir allt nema live mode, eins og er.
def trellisWatch():
	global tGO, status, voice, a, b, tStatus
	if tGO==1 and lGO==0:																						#-----------ATHUGA
		time.sleep(0.03) 							#bid sem var alltaf i synidaemum og gaeti kannski thurft ad auka.
													#ef sleep er aukið keyrir loop-an sjaldnar á mínútu sem sparar resources í cpu. auka þetta til að létta keyrslu ef þarf.
		status=tStatus 								#--------------utskyrt nedar-------
		if trellis.readSwitches():					#les hvort thad hafir verid ytt a EINHVERN takka 
			for x in range (0, 64) 					#64 er fjoldi takka:
				if tGO==0 or lGO==1: 				
					break 							
				if trellis.justPressed(x): 			#spyr hvort thad hafi verid ytt a takka x.
					if status[x%8][x//8][voice]==0:	#les i fylkid hvort stadan hafi verid ovirkt adur. 	--- x%8 er gert rad fyrir ad se dalkur og x//8 lina. gaeti verid rangt.
						status[x%8][x//8][voice]=1 	#setur stoduna sem virkt	--- kannski er thetta 4 en ekki 8 thar sem trellis-in sjalfur er bara 4 a lengd.
						trellis.setLED(x) 			#kveikir a ljosi a trellis undir takka x.
					else:
						status[x%8][x//8][voice]=0 	#her var x virkt svo nuna er thad gert ovirkt
						trellis.clrLED(x) 			#gert ovirkt svo vid slokkvum a LED-inu
		trellis.writeDisplay() 						#uppfærir LED svo breytingarnar komi inn.
		tStatus=status 								#------------uutskyring her fyrir nedan.
	elif tGO==0 and lGO==0: 						#her eru 2 her um bil eins foll. eitt fyrir tStatus og eitt fyrir status.
		time.sleep(0.03) 							#ef ekki er haegt að setja inn notur i status eins og er þá er það sett í
		if trellis.readSwitches():					#tStatus í staðinn. kveikt og slökkt er á ljósum sem skyldi.
			for x in range (0, 64) 					#þegar aftur má setja í status þá veljum við að status=tStatus til að allt sem
				if trellis.justPressed(x): 			#gerðist á meðan sé inn í kerfinu. í lokin eftir að við höfum verið að fylgjast með
					if tStatus[x%8][x//8][voice]==0:#status þá styllum við tStatus=status. þetta tryggir að tStatus er alltaf það sama og status
						tStatus[x%8][x//8][voice]=1 #nema þegar það má ekki breyta status.
						trellis.setLED(x) 			
					else:
						tStatus[x%8][x//8][voice]=0 	
						trellis.clrLED(x)
	elif lGO==1:
		livePlay() 									#trellisWatch þráðurinn fer yfir í livePlay ef 
	elif clA==1:
		clearAll()
	trellisWatch() 									#endurkvaemt fall svo thad heldur endalaust afram.
#trellisWatch ends
	


#modColumn begins		--- moddar dalkinn on the fly ef notad er 
def modColumn(dalkur):								#dalkurinn sem er verid ad modda
#modColumn ends			--- a augljuslega eftir ad paela betur i hvernig thetta verdur.



#myndavel begins 		--- SINDRI you have been summoned.
def myndavel ():
	if cGO==1:
		#STUFF
	else:
		time.sleep(1)								#lata forritið checka á 1 sekundu fresti hvort það sé kveikt. lengri start tími eeen
													#sparar cpu alveg massift.
#myndavel ends 		--- open cv dot.. vonandi er haegt ad gera thetta allt her, ef ekki tha thurfum vid ad koma med adra
#								 hugmynd um hvernig forritin tala saman



#playcolumn begins --- spilar notur i dalk og takt maelinn lika.
def playColumn(dalkur):
	global tempo, FLASH, status, tGO, mcGO			#global breytur, útskýrðar efst.
	tGO=0 											#slekkur a trellisWatch.
	#time.sleep(0.01)								#kannski þarf til að leyfa trellisWatch að klára for loopu.
	for x in range (0,8):							#keyrir forlykkju fyrir allar mogulegar notur i gefnum dalki.
		for v in range (0,16): 						#gera forlykkju svo við spilum allar voices (channels).
			if status[dalkur][x][v]==1: 			#spyr hvort nóta með hnitin (dalkur,x) sé virk.
				midiout.send_message(mido.Message('note_on', channel=voice, note=skali[x], velocity=mod(dalkur, x, v, 0)).bytes()) 		
													#ef svo er þá er sent midi-message gegnum midi pakkan mido með channel, 
													#notan er valin ur skala, og velocity ur fylkinu mod sem heldur utan um (x,y,z) þar sem (x,y) er 
													#hnit nótunnar en z=1 heldur utan um velocity. svo (x,y,1) er velocity notunnar (x,y) 
	tGO=1
	mcGO=1 											#kveikir á modColumn
 	#ATHUGASEMD, svona er ekki haegt ad breyta 
 	#timasetningum fyrir note on eda off einstaklega. -expect some change.
	taktmaelir(dalkur) 								#hérna kemur inn flash frá taktmælir, ath það líður smá tími á meðan sem er táknuð FLASH.
	time.sleep(tempo-tempo*lengd-FLASH) 			#látum forritið bíða með nótuna í gangi. tempo timi milli upphaf notna. 
													#tempo*lengd er tíminn sem nótan lifir og FLASH er tíminn sem taktmælirinn notar.
	tGO=0
	mcGO=0 											#slekkur a modColumn
	for x in range (0,8): 						
		for v in range (0,16):
			if status[dalkur][x][v]==1:				#velur allar notur sem við kveiktum og á og slekkur á þeim.
				midiout.send_message(mido.Message('note_off', channel=voice, note=skali[x], velocity=0).bytes()) 		
													#eini munurinn á þessu og síðasta er að message-ið er note_off og velocity er 0.
													#velocity er valið 0 vegna þess að sum midi hljóðfæri nota ekki message-ið note off heldur bara velocity 0.
	tGO=1 											#kveikir á trellisWatch.
	time.sleep(tempo*lengd) 						#tíminn milli lok nótu og upphaf næstu.
#playColumn ends		--- finna út hvernig á að deala við mismunandi takta nótna.



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



#SEQUENCER LOOP, THIS IS IT YO GUYS:
def Sequencer():									
	if (stop == 0):									#ef ýtt var á stopp þá leyfum við sequencer-inum ekki að spila.
		for dalkur in range (0,8): 					#fyrir alla dálka í sequencer.
			playColumn(dalkur) 						#spila nótur dálks auk bið og taktmælis.
			if (stop == 1) 							#a ad stodva allt?
				break 								#ef svo er, stöðvum við loopuna.
	elif (stop == 1): 								#ef sequencerinn var stoppaður er enginn ástæða til að drepa örgjörvan. setjum sleep til að 
		time.sleep(0.2)								#eyða minna afli örgjörvans.
	Sequencer() 									#annars/eftir að spila i gegnum alla dálka, förum við aftur i sequencer. "hala"endurkvæmt fall.
#SEQUENCER END, BOOOOOOOOOIIII	 			--- hér þarf ekkert time.sleep því það er nóg af því í playcolumn svo við bræðum ekki kerfið.



#clearAll begins 		--- eyðir öllum voice-um.
def clearAll():
	global status, mod
	for v in range (0,16):
		for dalkur in range (0, 8):
			for lina in range (0,8):
				status[dalkur][lina][v]=0
				#normalize(dalkur,lina,v)
	for x in range (0,64):
		trellis.clrLED(x)
	trellisWatch()
#clearAll ends



#modWatch begins 		--- her kemur mod vinnsla fyrir hverja notu fyrir sig. veit ekki hvar vid munum vinna med voice.
def modWatch():
	global a, b 									#global breytur, útskýrðar efst	
#modWatch ends    		--- vantar allt! .... nema a og b :)



#livePlay begins 		--- her er megin vinnslan fyrir liveplay partinn.
def livePlay():
	global voice, skali
	if trellis.readSwitches():
		for x in range (0, 64):
			if trellis.justPressed(x):
				midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x%8), velocity=60).bytes()) 
			if trellis.justReleased(x):
				midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x%8), velocity=60).bytes()) 

#livePlay ends  		--- vantar allt



#menuWatch begins 		--- vantar betra nafn á þetta fall. fylgist með öllum utanaðkomandi inputum nema trellis og myndavél. þ.e. knob og tökkunum
def menuWatch():
#menuWatch ends


	
#multithread starts		--- partur af main.
t1=thread(target=trellisWatch)
t2=thread(target=myndavel)
t3=thread(target=menuWatch)
t1.start()
t2.start()
t3.start()
#multithread ends    --- breyta i function með if skilyrðum hvort þráður sé dauður eða ekki.



#MAIN end
Sequencer()
#MAIN  end
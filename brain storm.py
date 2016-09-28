
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
msGO=0 												#-II- fyrir hvort modstuff se virkt.
velocity=63 										#50% af max.
voice=0 											#voice=channel. það channel sem er núna í notkun.
status=np.zeros((8,8,16))							#heldur utan um hvada notur eru merktar sem thekktar.
mod=16*[8*[8*[8*[0]]]]								#mun halda utan um upplysingar hverrar notu sidar.
tempStatus=np.zeros((8,8,16))						#heldur timabundid um breytur.
skali=[60, 62, 64, 65, 67, 69, 71, 72] 				#skali, nuna c dur. seinna a ad geta valid.
liveplay=0 											#hvort thetta se i liveplay mode eda sequencer mode.
a=0 												
b=0 												#global breyturnar a og b eru hnit fyrir notu i modWatch.
#Startup only end  		--- þarf sennilega að breyta status í 8x8x16 fylki til að halda utan um voices.
#						--- Þarf sennilega amk 8x8x8 fyrir mod lika til að halda utan um nægar upplysingar. x,y hnit og z mod factor. fylki með gildum ekki 1 og 0.

	
   
#trellisWatch begins 	--- fylgist med tokkum a trellis.
def trellisWatch():
	global tGO, status, voice, a, b					#global breytur, útskýrðar efst.
	if tGO==1:																						#-----------ATHUGA
		time.sleep(0.03) 							#bid sem var alltaf i synidaemum og gaeti kannski thurft ad auka.
		if trellis.readSwitches():					#les hvort thad hafir verid ytt a EINHVERN takka 
			for x in range (0, 63) 					#63+1 er fjoldi takka:
				if trellis.justPressed(x): 			#spyr hvort thad hafi verid ytt a takka x.
					if status[x%8][x//8][voice]==0:	#les i fylkid hvort stadan hafi verid ovirkt adur. 	--- x%8 er gert rad fyrir ad se dalkur og x//8 lina. gaeti verid rangt.
						status[x%8][x//8][voice]=1 	#setur stoduna sem virkt	--- kannski er thetta 4 en ekki 8 thar sem trellis-in sjalfur er bara 4 a lengd.
						trellis.setLED(x) 			#kveikir a ljosi a trellis undir takka x.
					else:
						status[x%8][x//8][voice]=0 	#her var x virkt svo nuna er thad gert ovirkt
						trellis.clrLED(x) 			#gert ovirkt svo vid slokkvum a LED-inu
		trellis.writeDisplay() 						#uppfærir LED svo breytingarnar komi inn.
	elif msGO=1:
		time.sleep(0.03)
		if trellis.readSwitches():
			for x in range (0, 63):
				if trellis.justPressed(x):
					mod




	trellisWatch() 									#endurkvaemt fall svo thad heldur endalaust afram.
#trellisWatch ends



#modstuff begins		--- moddar dalkinn on the fly ef notad er 
def modstuff(dalkur):								#dalkurinn sem er verid ad modda
#modWatch ends 			--- a augljuslega eftir ad paela betur i hvernig thetta verdur.



#myndavel begins 		--- SINDRI you have been summoned.
def myndavel ():
	#hehehe
#myndavel ends 		--- open cv dot.. vonandi er haegt ad gera thetta allt her, ef ekki tha thurfum vid ad koma med adra
#								 hugmynd um hvernig forritin tala saman



#playcolumn begins --- spilar notur i dalk og takt maelinn lika.
def playColumn(dalkur):
	global tempo, FLASH, status, tGO, msGO			#global breytur, útskýrðar efst.
	tGO=0 											#slekkur a trellisWatch.
	for x in range (0,7):							#keyrir forlykkju fyrir allar mogulegar notur i gefnum dalki.
		for v in range (0,15):
			if status[dalkur][x][v]==1: 			#spyr hvort nóta með hnitin (dalkur,x) sé virk.
				midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x), velocity=mod(v, dalkur, x, 1)).bytes()) 		
													#ef svo er þá er sent midi-message gegnum midi pakkan mido með channel, 
													#notan er valin ur skala, og velocity ur fylkinu mod sem heldur utan um (x,y,z) þar sem (x,y) er 
													#hnit nótunnar en z=1 heldur utan um velocity. svo (x,y,1) er velocity notunnar (x,y) 
	msGO=1 											#kveikir á modStuff
 	#ATHUGASEMD, svona er ekki haegt ad breyta 
 	#timasetningum fyrir note on eda off einstaklega. -expect some change.
	taktmaelir(dalkur) 								#hérna kemur inn flash frá taktmælir, ath það líður smá tími á meðan sem er táknuð FLASH.
	time.sleep(tempo-tempo*lengd-FLASH) 			#látum forritið bíða með nótuna í gangi. tempo timi milli upphaf notna. 
													#tempo*lengd er tíminn sem nótan lifir og FLASH er tíminn sem taktmælirinn notar.
	msGO=0 											#slekkur a modStuff
	for x in range (0,7): 						
		if status(dalkur,x)==1: 					#velur allar notur sem við kveiktum og á og slekkur á þeim.
			midiout.send_message(mido.Message('note_off', channel=voice, note=skali(x), velocity=0).bytes()) 		
													#eini munurinn á þessu og síðasta er að message-ið er note_off og velocity er 0.
													#velocity er valið 0 vegna þess að sum midi hljóðfæri nota ekki message-ið note off heldur bara velocity 0.
	tGO=1 											#kveikir á trellisWatch.
	time.sleep(tempo*lengd) 						#tíminn milli lok nótu og upphaf næstu.
#playColumn ends 		--- þarf að breyta status i 8x8x16 og deala við það. 
# 						--- finna út hvernig á að deala við mismunandi takta nótna.



#taktmaelir begins
def taktmaelir(dalkur) :
	global FLASH, status							#global breytur, útskýrðar efst.
	for x in range (0,8):							#fyrir öll LED í 'dálkur'
		trellis.setLED(x) 							#kveikja á LED!
	trellis.writeDisplay() 							#uppfæra led á borði.. VERÐI LJÓS!
	time.sleep(FLASH) 								#biðtími eftir taktmælis flash.
	for x in range (0,8): 							#fyrir öll LED í 'dálkur'
		trellis.clrLED(x) 							#slökkva á LED!
	trellis.writeDisplay()							#uppfæra led á borði.. VERÐI MYRKUR!
#taktmaelir end  		--- vantar ad kveikja a ljosum aftur sem voru tharna fyrir. eda excluda thau.
#						--- öllu helst að bua til fylki LED sem heldur utanum hvaða ljos eiga að vera i gangi currently.



#SEQUENCER LOOP, THIS IS IT YO GUYS:
def Sequencer():									
	if (livemode == 0 and modmode == 0  			#skoðar hvort AVON vinnslurými eigi að vera í sequencer-, live- eða modemode.
	    	and stop == 0):	
		for dalkur in range (0,7): 						#fyrir alla dálka í sequencer.
			playColumn(dalkur) 							#spila nótur dálks auk bið og taktmælis.
			if (livemode == 1 or modmode == 1 			#skoðar hvort það hafi verið breyting á hvaða mode er i gangi.
			or stop == 1) 								#a ad stodva allt?
				break 									#ef svo er, stöðvum við loopuna.
			sequencer() 								#förum aftur i sequencer. byrjun fallsins finnur ut hvort þurfi að flytja vinnslusvæðið.
	elif livemode == 1: 							#ef live mode er 1
		livePlay() 									#förum við í liveplay, sem er til að spila on the fly.
	elif modmode == 1: 								#ef modmode er 1
		modWatch() 									#förum við í modwatch.
	elif stop == 1:									#effectively drepur sequencerinn.
		pass 										#þvi pass gerir ekkert og þráðurinn endar eftir þetta.
	else:	
		Sequencer() 									#annars/eftir að spila i gegnum alla dálka, förum við aftur i sequencer. "hala"endurkvæmt fall.
#SEQUENCER END, BOOOOOOOOOIIII



#clearVoice begins 		--- það voice sem er í gangi er eytt út.
def clearVoice(voice):
#clearVoice ends



#clearAll begins 		--- eyðir öllum voice-um.
def clearAll():
#clearAll ends



#modWatch begins 		--- her kemur mod vinnsla fyrir hverja notu fyrir sig. veit ekki hvar vid munum vinna med voice.
def modWatch():
	global a, b 									#global breytur, útskýrðar efst	
#modStuff ends    		--- vantar allt! .... nema a og b :)



#livePlay begins 		--- her er megin vinnslan fyrir liveplay partinn.
def livePlay():
#livePlay ends  		--- vantar allt



#menuWatch begins 		--- vantar betra nafn á þetta fall. fylgist með öllum utanaðkomandi inputum nema trellis og myndavél. þ.e. knob og tökkunum
def menuWatch():
#menuWatch ends


	
#multithread starts		--- partur af main.
t1=thread(target=trellisWatch)
t2=thread(target=myndavel)
t3=thread(target=modWatch)
t4=thread(target=menuWatch)
t1.start()
t2.start()
t3.start()
t4.start()
#multithread ends    --- breyta i function með if skilyrðum hvort þráður sé dauður eða ekki.



#MAIN end
Sequencer()
#MAIN  end
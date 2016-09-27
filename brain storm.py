
from threading import thread
import time



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
status=8*[8*[0]]									#heldur utan um hvada notur eru merktar sem thekktar.
mod=8*[8*[0]] 										#mun halda utan um upplysingar hverrar notu sidar.
skali=[60, 62, 64, 65, 67, 69, 71, 72] 				#skali, nuna c dur. seinna a ad geta valid.
liveplay=0 											#hvort thetta se i liveplay mode eda sequencer mode.
a=0 												
b=0 												#global breyturnar a og b eru hnit fyrir notu i modWatch.
#Startup only end

	
   
#trellisWatch begins 	--- fylgist med tokkum a trellis.
def trellisWatch():
	global tGO										#til ad vera ad vinna med global breytu.
	global status									#-II-.
	if tGO==1:																						#-----------ATHUGA
		time.sleep(0.03) 							#bid sem var alltaf i synidaemum og gaeti kannski thurft ad auka.
		if trellis.readSwitches():					#les hvort thad hafir verid ytt a EINHVERN takka 
			for x in range (0, 63) 					#63+1 er fjoldi takka:
				if trellis.justPressed(x): 			#spyr hvort thad hafi verid ytt a takka x.
					if status[x%8,x//8]==0:			#les i fylkid hvort stadan hafi verid ovirkt adur. 	--- x%8 er gert rad fyrir ad se dalkur og x//8 lina. gaeti verid rangt.
						status[x%8,x//8]=1    		#setur stoduna sem virkt	--- kannski er thetta 4 en ekki 8 thar sem trellis-in sjalfur er bara 4 a lengd.
						trellis.setLED(x) 			#kveikir a ljosi a trellis undir takka x.
					else:
						status[x%8,x//8]=0 			#her var x virkt svo nuna er thad gert ovirkt
						trellis.clrLED(x) 			#gert ovirkt svo vid slokkvum a LED-inu
		trellis.writeDisplay() 						#uppfærir LED svo breytingarnar komi inn.
return trellisWatch() 								#endurkvaemt fall svo thad heldur endalaust afram.
#trellisWatch ends



#modstuff begins		--- moddar dalkinn on the fly ef notad er 
def modstuff(dalkur):								#dalkurinn sem er verid ad modda
#modWatch ends 			--- a augljuslega eftir ad paela betur i hvernig thetta verdur.



#myndavel begins 		--- SINDRI you have been summoned.
def myndavel ():
	#hehehe
#myndavel ends 		--- open cv dot.. vonandi er haegt ad gera thetta allt her, ef ekki tha thurfum vid ad koma med adra
#								 hugmynd um hvernig forritin tala saman



#playcolumn begin --- spilar notur i dalk og takt maelinn lika.
def playColumn(dalkur):
	global tempo  									#tempo er timi milli upphaf notna.
	global FLASH 									#timalengd thess er taktmaelirinn lysir dalk i takt.
	global status 									#astands fylki fyrir hvada notur eiga ad vera i gangi.
	global tGO 										#leyfir okkur ad breyta og lesa tGO.
	global msGO 									#-II- msGO
	tGO=0 											#slekkur a trellisWatch.
	for x in range (0,7):							#keyrir forlykkju fyrir allar mogulegar notur i gefnum dalki.
		if status(dalkur,x)==1: 					#spyr hvort nóta með hnitin (dalkur,x) sé virk.
			midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x), velocity=mod(dalkur, x, 1)).bytes()) 		
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
#translate status to tones end



#taktmaelir begin
def taktmaelir(dalkur) :
	global FLASH
	global status
	for x in range (0,8):
		trellis.setLED(x)
	trellis.writeDisplay()
	time.sleep(FLASH)
	for x in range (0,8):
		trellis.clrLED(x)
	trellis.writeDisplay()							#vantar ad kveikja a ljosum aftur sem voru tharna fyrir. eda excluda thau.
#taktmaelir end



#SEQUENCER LOOP, THIS IS IT YO GUYS:
def Sequencer():
	if (livemode == 0 and modmode == 0):
		for dalkur in range (0,7):
			playColumn(dalkur)
			if (if livemode == 1 or modmode == 1):
				break
	elif livemode == 1:
		livePlay()
	elif modmode == 1:
		modWatch()
	else :
		Sequencer()
#SEQUENCER END, BOOOOOOOOOIIII



#modWatch begins 		--- her kemur mod vinnsla fyrir hverja notu fyrir sig. veit ekki hvar vid munum vinna med voice.
def modWatch():
	global a
	global b

#modStuff ends



#livePlay begins 		--- her er megin vinnslan fyrir liveplay partinn.
def livePlay():
	blah
#livePlay ends



#multithread starts		--- partur af main.
t1=thread(target=trellisWatch)
t2=thread(target=myndavel)
t3=thread(target=modWatch)
t1.start()
t2.start()
t3.start()
#multithread ends



#MAIN end
Sequencer()
#MAIN  end
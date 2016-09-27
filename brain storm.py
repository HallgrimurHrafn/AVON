
from threading import thread
import time



#Startup only begin these should all be global variables.
trellis.readSwitches()		#man ekki af hverju eg setti thetta hingad. laet etta vera for now.
tempo=0.5						#tempo, timi milli byrjun notna.
lengd=0.1 						#notna lengd, hlutfall af tempo.
FLASH=0.1 						#styllir timalengd led flash i taktmaeli. ATH tempo>=tempo*lengd+FLASH
tGO=1 							#1 thydir ad trellisWatch er virkt, 0 thydir ovirkt.
cGO=0 							#-II- fyrir myndavel. tharf ad baeta fleiri breytum sem stjorna hvada parametrum er verid ad breyta.
mGO=0  							#-II- fyrir hvort modWatch se virkt.
velocity=63 					#50% af max.
status=8*[8*[0]]				#heldur utan um hvada notur eru merktar sem thekktar.
mod=8*[8*[0]] 					#mun halda utan um upplysingar hverrar notu sidar.
#Startup only end

	
   
#trellisWatch begins 	--- fylgist med tokkum a trellis.
def trellisWatch():
	global tGO
	if tGO==1:																						#-----------ATHUGA
		time.sleep(0.03) # bid sem var alltaf i synidaemum og gaeti kannski thurft ad auka.
		if trellis.readSwitches():
			for x in range (0, 63) # 63+1 er fjoldi takka:
				if trellis.justPressed(x):
					if status[x%8,x//8]==0:
						status[x%8,x//8]=1    #kannski er thetta 4 en ekki 8 thar sem trellis-in sjalfur er bara 4 a lengd.
						trellis.setLED(x)
					else:
						status[x%8,x//8]=0
						trellis.clrLED(x)
		trellis.writeDisplay()
return trellisWatch()
#trellisWatch ends



#modWatch begins		--- a bara ad vera i gangi thegar notandi er ad velja mods fyrir akvedna notu.
def modWatch (x, y):	#x og y eru hnit notunnar.
return
#modWatch ends 			--- a augljuslega eftir ad paela betur i hvernig thetta verdur.



#modStuff begins 		--- her kemur mod vinnsla fyrir hverja notu fyrir sig ad fraskyldu velocity. veit ekki hvar vid munum vinna med voice.
def modstuff (dalkur):
return
#modStuff ends



#myndavel begins 		--- SINDRI you have been summoned.
def myndavel ():
	#hehehe
return
#myndavel ends 		--- open cv dot.. vonandi er haegt ad gera thetta allt her, ef ekki tha thurfum vid ad koma med adra
#								 hugmynd um hvernig forritin tala saman



#playcolumn begin --- spilar notur i dalk og takt maelinn lika.
def playColumn (dalkur):
	global tempo
	global FLASH
	for x in range (0,7):
		if status(dalkur,x)==1:
			NOTEON(voice, x, velocity)
	taktmaelir
	time.sleep(tempo-tempo*lengd-FLASH)
	for x in range (dalkur,7):
		if status(dalkur,x)==1:
			NOTEOFF(voice, x, velocity)
	time.sleep(tempo*lengd)
	return
#translate status to tones end



#NOTEON begin
def NOTEON(voice, key, velocity) :
	####OKKUR VANTAR MIDI LIBRARY
	return
#NOTEON end



#NOTEOFF begin
def NOTEOFF(voice,key,velocity):
	######OKKUR VANTAR MIDI LIBRARY
	return
##NOTEOFF end


#taktmaelir begin
def taktmaelir :
	global FLASH
	for x in range (0,8):
		trellis.setLED(x)
	trellis.writeDisplay()
	time.sleep(FLASH)
	for x in range (0,8):
		trellis.clrLED(x)
	trellis.writeDisplay()


	#vantar ad kveikja a ljosum aftur sem voru tharna fyrir. eda excluda thau.

	return
#taktmaelir end



#multithread starts		--- partur af main.
t1=thread(target=trellisWatch)
t2=thread(target=myndavel)
t3=thread(target=modWatch)
t1.start()
t2.start()
t3.start()
#multithread ends



#MAIN LOOP begin ---- hvernig geri eg mainloop? geri eg kannski bara endalausa while loopu?
d=0
while d==0
	for x in range (0,7):
		playColumn (x)
#MAIN LOOP end
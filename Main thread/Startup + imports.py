
from threading import thread
import time
import numpy as np 									#erum við ekki örugglega með numpy a raspberry pi? annars þurfum við að bæta þvi við.


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
skali=[60, 62, 64, 65, 67, 69, 71, 72] 				#skali, nuna c dur. seinna a ad geta valid.
a=0 												
b=0 												#global breyturnar a og b eru hnit fyrir notu i modWatch.
cVA=0												#ef cVA=1 þá er öllu eytt.
SAVE=0												#hvort eigi að save-a...
#Startup only end  
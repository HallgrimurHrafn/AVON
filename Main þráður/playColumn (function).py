#playcolumn begins --- spilar notur i dalk og takt maelinn lika.
def playColumn(dalkur):
	global tempo, FLASH, status, tGO, mcGO			#global breytur, útskýrðar efst.
	tGO=0 											#slekkur a trellisWatch.
	#time.sleep(0.01)					#kannski þarf til að leyfa trellisWatch að klára for loopu.
	for x in range (0,7):							#keyrir forlykkju fyrir allar mogulegar notur i gefnum dalki.
		for v in range (0,15): 						#gera forlykkju svo við spilum allar voices (channels).
			if status[dalkur][x][v]==1: 			#spyr hvort nóta með hnitin (dalkur,x) sé virk.
				midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x), velocity=mod(dalkur, x, v, 0)).bytes()) 		
													#ef svo er þá er sent midi-message gegnum midi pakkan mido með channel, 
													#notan er valin ur skala, og velocity ur fylkinu mod sem heldur utan um (x,y,z) þar sem (x,y) er 
													#hnit nótunnar en z=1 heldur utan um velocity. svo (x,y,1) er velocity notunnar (x,y) 
	mcGO=1 											#kveikir á modColumn
 	#ATHUGASEMD, svona er ekki haegt ad breyta 
 	#timasetningum fyrir note on eda off einstaklega. -expect some change.
	taktmaelir(dalkur) 								#hérna kemur inn flash frá taktmælir, ath það líður smá tími á meðan sem er táknuð FLASH.
	time.sleep(tempo-tempo*lengd-FLASH) 			#látum forritið bíða með nótuna í gangi. tempo timi milli upphaf notna. 
													#tempo*lengd er tíminn sem nótan lifir og FLASH er tíminn sem taktmælirinn notar.
	mcGO=0 											#slekkur a modColumn
	for x in range (0,7): 						
		for v in range (0,15):
			if status[dalkur][x][v]==1:				#velur allar notur sem við kveiktum og á og slekkur á þeim.
				midiout.send_message(mido.Message('note_off', channel=voice, note=skali(x), velocity=0).bytes()) 		
													#eini munurinn á þessu og síðasta er að message-ið er note_off og velocity er 0.
													#velocity er valið 0 vegna þess að sum midi hljóðfæri nota ekki message-ið note off heldur bara velocity 0.
	tGO=1 											#kveikir á trellisWatch.
	time.sleep(tempo*lengd) 						#tíminn milli lok nótu og upphaf næstu.
#playColumn ends		--- finna út hvernig á að deala við mismunandi takta nótna.
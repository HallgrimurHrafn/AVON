#playcolumn begins --- spilar notur i dalk og takt maelinn lika.
def playColumn(dalkur):
	global tempo, FLASH, status, tGO, mcGO,lengd	#global breytur, utskyrdar efst.
	tGO=0 											#slekkur a trellisWatch.
	#time.sleep(0.01)								#kannski tharf til ad leyfa trellisWatch ad klara for loopu.
	for x in range (0,8):							#keyrir forlykkju fyrir allar mogulegar notur i gefnum dalki.
		for v in range (0,16): 						#gera forlykkju svo vid spilum allar voices (channels).
			if status[dalkur][x][v]==1: 			#spyr hvort nota med hnitin (dalkur,x) se virk.
				#midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x), velocity=60).bytes())  #velocity=mod(dalkur, x, v, 0)		
				print('on','channel er', v, 
					'notan er', skali[x], 'velocity er'
					, 60)
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
					'notan er', skali[x], 'velocity er'
					, 0)
													#eini munurinn a thessu og sidasta er ad message-id er note_off og velocity er 0.
													#velocity er valid 0 vegna thess ad sum midi hljodfaeri nota ekki message-id note off heldur bara velocity 0.
	tGO=1 											#kveikir a trellisWatch.
	time.sleep(tempo*lengd) 						#timinn milli lok notu og upphaf naestu.
#playColumn ends		--- finna ut hvernig a ad deala vid mismunandi takta notna.

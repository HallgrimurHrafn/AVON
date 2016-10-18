#SEQUENCER LOOP, THIS IS IT YO GUYS:
def Sequencer():									
	if (stop == 0):									#ef ýtt var á stopp þá leyfum við sequencer-inum ekki að spila.
		for dalkur in range (0,7): 					#fyrir alla dálka í sequencer.
			playColumn(dalkur) 						#spila nótur dálks auk bið og taktmælis.
			if (stop == 1) 							#a ad stodva allt?
				break 								#ef svo er, stöðvum við loopuna.
	elif (stop == 1): 								#ef sequencerinn var stoppaður er enginn ástæða til að drepa örgjörvan. setjum sleep til að 
		time.sleep(0.2)								#eyða minna afli örgjörvans.
	Sequencer() 									#annars/eftir að spila i gegnum alla dálka, förum við aftur i sequencer. "hala"endurkvæmt fall.
#SEQUENCER END, BOOOOOOOOOIIII	 			--- hér þarf ekkert time.sleep því það er nóg af því í playcolumn svo við bræðum ekki kerfið.
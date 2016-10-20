#SEQUENCER LOOP, THIS IS IT YO GUYS:
def Sequencer():									
	if stop == 0:									#ef ytt var a stopp tha leyfum vid sequencer-inum ekki ad spila.
		for dalkur in range (0,8): 					#fyrir alla dalka i sequencer.
			playColumn(dalkur) 						#spila notur dalks auk bid og taktmaelis.
			if stop == 1: 							#a ad stodva allt?
				break 								#ef svo er, stodvum vid loopuna.
	elif stop == 1: 								#ef sequencerinn var stoppadur er enginn astaeda til ad drepa orgjorvan. setjum sleep til ad 
		time.sleep(0.2)								#eyda minna afli orgjorvans.
		#BETRA ad gera event her.
	Sequencer() 									#annars/eftir ad spila i gegnum alla dalka, forum vid aftur i sequencer. "hala"endurkvaemt fall.
#SEQUENCER END, BOOOOOOOOOIIII	 			--- her tharf ekkert time.sleep thvi thad er nog af thvi i playcolumn svo vid braedum ekki kerfid.

#trellisWatch begins 	--- fylgist med tokkum a trellis. fyrir allt nema live mode, eins og er.
def trellisWatch():
	global tGO, status, voice, a, b, tStatus
	if tGO==1 and lGO==0:																						#-----------ATHUGA
		time.sleep(0.03) 							#bid sem var alltaf i synidaemum og gaeti kannski thurft ad auka.
													#ef sleep er aukið keyrir loop-an sjaldnar á mínútu sem sparar resources í cpu. auka þetta til að létta keyrslu ef þarf.
		status=tStatus 								#--------------utskyrt nedar-------
		if trellis.readSwitches():					#les hvort thad hafir verid ytt a EINHVERN takka 
			for x in range (0, 63) 					#63+1 er fjoldi takka:
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
			for x in range (0, 63) 					#þegar aftur má setja í status þá veljum við að status=tStatus til að allt sem
				if trellis.justPressed(x): 			#gerðist á meðan sé inn í kerfinu. í lokin eftir að við höfum verið að fylgjast með
					if tStatus[x%8][x//8][voice]==0:#status þá styllum við tStatus=status. þetta tryggir að tStatus er alltaf það sama og status
						tStatus[x%8][x//8][voice]=1 #nema þegar það má ekki breyta status.
						trellis.setLED(x) 			
					else:
						tStatus[x%8][x//8][voice]=0 	
						trellis.clrLED(x)
	elif mwGO==1:
		modWatch()
	elif lGO==1:
		livePlay() 									#trellisWatch þráðurinn fer yfir í livePlay ef 
	elif clA==1:
		clearAll()
	trellisWatch() 									#endurkvaemt fall svo thad heldur endalaust afram.
#trellisWatch ends 		--- vantar þriðja part lykkjunar, fyrir modwatch. þ.e. tone edit vs adding/removing tones.
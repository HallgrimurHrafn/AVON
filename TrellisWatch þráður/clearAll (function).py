#clearAll begins 		--- eyðir öllum voice-um.
def clearAll():
	global status, mod
	for v in range (0,15):
		for dalkur in range (0, 7):
			for lina in range (0,7):
				status[dalkur][lina][v]=0
				#normalize(dalkur,lina,v)
	for x in range (0,63):
		trellis.clrLED(x)
	trellisWatch()
#clearAll ends
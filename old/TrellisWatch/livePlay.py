voice=0
skali=np.array([60,62,64,65,67,69,71,72])

#livePlay begins 		--- her er megin vinnslan fyrir liveplay partinn.
def livePlay():
	global voice, skali
	if trellis.readSwitches():
		for x in range (0, 63):
			if trellis.justPressed(x):
				print('on','channel er', v,'notan er', skali[x], 'velocity er', 60)
				#midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x%8), velocity=60).bytes()) 
			
			if trellis.justReleased(x):
				print('off','channel er', v,'notan er', skali[x], 'velocity er', 0)
				#midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x%8), velocity=60).bytes()) 

#livePlay ends  		--- vantar allt
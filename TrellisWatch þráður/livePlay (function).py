#livePlay begins 		--- her er megin vinnslan fyrir liveplay partinn.
def livePlay():
	global voice, skali
	if trellis.readSwitches():
		for x in range (0, 63):
			if trellis.justPressed(x):
				midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x%8), velocity=60).bytes()) 
			if trellis.justReleased(x):
				midiout.send_message(mido.Message('note_on', channel=voice, note=skali(x%8), velocity=60).bytes()) 

#livePlay ends  		--- vantar allt
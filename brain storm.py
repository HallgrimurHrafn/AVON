

import time
#Startup only begin

trellis.readSwitches()
k=8
y=0.5	#brot af tempo
mod=k*[k*[0]]
status=k*[k*[0]]
velocity=60	#test for now
voice=0 	#test for now
#Startup only end

#Interrupt fyrir takka begin
def intterrupt:
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
return
#interrupt fyrir takka end

#translate status to tones begin 
def translate (dalkur)
	for x in range (0,7):
		if status(dalkur,x)==1:
			NOTEON(voice, x, velocity)

	taktmaelir

	time.sleep(y-0.2)
	 
	for x in range (dalkur,7):
		if status(dalkur,x)==1:
			NOTEOFF(voice, x, velocity)

	time.sleep(0.1)
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
	for x in range (0,8):
		trellis.setLED(x)
	trellis.writeDisplay()
	time.sleep(0.1)
	for x in range (0,8):
		trellis.clrLED(x)
	trellis.writeDisplay()
	return
#taktmaelir end



#MAIN LOOP begin

for x in range (0,7):
	interrupt()
	translate (x)


#MAIN LOOP end
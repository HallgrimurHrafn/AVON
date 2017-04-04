#ifndef MAIN_H
#define MAIN_H

#include "global.h"
#include <thread>
#include <math.h>
#include <stdlib.h>
#include "scrollMap.h"
#include "avon-gui/avonwidget.h"
#include "metro.h" // tempo operations and status
#include "metro.cpp" // tempo operations and status
#include "midime.h"
#include "trellis.h"



// FROM main.py @@@@ Sequencer Part.
void Sequencer() {
	for(;;)
	{
		if (stop == 0)
		{
			for(int i = 0; i<8; i++)
			{
        timi = (15000000/myMetro.getTempo())/bar;
				for(int j=0; j<8; j++){
    				Scale[j] = newScale[j];
				}
				column = i;
				playColumn(column);
                while (paused == 1) {
					usleep(100000);

					if (stop == 1)
						break;
				}
				if (stop == 1)
					break;
			}
		}
        while (paused == 1)
			usleep(100000);
	}
}

void playColumn(int column)
{
    // Creating thread to play current column.
    thread p1(NOTEON,column,true);
    p1.detach();
    // Wait for note duration.
    usleep(timi-timi*length);
    // Turn the note off.
    thread p2(NOTEOFF,column);
    p2.detach();
    // Delay before next column should start playing.
    usleep(timi*length);
}

void NOTEON(int column, bool cd)
{
	tick = TIME::now();
	trellStatus = 0;
	for(int i=0;i<8;i++) {
		for(int j=0; j<16;j++) {
			if(status[j][column][i] == 1)
				midime(144+j,Scale[i],100);
		}
	}
	trellStatus = 1;
	modWatch = 1;
	metronome(column);
}

void NOTEOFF(int column)
{
	trellStatus = 0;
	for(int i = 0; i < 8;i++)
	{
		for(int j = 0; j < 16; j++)
		{
			if(status[j][column][i] == 1)
				midime(128+j,Scale[i],100);
		}
	}
	modWatch =0;
	trellStatus = 1;
}

void metronome(column) // vantar info um trellis
{
	metroLed = true;
	for(int i =0; i<8; 1++)
		setLED(invTrellisTransf(i * 8 + column));
	writeDisplay();
	usleep(FLASH*timi);
	for(int i =0; i<8; 1){
	  if (status[channel][column][i] == 0)
      	clrLED(invTrellisTransf(i * 8 + column));
	}
  	writeDisplay();
	metroLed = false;
}

void Sync()
{
	for(int i=0; i<16 ; i++)
	{
		midime(240,0,0);
		usleep((timi-synctime)/12);
	}
}

// FROM Main.py @@@@ Trellis Transformations.
int TrellisTransf(int a) // Trellis format to our format
{
	int f = a/16;
	int d = (a % 16) % 4;
	int l = (a % 16) / 4;
	int b;
	if (f % 2 == 0)
      b = 16 * f + 8 * l + d;
	else
      b = 16 * (f + 1) - (3 - l) * 8 + d - 4;
  	return b;
}

int invTrellisTransf(int a)  // Our format to Trellis format
{
	int f = a / 16;
  	int d = (a % 16) % 8;
  	int l = (a % 16) / 8;
	int b;
  	if (d < 4)
		{
      	if (f < 2)
       	   b = 8 * f + 4 * l + d;
      	else
		{
  	      if (f == 2)
	          b = 32 + 4 * l + d;
          else
              b = 40 + d + 4 * l;
		}
	}
	else
	{
      if (f % 2 == 1)
          b = 16 * (f + 1) + d - 4 * (3 - l);
      else
          b = 16 * (f + 1) + d - 4 * (3 - l) + 8;
	}
  	return b
}


// FROM Main.py @@@@ Setting up trellis events.
void trellisEventSetup()
{
	usleep(15000);
	if (live == 1)
	{
		thread ls(liveSet);
		ls.detach();
	}
	else
	{
		thread te(sequencerSet);
		te.detach();
	}
}

void trellisWatch()
{
	if (live)
		livePlay();
	else
		sequencerWatch();
}

void sequencerSet()
{
	int ready = false;
	int matrix[8][8] = {0};
	// Creating Matrix as a 8x8 matrix copy of status for current channel.
	// and getting the correct status back from tStatus.
	for (int i=0;i<16;i++) {
		for (int j=0;j<8;j++) {
			for (int k=0;k<8;k++) {
				status[i][j][k]=tStatus[i][j][k];
				if (i==channel)
					matrix[j][k] = status[i][j][k];
			}
		}
	}
  ledshow(matrix);
}

void sequencerWatch()
{
	usleep(15000);  // requirement for trellis to process the change.
	if (readSwitches()) { // was a key pressed?
		for (int i=0; i<64; i++) { // for all keys in trellis.
			if (justPressed(i)) { // was this exact key pressed?
				int y = TrellisTransf(i);  // transform key to our format.
				if (tStatus[channel][y%8][y/8] == 0) { // if key was off
					tStatus[channel][y%8][y/8] = 1; // turn it on
					setLED(x); // also turn on the LED.
				}
				else {
					tStatus[channel][y%8][y/8] = 0; // turn it off
					clrLED(x); // and turn of the LED
				}
				readSwitches(); // an attempt to improve response time.
			}
		}
		writeDisplay(); // update the LEDs on trellis.
		if (trellStatus == 1) { // are we allowed to update status.
			for (int i=0; i<16; i++) { // setting status=tStatus for values not pointers.
				for (int j=0; j<64; j++) {
					status[i][j%8][j/8] = tStatus[i][j%8][j/8];
				}
			}
			usleep(15000); // attempt to improve response time
			readSwitches(); // attempt to improve response time
		}
		else {
			usleep(15000); // attempt to improve response time
			readSwitches(); // attempt to improve response time
			sequencerWatch(); // not allowed to update status. cant wait since
			// we could get a data hazard if multiple notes were pressed. for the price
			// of some performance we cann rerun the function to update it. This should
			// prevent the data hazard and possible improve response time as well.
		}
	}
}


void liveSet()
{
	// Saving the status to tStatus.
	for(int i=0;i<16;i++)
	{
		for (int j=0;j<8;j++)
		{
			for (int k=0;k<8;k++)
				tStatus[i][j][k] = status[i][j][k];
		}
	}
	// Setting the status of this channel to 0 to prevent sequencer from playing it.
  for (int i=0; i<64; i++)
     status[channel][i % 8][i / 8] = 0
	 // Creating an empty 8x8 matrix for ledshow.
	 int matrix[8][8] = {0};
  ledshow(matrix);
}

void livePlay()   // ????
{
	if (live == 1) { // are we in livemode.
		usleep(30000); // required to allow trellis to process information.
		if (readSwitches())	{ // update trellis info, was a key pressed?
			for(int i=0; i<64; i++) { // iterate through all keys
				int y = TrellisTransf(i); // transform into our system.
				if (justPressed(i)){ // was this key just pressed?
					midime(144+channel, scale[y/8], 100); // send out note.
					setLED(i); // turn on led
				} else if (justReleased(i)) { // was this key just released?
					midime(128+channel, scale[y/8], 0); // stop note..
					clrLED(i); // turn off led
				}
			}
			writeDisplay(); // update LEDS
		}
	}
}


void channelChange()
{
	if (nextChannel != channel)
	{
		// remove all the leds.
    clearLeds();
		// turning on leds for metronome if currently flashing.
    if (metroLed){
			for(int i=0; i<8; i++)
				setLED(invTrellisTransf(i * 8 + column));
        }
		// updating channel and turning on corresponding leds.
  	channel=nextChannel;
		for (int x=0; x<64; x++)
		{
			y = TrellisTransf(x);
			if (status[channel][y % 8][y / 8] == 1)
				setLED(x);
		}
		// update the board.
  	writeDisplay();
	}
}


// FROM Main.py @@@@ LED operations on the trellis keypad.
void ledshow(int matrix[][8])
{
	for (int i = 0; i<6; i++)
	{
		if (i<4)
		{
			for(int j = 0; j<ledsNum[i];j++)
				setLED(leds[i][j]);
		}
		if (i>1)
		{
			for(int j = 0; j<j<ledsNum[i-2];j++)
				ledHelp(leds[i-2][j],matrix);
		}
	}
}

void ledHelp(int x, int matrix[][8])
{
	int y = TrellisTransf(x);
  if (matrix[y % 8][y / 8] ==0)
  		clrLED(x);
}



void clearLeds(){
	for(int i = 0; i<64; i++)
		clrLED(i);
	writeDisplay();
}

// FROM Main.py @@@@ Button related Functions.
void PlayPause()
{
	cout << "playpause" << endl;
    if (paused == 0)
        paused = 1;
	else
        paused = 0;
}

void stopper()
{
	cout << "stopper" << endl;
	if (stop == 0)
	{
		stop = 1;
        paused = 1;
		usleep(timi);
		stop = 0;
	}
}



// FROM Rotary.py @@@@ The Rotary solution.
void Rotary(int RotaryNum, int leftPin, int rightPin){
// RotaryNum indicates what Rotary was used.
// RotaryAction indicates what was done. 0=click, 1=Left Rotate or Right Rotate.

// Clockwise:
// 0,0 : state 0
// 1,0 : state 1
// 1,1 : state 2
// 0,1 : state 3
// 0,0 : state 0  Full turn.

	int tempLeft = digitalRead(leftPin);
	int tempRight = digitalRead(rightPin);
	// Did we change state?
	if ((leftTurn[RotaryNum] == tempLeft) && (rightTurn[RotaryNum] == tempRight))
		return;  // if not, return. else we update state.
	leftTurn[RotaryNum] = tempLeft;
	rightTurn[RotaryNum] = tempRight;
	prevState[RotaryNum] = state[RotaryNum];
	state[RotaryNum] = abs(3*rightTurn[RotaryNum]-leftTurn[RotaryNum]);
	// If current state is 0 then the rotary has done a full turn.
	if (state[RotaryNum] == 0)
		{
			if (prevState[RotaryNum] == 1)
				// MOVE TO RIGHT.
				Map(RotaryNum, 1);
			else if (prevState[RotaryNum] == 3)
				// MOVE TO LEFT.
				Map(RotaryNum, -1);
		}
	return;
}


// FROM ALLOVER @@@@ GPIO INTERRUPT SYSTEM.
void Interruption()
{
	wiringPiSetupGpio ();

	pinMode(4, INPUT); // Trellis
	pinMode(20, INPUT); // STOP
	pinMode(21, INPUT); // PLAY/PAUSE
	pinMode(16, INPUT); // TAP
	pinMode(13, INPUT); // rotary 1 right
	pinMode(19, INPUT); // rotary 1 left
	pinMode(26, INPUT); // rotary 1 click
	pinMode(5, INPUT); // rotary 2 right
	pinMode(6, INPUT); // rotary 2 left
	pinMode(12, INPUT); // rotary 2 click

  	pullUpDnControl(4, PUD_UP); // Trellis
  	pullUpDnControl(20, PUD_UP); // STOP
  	pullUpDnControl(21, PUD_UP); // PLAY/PAUSE
  	pullUpDnControl(16, PUD_UP); // TAP
  	pullUpDnControl(13, PUD_UP); // rotary 1 right
  	pullUpDnControl(19, PUD_UP); // rotary 1 left
  	pullUpDnControl(26, PUD_UP); // rotary 1 click
  	pullUpDnControl(5, PUD_UP); // rotary 2 right
  	pullUpDnControl(6, PUD_UP); // rotary 2 left
  	pullUpDnControl(12, PUD_UP); // rotary 2 click

  	wiringPiISR (4, INT_EDGE_FALLING, &trellisPrep); // s
  	wiringPiISR (20, INT_EDGE_FALLING, &stopperPrep); //STOP
  	wiringPiISR (21, INT_EDGE_FALLING, &PlayPausePrep); // PLAY/PAUSE
  	wiringPiISR (16, INT_EDGE_FALLING, &callbackTapPrep); //TAP
  	wiringPiISR (13, INT_EDGE_FALLING, &rotary1Prep); // rotary 1 right
  	wiringPiISR (19, INT_EDGE_FALLING, &rotary1Prep); // rotary 1 left
  	wiringPiISR (26, INT_EDGE_FALLING, &clickerPrep1); // rotary 1 click
  	wiringPiISR (5, INT_EDGE_FALLING, &rotary2Prep); // rotary 2 right
  	wiringPiISR (6, INT_EDGE_FALLING, &rotary2Prep); // rotary 2 left
  	wiringPiISR (12, INT_EDGE_FALLING, &clickerPrep2); // rotary 2 click

	for(;;)
	{
		usleep(1000000);
	}
}

// NEW @@@@ groundwork interruptions.
void trellisPrep()
{
	auto tock = TIME::now();
	timer timeDifference = tock-trellisBounce;
	ms timeDifferenceMs = chrono::duration_cast<ms>(timeDifference);
	if(timeDifferenceMs> hundradms/5)
	{
	 thread trellisThread(trellisWatch);
	 trellisThread.detach();
	 trellisBounce = tock;
	}
}

void stopperPrep()
{
	auto tock = TIME::now();
	timer timeDifference = tock-stopBounce;
	ms timeDifferenceMs = chrono::duration_cast<ms>(timeDifference);
	if(timeDifferenceMs> hundradms*2)
	{
	 thread StopperThread(stopper);
	 StopperThread.detach();
	 stopBounce = tock;
	}
}

void PlayPausePrep()
{
	auto tock = TIME::now();
	timer timeDifference = tock-playBounce;
	ms timeDifferenceMs = chrono::duration_cast<ms>(timeDifference);
	if(timeDifferenceMs> hundradms*2)
	{
	 thread PlayPauseThread(PlayPause);
	 PlayPauseThread.detach();
	 playBounce = tock;
	}
}

void callbackTapPrep()
{
	auto tock = TIME::now();
	timer timeDifference = tock-tapBounce;
	ms timeDifferenceMs = chrono::duration_cast<ms>(timeDifference);
	if(timeDifferenceMs> hundradms)
	{
  	thread TapThread(myMetro.callbackTap());
	 	TapThread.detach();
	 	tapBounce = tock;
	}
}



void clickerPrep1()
{
	auto tock = TIME::now();
	timer timeDifference = tock-Rotary1Bounce;
	ms timeDifferenceMs = chrono::duration_cast<ms>(timeDifference);
	if(timeDifferenceMs> hundradms)
	{
	 thread clicker2Thread(clicker, 0);
	 clicker2Thread.detach();
	 Rotary1Bounce = tock;
	}
}

void clickerPrep2()
{
	auto tock = TIME::now();
	timer timeDifference = tock-Rotary2Bounce;
	ms timeDifferenceMs = chrono::duration_cast<ms>(timeDifference);
	if(timeDifferenceMs> hundradms)
	{
	 thread clicker1Thread(clicker, 1);
	 clicker1Thread.detach();
	 Rotary2Bounce = tock;
	}
}

void rotary1Prep()
{
	thread Rotary1Thread(Rotary,0,19,13);
	Rotary1Thread.detach();
}

void rotary2Prep()
{
	thread Rotary2Thread(Rotary,1,5,6);
	Rotary2Thread.detach();
}


// FROM menu.py @@@@ NAVIGATION

void clicker(int Num)
{
	if (Num == 1)
	{
		string mapKey = to_string(nav[1])+to_string(nav[0]);
		clickMap().find(mapKey)->second;
	}
	else
        moveUp();
}

void moveUp()
{
	// Not allowed to move up in first position.
	if (nav[1] == 0)
		return;
	// Setting navigation for current depth to 0.
	oldNav[nav[1]] = 0;
	// Update navigation depth.
	if (nav[1] == 3)
		addScale();
	else
		nav[1] = 0;
	// Get old navigation for the new depth.
	nav[0] = oldNav[nav[1]];
}

void Map(int RotaryNum, int val)
{
	if(RotaryNum==0)
    fScrollMapX(nav[1],nav[0],val);
	else if(RotaryNum==1)
		fScrollMapY(nav[1],nav[0],val);
}


// From Menu.py  @@@@ Functions!
void channelPrep(int val)
{
	if(0<= nextChannel+val && nextChannel+val<=15)
		{
			nextChannel=nextChannel+val;
      channelChange();
			renderChan = true;
			cout << channel << endl;
		}
}




//////////////////////////////////////////////////////////////////////
////////////////// Methods that trigger UI changes! //////////////////
//////////////////////////////////////////////////////////////////////

Class MainInteractions {

    AvonWidget &mrBarks;

    public:
        MainInteractions(AvonWidget &a): avonwidget(a) {
            // Warning: outer is not fully constructed yet
            //          don't use it in here
            std::cout << "Inner: " << this << std::endl;
        };


// no comprendo en ok
void tempoChange(int val,int x)
{
    int BPM = myMetro.getTempo();
    if(60/float(BPM+val*x)/float(bar/4)>=0.05)
    {
        myMetro.tapOK = false;
        usleep(10000);
        Metro.setTempo(BPM + val*x);
        myMetro.tapOK = true;

        &mrBarks.refreshTempo();
    }
}

void liveChange()
{
    live = 1-live;
    renderLive = true;
    trellisEventSetup();

    &mrBarks.refreshMode();
}

void cameraChange()
{
    if(cam)
        camOFF();
    else
        camON();

    mrBarks->refreshChan();
}

void camON()
{
    cam = true;
    seen = true;
    thread c1(vision);
    c1.detach();
    thread c2(cam);
    c2.detach();
}

void camOFF()
{
    cam = false;
    seen = false;
}

void cameraMode(int val, int xyz)		// Bragi þarf smá hjálp hér. µµµµ
{
    if(xyz==0)
    {

    }
    else if(xyz==1)
    {

    }
    else if(xyz==2)
    {

    }
}

void noteLengthChange(int value)
{
    float val=-float(value)/20;
    if(0<length+val && length+val<1)
    {
        length = length+val;
        cout << length << endl;
    }

    &mrBarks.refreshLength();

}

void barChange(int val)
{
    float x = pow(2,val);
    if(60/float(myMetro.getTempo())/float(x*bar/4)>=0.05)
        bar=bar*x;

    mrBarks->refreshStep();
}

void changeScale(int val,int x)
{
    if(x==1)
    {
        if(0<= note+val && note+val <=127)
        {
            note += val;
            cout << note << endl;
        }
    }
    else if(x==0)
    {
	      currentScale = (currentScale+val)%(Scales.size());
    }
    if (currentScale != scales.size())
    {
        for(int i =0;i<8;i++)
          newScale[i] = scales[currentScale][i]+note;
    }
}

void modScale(int val,int i)
{
    if(0<= custom[i]+val+note && custom[i]+val+note<=127)
        custom[i] += val; // new skali copy
}

void createScale()
{
	if(currentScale>2)
	{
		oldNav[nav[1]] = nav[0];
		nav[] = {0,3};
		for(int i=0; i<8; i++)
			custom[i]=0;
	}
}

void addScale()
{
	if (currentScale == scales.size())
	{
		scales.resize(scales.size()+1,vector<int>(8));		// Resize the scale vector
		for(int i=0;i<8:i++)
			scales[scales.size()-1][i] = custom[i];
	}
	else if (currentScale > 3){
		for(int i=0;i<8:i++)
			scales[currentScale-1][i] = custom[i];
	}
}


// From cam.py  @@@@ Functions!
void cam()
{
	while(cam)
	{
		ms t = chrono::duration_cast<ms>(fabs(TIME:now()-tick));
		if(timi-t>=0)
			usleep(timi-t);
		else
			usleep(t-timi);
		for(int i = 0;i<8;i++)
		{
			auto t = TIME::now();
			if(!cam)
				return;
			if(camera()[0]==1)
			{
				if(cursorxyz[0]==1 & i==0)
				{
					thread t1(opperate,1);
					t1.detach();
				}

				else
				{
					if(cursorxyz[0] != 1)
					{
						int mapKey = cursorxyz[0];
						xmod().find(mapKey)->second(cursorxyz[0]);
					}
				}
				if(cursorxyz[1] == 1 && i==0)
				{
					thread t2(opperate,2);
					t2.detach();
				}
 				else
 				{
 					if(cursorxyz!=1)
 					{
 						int mapKey = cursorxyz[1];
 						ymod().find(mapKey)->second(cursorxyz[0]);
 					}
 				}
 				if(cursorxyz[2] == 1 && i==0)
 				{
 					thread t3(opperate,3);
 					t3.detach();
 				}
 				else
 				{
 					if(cursorxyz!=1)
 					{
 						int mapKey = cursorxyz[2];
 						zmod().find(mapKey)->second(cursorxyz[0]);
 					}
 				}
 				else
 					passer(0);
 				if(i!=7)
 					usleep(timi/8+chrono::duration_cast<ms>(TIME:now()-t));
 			}
		}
	}
}

void opperate(int x)				// µµµµ
{
	if(x==1)
		xmod().find(cursorxyz[0])->second(camera()[1]);
	if(x==2)
		ymod().find(cursorxyz[1])->second(camera()[2]);
	if(x==3)
		zmod().find(cursorxyz[2])->second(camera()[3]);
}

void notes(int note)
{
	midime(144+channel,note,100);
	usleep(timi-timi*length);
	midime(128+channel,note,0);
}

void bPitch(int val)
{
	midime(224+channel,0,val);
}

void modWheel(int val)
{
	midime(176+channel,1,val);
}


void initialize()
{
	// // create Bouncetime
	// auto t2 = TIME::now();
	// usleep(100000);
  // 	auto t1 = TIME::now();
	// timer mismunur = tock-tick;
  // 	hundradms = chrono::duration_cast<ms>(mismunur);

	// Run Ledshow 3-4 times for starting animation
	int empty[8][8] = {};
	for (int i=0; i<3; i++)
		ledshow(empty);
	// start a thread for the Interruption
	thread InterruptionThread(Interruption);
	InterruptionThread.detach();
	// Start Sequencer.
	Sequencer();
}

};

//////////////////////////////////////////////////////////////////////
/////////////// End of methods that trigger UI changes! //////////////
//////////////////////////////////////////////////////////////////////

#endif

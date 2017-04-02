#ifndef MAIN_H
#define MAIN_H

#include "global.h"
#include <thread>
#include <math.h>
#include <stdlib.h>
#include "scrollMap.h"

// FROM main.py @@@@ Sequencer Part.
void Sequencer() {
	for(;;)
	{
		if (stop == 0)
		{
			for(int i = 0; i<8; i++)
			{
				timi = (15000000/BPM)/bar;
				for(int j=0; j<8; j++){
    			Scale[j] = newScale[j];
				}
				column = i;
				playColumn(column);
				while (pause == 1) {
					usleep(100000);

					if (stop == 1)
						break;
				}
				if (stop == 1)
					break;
			}
		}
		while (pause == 1)
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
	mcGo = 1;
	metronome(column);
}

void NOTEOFF(int column)
{
	trellStatus = 0;
	mcGo =0, //?
	for(int i = 0; i < 8;i++)
	{
		for(int j = 0; j < 16; j++)
		{
			if(status[j][column][i] == 1)
				midime(128+j,Scale[i],100);
		}
	}
	trellStatus = 1;
}

void metronome(column) // vantar info um trellis
{
	metroLed = true;
	for(int i =0; i<8; 1++)
		!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		trellis.setLED(invTrellisTransf(i * 8 + column));
	trellis.writeDisplay();
	!!!!!!!!!!!!!!!!!!!!!!!!!!!
	usleep(FLASH*timi);
	for(int i =0; i<8; 1){
	  if (status[channel][column][i] == 0)
		!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      trellis.clrLED(invTrellisTransf(i * 8 + column));
	}
  trellis.writeDisplay();
	!!!!!!!!!!!!!!!!!!!!!!!!!!
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
void multithread()
{
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	// GPIO.remove_event_detect(4)
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	usleep(15000);
	if (live == 1)
		thread ls(liveSet);
		ls.detach();
	else
		thread te(sequencerSet);
		te.detach();
}

void trellisWatch()
{
	if (live)
		livePlay();
	else
		sequencerPlay();
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

void sequencerPlay()  //  ????
{

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

}

void ChannelChange()
{
	if (nextChannel != channel)
	{
		// remove all the leds.
    clearleds()
		// turning on leds for metronome if currently flashing.
    if (metroLed){
			for(int i=0; i<8; i++)
				!!!!!!!!!!!!!!!!!!!!!!!!!!
				trellis.setLED(invTrellisTransf(i * 8 + column))
		}
		// updating channel and turning on corresponding leds.
  	channel=nextChannel;
		for (int x=0; x<64; x++)
		{
			y = TrellisTransf(x);
			if (status[channel][y % 8][y / 8] == 1)
				!!!!!!!!!!!!!!!
				trellis.setLED(x)
		}
		// update the board.
		!!!!!!!!!!!!!!!!!!!!!!
  	trellis.writeDisplay();
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
			!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				trellis.setLED(leds[i][j]);
		}
		if (i>1)
		{
			for(int j = 0; j<j<ledsNum[i-2];j++)
				ledhelp(leds[i-2][j],matrix);
		}
	}
}

void ledhelp(int x, int matrix[][8])
{
	int y = TrellisTransf(x);
  if (matrix[y % 8][y / 8] ==0)
      trellis.clrLED(x); !!!!!!!!!!!!!!!!!!!!
}



void clearleds(){
	for(int i = 0; i<64; i++)
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		trellis.clrLED(i);
	trellis.writeDisplay();
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}

// FROM Main.py @@@@ Button related Functions.
void PlayPause()
{
	cout << "playpause" << endl;
	if (pause == 0)
		pause = 1;
	else
		pause = 0;
}

void stopper()
{
	cout << "stopper" << endl;
	if (stop == 0)
	{
		stop = 1;
		pause = 1;
		usleep(timi);
		stop = 0;
	}
}


void calcBPM(vector<double> tap, vector<double> period)
{
	// þarf að tala við Mr.Karl;
	high_resolution_clock::TIME currentTime = high_resolution_clock::now();

	tap.push_back(currentTime);
	int tapCount = period.size();
	double avgPeriod = 0;
	if(tapCount==1)
		return;
	elseif ((tap.end()-(tap.end()-1))>=3 || (tap.end()-(tap.end()-1))<=0.2)
	{
		tap.erase(period.begin(),period.end()-1);
		return;
	}

	elseif(tapCount==2)
	{
		period.push_back(tap.end()-(tap.end()-1));
		return;
	}
	period.push_back(tap.end()-(tap.end()-1));

	if(tapCount==3)
		avgPeriod = (period.end()+(period.end()-1))/2;
	elseif (tapCount==4)
		avgPeriod = (period.end()+(period.end()-1)+(period.end()-2))/3;
	else
		avgPeriod = (period.end()+(period.end()-1)+2*(period.end()-2))/4;

	BPM = round(60/avgPeriod);
	return;
}

void callbackTap()
{
	if(tapTempo==0)
		return;
	calcBPM(tap,period);
	cout << "BPM: " << BPM << endl;
}

// FROM Rotary.py @@@@ The Rotary solution.
void Rotary(int RotaryNum, int RotaryAction, int leftPin, int rightPin){
// RotaryNum indicates what Rotary was used.
// RotaryAction indicates what was done. 0=click, 1=Left Rotate, 2=Right Rotate.

// Clockwise:
// 0,0 : state 0
// 1,0 : state 1
// 1,1 : state 2
// 0,1 : state 3
// 0,0 : state 0  Full turn.

	int tempLeft = digitalRead(leftPin);
	int tempRight = digitalRead(rightPin);
	if(RotaryAction == 0)
	{
		clicker(RotaryNum);
		return;
	}
	// Did we change state?
	else if ((leftTurn[RotaryNum] == tempLeft) && (rightTurn[RotaryNum] == tempRight))
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

  wiringPiISR (4, INT_EDGE_FALLING, &success(4)); // Trellis
  wiringPiISR (20, INT_EDGE_FALLING, &stopper()); //STOP
  wiringPiISR (21, INT_EDGE_FALLING, &PlayPause()); // PLAY/PAUSE
  wiringPiISR (16, INT_EDGE_FALLING, &trellisWatch()); //TAP
  wiringPiISR (13, INT_EDGE_FALLING, &Rotary(0, 2, 19, 13)); // rotary 1 right
  wiringPiISR (19, INT_EDGE_FALLING, &Rotary(0, 1, 19, 13)); // rotary 1 left
  wiringPiISR (26, INT_EDGE_FALLING, &Rotary(0, 0, 19, 13)); // rotary 1 click
  wiringPiISR (5, INT_EDGE_FALLING, &Rotary(1, 2, 5, 6)); // rotary 2 right
  wiringPiISR (6, INT_EDGE_FALLING, &Rotary(1, 1, 5, 6)); // rotary 2 left
  wiringPiISR (12, INT_EDGE_FALLING, &Rotary(1, 0, 5, 6)); // rotary 2 click

	for(;;)
	{
		usleep(1000000);
	}
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
		nav[1] = 2;
	else
		nav[1] = 0;
	// Get old navigation for the new depth.
	nav[0] = oldNav[nav[1]];
}

void Map(int RotaryNum, int val)
{
	if(RotaryNum==0)
		fScrollMapX(nav[1],nav[0],val);
	elseif(RotaryNum==1)
		fScrollMapY(nav[1],nav[0],val);
}


// From Menu.py  @@@@ Functions!
void channelPrep(int val)
{
	if(0<= nextChannel+val && nextChannel+val<=15)
		{
			nextChannel=nextChannel+val;
			ChannelChange();
			renderChan = true;
			cout << channel << endl;
		}
}

void tempChange(int val,int x)
{
	if(60/float(BPM+val*x)/float(bar/4)>=0.05)
	{
		tapTempo = 0;
		usleep(10000);
		BPM += val*x;
		tapTempo = 1;
	}
}

void liveChange()
{
	if(live==1)
		live=0;
	else
		live=1;
	renderLive = true;
	multithread();
}

void cameraChange()
{
	if(cam)
		camOFF();
	else
		camON();
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

void cameraMode(int val, int xyz)		// Bragi þarf smá hjálp hér.
{
	if(xyz==0)
	{

	}
	elseif(xyz==1)
	{

	}
	elseif(xyz==2)
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
}

void barChange(int val)
{
	float x = pow(2,val);
	if(60/float(BPM)/float(x*bar/4)>=0.05)
		bar=bar*x;
}

void scaleChange(int val,int x)
{
	if(x==1)
	{
		if(0<= note+val && note+val <=127)
		{
			note += val;
			cout << note << endl;
		}
	}
	elseif(x==0)
	{
		currentScale = (currentScale+val)%(((sizeof(Scales)/sizeof(*Scales))));
		// skoða með custom?
		cout ...
	}
	if (currentScale != 3)
	{
		for(int i =0;i<8;i++)
		{
			newScale[i] = scales[currentScale][i];
		}
	}
}

void customScale(int val,int i)
{
	if(0<= custom[i]+val && custom[i]+val<=127)
	{
		custom[i] += int(val);
		// new skali copy
	}
}

void customSetup()

void createNewScale()

// From cam.py  @@@@ Functions!

void vision()

void cam()
{
	while(cam)
	{

	}
}
<<<<<<< HEAD
#endif
=======

#endif
>>>>>>> origin/master

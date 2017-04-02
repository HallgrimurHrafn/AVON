#ifndef MAIN_H
#define MAIN_H

#include "global.h"
#include <thread>
#include <math.h>
#include <stdlib.h>
#include "scrollMap.h"


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
	// Wait for note duration.
	usleep(timi-timi*length);
	// Turn the note off.
	thread p2(NOTEOFF,column);
	// Delay before next column should start playing.
	usleep(timi*length);
}

void NOTEON(int column, bool cd)
{
	tick = TIME::now();
	trellStatus = 0;
	for(int i=0;i<8;i++)
	{
		for(int j=0; j<16;j++)
		{
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

void multithread()
{
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	// GPIO.remove_event_detect(4)
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	usleep(15000);
	if (live == 1)
		thread ls(liveSet);
	else:
		thread te(trellisEvent);
}

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

void trellisEvent();
// vantar GPIO library   ????

void trellisWatch();
// Vantar trellis Library   ????

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

void callbackTap(int channel)
{
	if(tapTempo==0)
		return;
	calcBPM(tap,period,BPM);
	cout << "BPM: " << BPM << endl;
}
void liveset();    // ????

void liveplay();   // ????

void ledshow(int matrix[][8])   // ????
{

}

void ChannelChange();    // ???

void clearleds(){
	for(int i = 0; i<64; i++)
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		trellis.clrLED(i);
	trellis.writeDisplay();
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}



// FROM Rotary.py @@@@

// Clockwise:
// 0,0 : state 0
// 1,0 : state 1
// 1,1 : state 2
// 0,1 : state 3
// 0,0 : state 0  Full turn.
void Rotary(int RotaryNum, int RotaryAction, int leftPin, int rightPin){
// RotaryNum indicates what Rotary was used.
// RotaryAction indicates what was done. 0=click, 1=Left Rotate, 2=Right Rotate.
	int tempLeft = !!!!!!GPIOinput(leftPin)!!!!!!!!;
	int tempRight = !!!!!!GPIOinput(rightPin)!!!!!!!!;
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
				move(RotaryNum, 1);
			else if (prevState[RotaryNum] == 3)
				// MOVE TO LEFT.
				move(RotaryNum, -1);
		}
	return;
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


// From Menu.py  @@@@ Functions!
void move(int RotaryNum, int val)
{
	if(RotaryNum==1)
		kort(i,val);
	else
		kort(1,val);
}


void kort(int RotaryNum, int val)
{
	if(RotaryNum==0)
		fScrollMapX(nav[1],nav[0],val);
	elseif(RotaryNum==1)
		fScrollMapY(nav[1],nav[0],val);
}

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
	thread c2(cam);
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

void noteLendthChange(int value)
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
		// skoða þetta halli
	}

}
#endif

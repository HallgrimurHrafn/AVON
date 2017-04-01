#include "global.h"
#include <thread>
#include <math.h>
#include <stdlib.h>


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

void calcBPM(float tap, int period, int tempo)
{

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
		!!!!!Menu.click(RotaryNum)!!!!!
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
			else if (prevState[RotaryNum] == 3)
				// MOVE TO LEFT.
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

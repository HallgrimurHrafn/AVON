#include "global.h"
#include <thread>


void playColumn(int column)
{
	thread p1(NOTEON,column,true);
	usleep(timi-timi*length);
	thread p2(NOTEOFF,column);
	usleep(timi*length);
}

void NOTEON(int column, bool cd)
{
	time_h tick;
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
	if(cd)
		metronome(column);
}

void NOTEOFF(column)
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

void Sync()
{
	for(int i=0; i<16 ; i++)
	{
		midime(240,0,0);
		usleep((timi-synctime)/12);
	}
}

void TrellisTransf() // Trellis format to our format

void invTrellisTransf()  // Our format to Trellis format

void multithread();

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

void trellisWatch();

void calcBPM(float tap, int period, int tempo)
{
	time_t currentTime 

}

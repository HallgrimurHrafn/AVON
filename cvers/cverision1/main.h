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
				midime(144+j,skali[i],100);
		}
	}
}


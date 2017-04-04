#include "wiringSerial.c"
#include <iostream>

using namespace std;

int wiringPiSetupGpio(void);

int inRange(int value,int min, int max)
{
	if (value<min)
	{
		value = min;
	}
	if (value>max)
	{
		value = max;
	}
	return value;
}


void midime(int cmd,int note,int val)
{
	note = inRange(note,0,127);
	val = inRange(val,0,127);
	char ccmd = cmd;
	char cnote = note;
	char cval = val;
	char msg[] = {ccmd,cnote,cval};
	cout << note << endl;
	cout << val << endl;
	int fd = serialOpen("/dev/ttyAMA0",38400);
	serialPuts(fd,msg);
}

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <sstream>
#include <wiringSerial.h>

using namespace std;

void midime(int cmd,int note, int val)
{
	if (note < 0)
	{
		note = 0;
	}
	if(note > 127)
	{
		note = 127;
	}
	stringstream sscmd;
	stringstream ssnote;
	stringstream ssval;
	string scmd;
	string snote;
	string sval;
	char com = cmd;
	sscmd << com;
	sscmd >> scmd;
	char nota = note;
	ssnote << nota;
	ssnote >> snote;
	char va = val;
	ssval << va;
	ssval >> sval;
	string mess = scmd+snote+sval;
	const char *msg = mess.c_str();
	int fd = serialOpen("/dev/ttyAMA0", 38400);
	serialPuts(fd,msg);
}


int main()
{
	int note = 64;
	int val = 100;
	int cmd = 144;
	midime(cmd,note,val) ;
	return 0;
}


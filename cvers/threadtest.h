#include <stdio.h>
#include <iostream>
#include <thread>
#include <unistd.h>
using namespace std;

void forrit1(int x, int y)
{
	cout << "t1:" << x+y << endl;
	cout << "t1: sofum í 4 sek" << endl;
	sleep(4);
	cout << "t1: vöknum, prentum aftur eftir 0.5 sek" << endl;
	usleep(500000);
	cout << "t1: " << x+y << endl;
	cout << "t1 hefur klárað sitt" << endl;
}

void forrit2(int x, char a)
{
	cout << "hæ t2 hér" << endl;
	cout << "ætla að telja uppá 10" << endl;
	for(int i = 0; i<11; i++)
	{
		cout << i << endl;
		sleep(1);
	}
	cout << "t2 er búinn" << endl;
}

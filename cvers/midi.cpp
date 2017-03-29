#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include "midime.h"

using namespace std;

int wiringPiSetup(void);

int main()
{
	int note;
	int val;
	while(1<2)
	{
		cout << "Please select a note" << endl;
		cin >> note;
		cout << "Please select velocity" << endl;
		cin >> val;
		midime(144,note,val);
		usleep(100000);
		midime(128,note,val);
	}
	return 0;
}

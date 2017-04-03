#include "trellis.h"
#include <iostream>

int main() {
	initialize();
	bool test;
	for (int i=0; i<65;i++)
		test = readSwitches();
	cout<<test << endl;
	finalise();
}

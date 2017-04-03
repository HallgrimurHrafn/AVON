#include "trellis.h"
#include <iostream>

int main() {
	initialize();
	bool test;
	cout<<"start" << endl;
	for (int i=0; i<65;i++)
		test = readSwitches();
	cout<<"stop" << endl;
	finalise();
}

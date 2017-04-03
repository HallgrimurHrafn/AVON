#include "trellis.h"
#include <iostream>

int main() {
	initialize();
	string test = readSwitches();
	cout<<test << endl;
	string test2 = justPressed(3);
	cout<<test2 << endl;
	finalise();
}

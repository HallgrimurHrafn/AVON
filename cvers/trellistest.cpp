#include "trellis.h"
#include <iostream>

int main() {
	initialize();
	bool test = readSwitches();
	cout<<test << endl;
	finalise();
}

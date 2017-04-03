#include "trellis.h"

int main() {
	initialize();
	bool test = readSwitches();
	cout<<test << endl;
	finalise();
}

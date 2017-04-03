#include "trellis.h"

int main() {
	initialize();
	for(int i=0;i<64;i++)
	{
		setLED(i);
		writeDisplay();
		sleep(1);
	}
	finalise();
}

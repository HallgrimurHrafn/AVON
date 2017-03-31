#include <iostream>
#include <stdio.h>
#include <chrono>
#include <unistd.h>

using namespace std;

chrono::time_point t0 = steady_clock::now();

void blah()
{	
	while(true)
	{
		steady_clock::time_point t1=timer::now();
		duration<double> x = t1-t0;
		cout << x.count() << endl;
		usleep(500000);
	}
}

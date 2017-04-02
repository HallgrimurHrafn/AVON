#include <iostream>
#include <stdio.h>
#include "changeval.h"

using namespace std;


void checkval()
{
	x = 2;
	cout << x << endl;
	cout << y << endl;
	changevalue();
	y = 0;
}

int main()
{
	cout << x <<endl;
	cout << y << endl;
	changevalue();
	cout << x << endl;
	cout << y << endl;
	checkval();
	cout << x+y << endl;
	return 0;
}

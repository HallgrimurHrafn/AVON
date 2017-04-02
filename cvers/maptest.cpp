#include <iostream>
#include "maptest.h"
#include "printer.h"
void printer1(int x, int y)
{
	cout<< x <<endl;
	cout<< y <<endl;
}
void printer2(int x, int y)
{
	cout<< x+y << endl;
}
void printer3(int x, int y)
{
	cout << x/y << endl;
}
int x;
int y;

int main()
{
	string mapKey;
	while(1<2)
	{
		cout << "Select x" << endl;
		cin >> x;
		cout << "Select y" << endl;
		cin >> y;
		cout << "'lol' - print x and y" << endl;
		cout << "'0' - print x and y" << endl;
		cout << "'3' - print x and y" << endl;
		cin >> mapKey;
		myMap().find(mapKey)->second(x,y); 
	}
}

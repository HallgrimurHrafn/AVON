#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int a[] ={1,3,5};
int b[] = {2,4,6};

string mess;

int main()
{
	int x;
	int y;
	cout << "Value a" << endl;
	cin >> x;
	cout << "value b" << endl;
	cin >> y;
	mess = to_string(a[x])+to_string(b[y]);
	cout << mess << endl;
	return 0;
}

#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

vector<int> a;

int main()
{
	a.push_back(1);
	cout << a[0] << endl;
	for(int i = 0;i<4;i++)
	{
		a.push_back(i);
	}
	for (int i=0; i<a.size(); ++i)
		cout << a[i] << endl;
	return 0;
}

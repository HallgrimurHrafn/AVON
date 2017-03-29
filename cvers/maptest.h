#include <stdio.h>
#include <map>
#include <boost/bind.hpp>
#include <array>
using namespace std;
typedef void (*intfunc_t)(int,int);
typedef map<string,intfunc_t> mama;

extern int x;
extern int y;
static mama m;
int scali[8] = {0,0,0,0,0,0,0,0};
void passer(int,int){};
extern void printer(int,int);
//extern void printer2(int,int);
//extern void printer3(int,int);
inline mama & myMap()
{
	m["lol"] = printer;
	m["0"] = printer;
	m["3"] = printer;
	return m;
}

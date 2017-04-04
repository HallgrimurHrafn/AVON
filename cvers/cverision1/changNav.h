#ifndef CHANGNAV_H
#define CHANGNAV_H
#include "scopeFix.h"

extern int oldNav[];
extern int nav[];

void changNav1()
{
	oldNav[nav[1]] = nav[0];
	nav[] = {0,1};
}
void changNav2()
{
	oldNav[nav[1]] = nav[0];
	nav[] = {0,2};
}
void changNav4()
{
	oldNav[nav[1]] = nav[0];
	nav[] = {0,4};
}

#endif

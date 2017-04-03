#ifndef SCROLLMAP_H
#define SCROLLMAP_H

#include <stdio.h>

#include "main.h"
using namespace std;

extern void passer(int);
extern int nav[];

void fScrollMapY(int line, int column,int val)
{
	if(line == 0)
	{
        if (column==0)
			tempChange(val,1);
        else if (column==1)
			channelChange(val);
        else if (column==3)
			liveChange();
        else if (column==4)
			cameraChange();
        else if (column==5)
			noteLengthChange(val);
        else if (column==6)
			barChange();
		else
			passer(0);
	}
	elseif(line==1)
	{
        if (column==0)
			tempChange(val,100);
        else if (column==1)
			tempChange(val,10);
        else if (column==2)
			tempChange(val,1);
		else
			passer(0);
	}
    else if (line==2)
	{
        if (column<2)
			scaleChange(val,column%1);
		else
			passer(0);
	}
    else if (line==3)
	{
		customScale(val,7-(column)%8);
	}
    else if (line==4)
	{
        if (column<3)
			cameraMode(val,column);
		else
			passer(0);
	}
}
void fScrollMapX(int line, int column,int val)
{
	if(column==0)
	{
		if(val==1)
			nav[0]+=val;
	}
    else if(column==1)
	{
		if(line==2)
		{
			if(val==-1)
				nav[0]+=val;
		}
	}
    else if(line==3)
	{
		if(column<7)
			nav[0]+=val;
		else
		{
			if(val==-1)
				nav[0]+=val;
		}
	}
    else if(line==0 && column<7)
	{
		if(column==6)
		{
			if(val==-1)
				nav[0]+=val;
		}
		else
            nav[0]+=val;
	}
    else if(column==2 && (line==1 || line==4))
	{
		if(val==-1)
			nav[0]+=val;
	}
	else
		passer(0);
}
#endif

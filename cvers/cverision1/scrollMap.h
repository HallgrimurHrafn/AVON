#ifndef SCROLLMAP_H
#define SCROLLMAP_H

#include <stdio.h>


using namespace std;

extern void passer(int);
extern int nav[];
extern void tempChange(int val, int x);
extern void channelChange(int val);
extern void liveChange();
extern void cameraChange();
extern void noteLengthChange(int value);
extern void barChange();
extern void scaleChange(int val, int x);
extern void cameraMode(int val, int x);

MainInteractions mainy;
void fScrollMapY(int row, int column,int val)
{
	if (row == 0)
	{
        if (column==0)
            tempoChange(val,1);
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
    else if (row==1)
	{
        if (column==0)
			tempoChange(val,100);
        else if (column==1)
			tempoChange(val,10);
        else if (column==2)
			tempoChange(val,1);
		else
			passer(0);
	}
    else if  (row==2)
	{
        if (column<2)
			scaleChange(val,column%1);
		else
			passer(0);
	}
    else if  (row==3)
	{
		customScale(val,7-(column)%8);
	}
    else if  (row==4)
	{
        if (column<3)
			cameraMode(val,column);
		else
			passer(0);
	}
}
void fScrollMapX(int (row, int column,int val)
{
	if(column==0)
	{
		if(val==1)
			nav[0]+=val;
	}
    else if(column==1)
	{
		if (row==2)
		{
			if(val==-1)
				nav[0]+=val;
		}
	}
    else if (row==3)
	{
		if(column<7)
			nav[0]+=val;
		else
		{
			if(val==-1)
				nav[0]+=val;
		}
	}
    else if (row==0 && column<7)
	{
		if(column==6)
		{
			if(val==-1)
				nav[0]+=val;
		}
		else
            nav[0]+=val;
	}
    else if(column==2 &&  (row==1 || (row==4))
	{
		if(val==-1)
			nav[0]+=val;
	}
	else
		passer(0);
}
#endif

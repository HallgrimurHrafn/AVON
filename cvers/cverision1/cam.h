
void cam()
{
	while(cam)
	{
		ms t = duration_cast<ms>(fabs(TIME:now()-tick));
		if(timi-t>=0)
			usleep(timi-t);
		else
			usleep(t-timi);
		for(int i = 0;i<8;i++)
		{
			auto t = TIME::now();
			if(!cam)
				return;
			if(seen)
			{
				if(cursorxyz[0]==1 & i==0)
					thread t1(opperate,1);
				else
				{
					if(cursorxyz[0] != 1)
					{
						int mapKey = cursorxyz[0];
						xmod().find(mapKey)->second(cursorxyz[0]);
					}
				}
				if(cursorxyz[1] == 1 && i==0)
					thread t2(opperate,2);
 				else
 				{
 					if(cursorxyz!=1)
 					{
 						int mapKey = cursorxyz[1];
 						ymod().find(mapKey)->second(cursorxyz[0]);
 					}
 				}
 				if(cursorxyz[2] == 1 && i==0)
 					thread t3(opperate,3);
 				else
 				{
 					if(cursorxyz!=1)
 					{
 						int mapKey = cursorxyz[2];
 						zmod().find(mapKey)->second(cursorxyz[0]);
 					}
 				}
 				else
 					passer(0);
 				if(i!=7)
 					usleep(timi/8+duration_cast<ms>(TIME:now()-t));
 			}
		}
	}
}

void opperate(int x)
{
	if(x==1)
		xmod().find(cursorxyz[0])->second(BÍÐAEFTIRVEKTOR);
	if(x==2)
		ymod().find(cursorxyz[1])->second(BÍÐAEFTIRVEKTOR);
	if(x==3)
		zmod().find(cursorxyz[2])->second(BÍÐAEFTIRVEKTOR);
}

void notes(int note)
{
	midime(144+channel,note,100);
	usleep(timi-timi*length);
	midime(128+channel,note,0);
}

void bPitch(int val)
{
	midime(224+channel,0,val);
}
void modWheel(int val)
{
	midime(176+channel,1,val);
}
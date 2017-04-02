#include "threadtest.h"
#include <thread>

int main()
{
	cout << "byrjum t1" << endl;
	thread t1(&forrit1,1,5);
	cout << "byrjum t2" << endl;
	thread t2(&forrit2,10,'a');
	cout << "sofum í 15 sek" << endl;
	sleep(15);
	cout << "ég er vaknaður, bless" << endl;
	return 0;
}

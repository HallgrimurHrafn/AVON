#include <stdio.h>
#include <thread>
#include <wiringPi.h>
#include <iostream>
#include <time.h>
#include <unistd.h>
// #include <chrono>
using namespace std;

auto tick = time::now();
auto tick2 = time::now();

void success(int a)
{
  cout << a << endl;
}

void supsuccess()
{
 tick = time::now();
 if(tick-tick2> 10)
 {
   thread test(success,0);
   test.detach();
   tick2 = tick;
 }
}

int main() {
  wiringPiSetupGpio ();

  int pin = 21;
  pinMode(pin, INPUT);
  pullUpDnControl(pin, PUD_UP);
  // wiringPiISR (pin, INT_EDGE_FALLING, &success(4));
  // wiringPiISR (pin, INT_EDGE_FALLING, &success);
  // wiringPiISR (pin, INT_EDGE_FALLING, &success2());
  wiringPiISR (pin, INT_EDGE_FALLING, &supsuccess);
  for(;;)
  {
    usleep(1000000);
  }
}

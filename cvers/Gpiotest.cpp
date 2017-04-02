#include <stdio.h>
#include <thread>
#include <wiringPi.h>
#include <iostream>
#include <time.h>
#include <unistd.h>
#include <chrono>

typedef chrono::high_resolution_clock TIME;
typedef chrono::milliseconds ms;
typedef chrono::duration<float> timer;

using namespace std;

auto tick = TIME::now();
auto tick2 = TIME::now();

void success(int a)
{
  cout << a << endl;
}

void supsuccess()
{
 tick = TIME::now();
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

#include <stdio.h>
#include <thread>
#include <wiringPi.h>
#include <iostream>
#include <time.h>
#include <unistd.h>
// #include <chrono>
using namespace std;

void success(int a)
{
  cout << a << endl;
}

void supsuccess()
{
   thread test(success,0);
   test.detach();
   usleep(100000);
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

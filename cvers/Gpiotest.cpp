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
  cout << "OUTPUT! "<< a << endl;
}

void success2()
{
  thread suc(success,32);
}
int main() {
  wiringPiSetupGpio ();

  int pin = 21;
  pinMode(pin, INPUT);
  pullUpDnControl(pin, PUD_UP);
  wiringPiISR (pin, INT_EDGE_FALLING, &success(4));
  wiringPiISR (pin, INT_EDGE_FALLING, &success2);
  wiringPiISR (pin, INT_EDGE_FALLING, &success2());
  // wiringPiISR (pin, INT_EDGE_FALLING, thread suc(success,100));
  for(;;)
  {
    usleep(1000000);
  }
}

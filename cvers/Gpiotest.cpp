#include <stdio.h>
#include <thread>
#include <wiringPi.h>
#include <iostream>
#include <time.h>
#include <unistd.h>
#include <chrono>

#include <iostream>
#include <string>
#include <chrono>
#include <unistd.h>

using namespace std;

typedef chrono::high_resolution_clock TIME;
typedef chrono::milliseconds ms;
typedef chrono::duration<float> timer;
auto tick = TIME::now();
ms tvohundrudms;

void success(int a)
{
  cout << a << endl;
}

void supsuccess()
{
  auto tock = TIME::now();
  mismunur = tock-tick;
  ms milli = chrono::duration_cast<ms>(mismunur);
 if(milli> tvohundrudms)
 {
   thread test(success,0);
   test.detach();
   tick = tock;
 }
}

int main() {
  usleep(200000);
  auto tock = TIME::now();
  timer mismunur = tock-tick;
  tvohundrudms = chrono::duration_cast<ms>(mismunur);
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

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

void success(int a)
{
  cout << a << endl;
}

void supsuccess()
{
  auto tock = TIME::now();
  timer x = t2-t1;
  ms milli = chrono::duration_cast<ms>(x);
 if(milli> 200)
 {
   thread test(success,0);
   test.detach();
   tick = tock;
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

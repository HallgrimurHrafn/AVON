#include <thread>
#include <wiringPi.h>
// #include <chrono>

int main() {
  wiringPiSetupGpio ();

  int pin = 21;
  pinMode(pin, INPUT);
  pullUpDnControl(pin, PUD_UP);
  int wiringPiISR (pin, INT_EDGE_FALLING,  success);



  for(;;)
  {
    usleep(1000000)
  }

}

void success()
{
  cout << "OUTPUT!" << endl;
}

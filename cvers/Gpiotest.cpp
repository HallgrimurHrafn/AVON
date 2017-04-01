#include <pigpio.h>

int main() {
  gpioInitialise();
  gpioSetMode(17, PI_INPUT);
  gpioSetPullUpDown(17, PI_PUD_UP);


  test pin

}
print shit if works

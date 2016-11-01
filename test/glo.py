import time

import Adafruit_Trellis         # trellis config
matrix0 = Adafruit_Trellis.Adafruit_Trellis()
matrix1 = Adafruit_Trellis.Adafruit_Trellis()
matrix2 = Adafruit_Trellis.Adafruit_Trellis()
matrix3 = Adafruit_Trellis.Adafruit_Trellis()
trellis = Adafruit_Trellis.Adafruit_TrellisSet(
    matrix0, matrix1, matrix2, matrix3
    )
I2C_BUS = 1
trellis.begin(
    (0x70,  I2C_BUS),
    (0x71, I2C_BUS),
    (0x72, I2C_BUS),
    (0x73, I2C_BUS)
    )

tester.test(3)

#include <Python.h> 
#include <string>

using namespace std;

void initialize() {
	Py_Initialize();
	PyRun_SimpleString("import sys\n");
	PyRun_SimpleString("sys.path.append(\"/home/pi/AVON/cvers\")\n");
	PyRun_SimpleString("import Adafruit_Trellis\n");
	PyRun_SimpleString("matrix0 = Adafruit_Trellis.Adafruit_Trellis()\n");
	PyRun_SimpleString("matrix1 = Adafruit_Trellis.Adafruit_Trellis()\n");
	PyRun_SimpleString("matrix2 = Adafruit_Trellis.Adafruit_Trellis()\n");
	PyRun_SimpleString("matrix3 = Adafruit_Trellis.Adafruit_Trellis()\n");
	PyRun_SimpleString("trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0, matrix1, matrix2, matrix3)\n");
	PyRun_SimpleString("I2C_BUS = 1\n");
	PyRun_SimpleString("trellis.begin((0x70,  I2C_BUS),(0x71, I2C_BUS),(0x72, I2C_BUS),(0x73, I2C_BUS))\n");
}

void finalise() {
	Py_Finalize();
}

void clrLED(int i){
}

void setLED(int i){
	string s = to_string(i);
	s = "trellis.setLED(" + s +")\n";
	PyRun_SimpleString(s);
}
 
void writeDisplay(){
	PyRun_SimpleString("trellis.writeDisplay()\n");
}

bool readSwitches(){
}

bool justPressed(){
}

bool justReleased(){
}

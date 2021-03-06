#include <Python.h>
#include <string>
#include <iostream>

using namespace std;

void trelliInitialize() {
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
	string s = "trellis.clrLED("+to_string(i)+")\n";
	char const* ch = s.c_str();
	PyRun_SimpleString(ch);
}

void setLED(int i){
	string s = "trellis.setLED("+to_string(i)+")\n";
	char const* ch = s.c_str();
	PyRun_SimpleString(ch);
}

void writeDisplay(){
	PyRun_SimpleString("trellis.writeDisplay()\n");
}

bool pythonCatch(char const* command){
	string stdOutErr =
    "class CatchOutErr:\n\
    def __init__(self):\n\
        self.value = ''\n\
    def write(self, txt):\n\
        self.value += txt\n\
catchOutErr = CatchOutErr()\n\
sys.stdout = catchOutErr\n\
sys.stderr = catchOutErr\n"; //this is python code to redirect stdouts/stderr

	 PyObject *pModule = PyImport_AddModule("__main__"); //create main module
	 PyRun_SimpleString(stdOutErr.c_str()); //invoke code to redirect


	 PyRun_SimpleString(command);
	 PyObject *catcher = PyObject_GetAttrString(pModule,"catchOutErr");

	 PyObject *output = PyObject_GetAttrString(catcher,"value");
	 string out = PyString_AsString(output);
	 out = out.substr(0,4);
	 if (out == "True")
	 		return true;
	 else
	 		return false;
}

bool readSwitches(){
	return pythonCatch("print trellis.readSwitches()\n");
}

bool justPressed(int i){
	string s = "print trellis.justPressed("+to_string(i)+")\n";
	char const* ch = s.c_str();
	return pythonCatch(ch);
}

bool justReleased(int i){
	string s = "print trellis.justReleased("+to_string(i)+")\n";
	char const* ch = s.c_str();
	return pythonCatch(ch);
}

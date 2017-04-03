#include <Python.h>

void initialize() {
	Py_Initialize();
	PyRun_SimpleString("import Adafruit_Trellis\n");
	PyRun_SimpleString("\n");
	PyRun_SimpleString("\n");
	PyRun_SimpleString("\n");
	PyRun_SimpleString("\n");
	PyRun_SimpleString("\n");
	PyRun_SimpleString("\n");
	PyRun_SimpleString("\n");
}

void finalize() {
	Py_Finalize();
}

void clrLed(int i){
}

void setLed(int i){
}

void writeDisplay(){
}

bool readSwitches(){
}

bool justPressed(){
}

bool justReleased(){
}

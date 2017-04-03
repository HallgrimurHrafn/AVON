#ifndef GLOBAL_H
#define GLOBAL_H

#include <time.h>
#include <map>
#include <sting>
#include <chrono>
#include <vector>

using namespace std;

typedef void(*modFunc)(int);
typedef void(*naviFunc)();
typedef map<string,naviFunc> clickmap;
typedef map<const int,modFunc> xmodMap;
typedef map<const int,modFunc> ymodMap;
typedef map<const int,modFunc> zmodMap;
typedef chrono::high_resolution_clock TIME;
typedef chrono::milliseconds ms;
typedef chrono::duration<float> timer; 

extern void fScrollMapX(int,int);
extern void FscorllMapY(int,int);
extern void notes(int);
extern void bPitch(int);
extern void modWheel(int);
extern void changNav1();
extern void changNav2();
extern void changNav4();
extern void customSetup();
extern void customScale(int, int);
void passer(int){cout<<"pass"<<endl;};
// here are all global variables defined. This file has to be included to be able to use all global variables.
// To start they will be split into menu and non menu, just so they can be easily found.
// These come from main.py
// MENU
bool cam = false;					// Is the camera on
bool seen = true;					// Does the camera see the object
int camxyz[3] = {60,64,67};				// Coordinates of the object (x,y,z)
int clear = 0;						// if 1 clear all notes
int live = 0;						// if 1 live mode is on
int pause = 0;						// should we pause?
int stop = 0;						// time to stop?
int newScale[8] = {72,71,69,67,65,64,62,60};		// Scale we are changing to
int Scale[8] = {72,71,69,67,65,64,62,60};		// Current scale
int timi = 500000;					// Time for common use
int synctime = 500000;					// Time for synchronization
int BPM = 120;						// Beats per minute
int FLASH = 0.9;					// Ratio time length for the metronome
int length = 0.1;					// Ratio of time, end to begining of note
int bar = 8;						// 8=1/8 note, 4=1/4 note

// NONMENU
auto tick = TIME::now();
int tapTempo = 1;					// Is the tap tempo active?
int nextChannel = 0;					// What MIDI channel are we changing to
int channel = 0;					// What is the current MIDI channel
bool metroLed = false;					// Is the metronome lights on?
int column = 0;						// What column is playing
int modWatch = 0;					// Are we in Mod Watch
int trellStatus = 1;					// Status changes allowed in Trellis
int mod[8][8][16][8] = {0};				// Info on each note
int status[16][8][8] = {0};				// Status note array
int tStatus[16][8][8] = {0};				// temporary status used when trellStatus = 0
int nowPlaying[8][8] = {0};				// For live mode
vector<double> tap;
vector<double> period;

// These are from other .py files

// ROTARY
int leftTurn[2] = {0};					// Left rotary click
int rightTurn[2] = {0};				// Right rotary click
int state[2] = {0};					// Current state
int prevState[2] = {0};					// Previous state


// Bouncetime timers.
ms hundradms;
auto stopBounce = TIME::now();
auto playBounce = TIME::now();
auto tapBounce = TIME::now();
auto trellisBounce = TIME::now();
auto Rotary1Bounce = TIME::now();
auto Rotary2Bounce = TIME::now();

// FROM GLO
int nav[2] = {0,0};					// Current Navigation state for the menu {x,y}
int oldNav[5] = {0,0,0,0,0};		// Old Navigation state (MEIRA INFO HALLI?)
int cursorxyz[3] = {0,0,0};			// Cursor {x,y,z}
int stat = 1;						// Status?

int editScale = 0;					// edit scale, 1 for custom scale 1, 2 for custom 2 etc...
int note = 60;						// deafult note
int currentScale = 0;				// 0 major, 1 minor, 2 penta, 3-4-5 custom
string pass("pass");
vector <vector<int>> Scales({{note+12,note+11,note+9,note+7,note+5,note+4,note+2,note}, 
							{note+12,note+10,note+8,note+7,note+5,note+3,note+2,note},
							{note+17,note+15,note+12,note+10,note+7,note+5,note+3,note}});		// scales.resize(scales.size()+1,vector<int>(8))
int custom[8] = {60,60,60,60,60,60,60,60};
string p = "pass";
string cursor[5][8] ={{p,p,p,p,p,p,p,p},{p,p,p,p,p,p,p,p},{p,p,p,p,p,p,p,p},
						{p,p,p,p,p,p,p,p},{p,p,p,p,p,p,p,p}};
int cScale[8] = {0};
bool renderLive = true;
bool renderChan = true;


static xmodMap xMod;
static ymodMap yMod;
static zmodMap zMod;
static clickmap cMap
inline xmodMap & xmod(){				// Notkun: xmod().find(mapKey)->second(x)
	xMod[0] = passer;
	xMod[1] = notes;
	xMod[2] = bPitch;
	xMod[3] = modWheel;
	return xMod;
}
inline ymodMap & ymod(){
	yMod[0] = passer;
	yMod[1] = notes;
	yMod[2] = bPitch;
	yMod[3] = modWheel;
	return yMod;
}
inline zmodMap & zmod(){
	zMod[0] = passer;
	zMod[1] = notes;
	zMod[2] = bPitch;
	zMod[3] = modWheel;
	return zMod;
}
inline clickmap & clickMap(){
	string temp;
	for(int i=0;i<8;i++){
		for(int j=0;j<5;j++){
			temp = to_string(i)+to_string(j);
			cMap[temp] = passer;
		}
	}
	cMap["00"] = changNav1;
	cMap["02"] = changNav2;
	cMap["04"] = changNav4;
	cMap["21"] = customSetup;
	return cMap;
}

// Ugly stuff to to create Led show.
int Leds[4][28]  = {0};
int Leds1[4]  = {15,35,48,28,0,0,0,0,0,0,0,0,0,0,0,
														0,0,0,0,0,0,0,0,0,0,0,0,0};
int Leds2[12] = {10,11,14,24,25,34,38,39,29,49,52,
										53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
int Leds3[20] = {5,6,7,9,13,20,21,22,26,27,41,42,
								43,33,34,50,51,56,57,58,0,0,0,0,0,0,0,0};
int Leds4[28] = {0,1,2,3,4,8,12,16,17,18,19,23,24,
								25,44,45,46,47,32,33,34,60,61,62,63,51,52,53};
int ledsNum[4] = {4,12,20,28};
for (int i=0;i<28;i++){ leds[0][i]=Leds1[i]; }
for (int i=0;i<28;i++){ leds[1][i]=Leds2[i]; }
for (int i=0;i<28;i++){ leds[2][i]=Leds3[i]; }
for (int i=0;i<28;i++){ leds[3][i]=Leds4[i]; }


#endif

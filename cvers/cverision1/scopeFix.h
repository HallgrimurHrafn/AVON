#ifndef SCOPE_FIX_H
#define SCOPE_FIX_H


extern void Sequencer();
extern void playColumn(int);
extern void NOTEON(int, bool);
extern void NOTEOFF(int);
extern void metronome(int);
extern void Sync();
extern int TrellisTransf(int);
extern int invTrellisTransf(int);
extern void trellisEventSetup();
extern void trellisWatch();
extern void sequencerSet();
extern void sequencerWatch();
extern void liveSet();
extern void livePlay();
extern void channelChange();
extern void ledshow(int[][]);
extern void ledHelp(int, int[][]);
extern void clearLeds();
extern void PlayPause();
extern void stopper();
extern void Rotary(int, int, int);
extern void Interruption();
extern void trellisPrep();
extern void stopperPrep();
extern void PlayPausePrep();
extern void callbackTapPrep();
extern void clickerPrep1();
extern void clickerPrep2();
extern void rotary1Prep();
extern void rotary2Prep();
extern void clicker(int);
extern void moveUp();
extern void Map(int, int);
extern void channelPrep(int);
extern void tempoChange(int ,int);
extern void liveChange();
extern void cameraChange();
extern void camON();
extern void camOFF();
extern void cameraMode(int, int);
extern void noteLengthChange(int);
extern void barChange(int);
extern void changeScale(int,int);
extern void modScale(int ,int);
extern void createScale();
extern void addScale();
extern void camFunc();
extern void opperate(int);
extern void notes(int);
extern void bPitch(int);
extern void modWheel(int);



#endif

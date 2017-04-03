#ifndef METRO_H
#define METRO_H
#include <vector>
#include <chrono>


using namespace std;
using namespace std::chrono;

typedef high_resolution_clock Clock;

class Metro
{
public:
    Metro(int tempo=120); // if tempo not specified, default = 120
    int getTempo();
    void setTempo(int t);



    /**
     * Usage: callback_tap(channel). runs whenever TAP button pressed.
     * Before: global variable tempo is an integer.
     * After: tempo = average tempo of last three taps.
    **/
    void callbackTap();

    bool tapOK;

private:
    int tempo;	// tempo in beats per minute, formerly BPM

    /**
     * Usage: tempo = calcBPM(tap);
     *
     * Before: tap is a nonempty list of floating point values, representing
     * seconds.
     *
     * After: tempo contains the average bpm between the last two values in tap.
     *
     * @brief calcBPM
     * @param tap
     * @param period
     */
    void calcBPM();

    int getTempoFromPeriod(duration<double> period); // returns tempo in BPM

    vector<Clock::time_point> taps;
    vector<double> tempi; // vector list of tempi to take average of when tapping (*formerly period)


};




#endif // METRO_H

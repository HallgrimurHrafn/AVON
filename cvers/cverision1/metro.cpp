#include "metro.h"
//#include "global.h"
#include <math.h>
#include <time.h>
//#include <map>
#include <chrono>
#include <iostream>




Metro::Metro(int tempo)
{
    setTempo(tempo);
    tapOK = true;

}

int Metro::getTempo()
{
    return tempo;
}

void Metro::setTempo(int t)
{
    tempo = t;
}



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
void Metro::calcBPM() {
    // temp placeholders for temporary period and tempo
    duration<double> p;
    double t;

    // first add the newest tap time to the tap vector.
    auto currentTime = Clock::now();
    taps.push_back(currentTime);

    int tapCount = tempi.size();
    double avgTempo = getTempo();
    if (tapCount==1)
        return;
    else if ((taps.back()-(taps.at(taps.size()-2))>=milliseconds(3000) ||
              (taps.back()-(taps.at(taps.size()-2))<=milliseconds(200))))
    {
        taps.clear(); // too long or too short between taps? reset.
        return;
    }

    else if (tapCount==2) {
        // add a new period (time between taps) but don't adjust tempo.
        p = taps.back()-(taps.at(taps.size()-2));
              cout << "TAP: " << tempi.back() << " bpm" << endl;

        t = getTempoFromPeriod(p);
        tempi.push_back(t);
        cout << "TAP: " << tempi.back() << " bpm" << endl;
        return;
    }

    /**
     * else: # tap_count > 2:
     * add a new period and calculate tempo in bpm.
    **/
    p = taps.back()-(taps.at(taps.size()-2));
    t = getTempoFromPeriod(p);
    tempi.push_back(t);

    if (tapCount == 3) // 3 taps = get avg of two tempi
        avgTempo = (tempi.back()+(tempi.at(tempi.size()-2)))/2;
    else //  (tapCount >= 4) // only get average of last 3
        avgTempo = (tempi.back()+(tempi.at(tempi.size()-2))+(tempi.at(tempi.size()-3)))/3;

    int BPM = round(60/avgTempo);
    setTempo(BPM);
    return;
}

/**
 * Usage: callback_tap(channel). runs whenever TAP button pressed.
 * Before: global variable tempo is an integer.
 * After: tempo = average tempo of last three taps.
**/
void Metro::callbackTap()
{
    if (tapOK==false)
        return;
    else
        calcBPM();
    cout << getTempo() << " bpm" << endl;
}

int Metro::getTempoFromPeriod(duration<double> period)
{
    return round(seconds(60)/period);
}

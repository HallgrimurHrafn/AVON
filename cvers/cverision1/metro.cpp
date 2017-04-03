#include "metro.h"
#include "global.h"

Metro::Metro()
{


}

int Metro::getTempo()
{

}

void Metro::setTempo(int t)
{

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
void Metro::calcBPM(vector<double> tap, vector<double> period)
{
    // þarf að tala við Mr.Karl;
    high_resolution_clock::TIME currentTime = high_resolution_clock::now();

    tap.push_back(currentTime);
    int tapCount = period.size();
    double avgPeriod = 0;
    if(tapCount==1)
        return;
    elseif ((tap.end()-(tap.end()-1))>=3 || (tap.end()-(tap.end()-1))<=0.2)
    {
        tap.erase(period.begin(),period.end()-1);
        return;
    }

    elseif(tapCount==2)
    {
        period.push_back(tap.end()-(tap.end()-1));
        return;
    }
    period.push_back(tap.end()-(tap.end()-1));

    if(tapCount==3)
        avgPeriod = (period.end()+(period.end()-1))/2;
    elseif (tapCount==4)
        avgPeriod = (period.end()+(period.end()-1)+(period.end()-2))/3;
    else
        avgPeriod = (period.end()+(period.end()-1)+2*(period.end()-2))/4;

    BPM = round(60/avgPeriod);
    return;
}

/**
 * Usage: callback_tap(channel). runs whenever TAP button pressed.
 * Before: global variable tempo is an integer.
 * After: tempo = average tempo of last three taps.
**/
void Metro::callbackTap()
{
    if(tapTempo==0)
        return;
    calcBPM(tap,period);
    cout << "BPM: " << BPM << endl;
}

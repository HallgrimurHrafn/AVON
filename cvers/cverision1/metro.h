#ifndef METRO_H
#define METRO_H


class Metro
{
public:
    Metro();
    int getTempo();
    void setTempo(int t);

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
    void calcBPM(vector<double> tap, vector<double> period);

    /**
     * Usage: callback_tap(channel). runs whenever TAP button pressed.
     * Before: global variable tempo is an integer.
     * After: tempo = average tempo of last three taps.
    **/
    void callbackTap();

private:
    int tempo = 120;	// tempo in beats per minute, formerly BPM
};




#endif // METRO_H

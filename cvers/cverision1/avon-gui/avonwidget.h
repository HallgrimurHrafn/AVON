#ifndef AVONWIDGET_H
#define AVONWIDGET_H

#include <QWidget>
#include <iostream>
#include <QButtonGroup>
#include <QFrame>
#include "../metro.h"
#include "../main.h"
using namespace std;

namespace Ui {
class AvonWidget;
}

class AvonWidget : public QWidget
{
    Q_OBJECT
    MainInteractions maini;

public:
    // this sees whether I'm passing the AvonWidget methods for main.h to call.
    explicit AvonWidget(QWidget *parent = 0): maini(*this);
    std::cout << "Outer: " << this << std::endl;

    void highlightFrame(QFrame *myFrame, bool highlighted);
    ~AvonWidget();


    void refreshTempo(Metro &metro);
    void refreshChan();
    void refreshStep();
    void refreshMode();
    void refreshLength();
    void refreshCam();

private slots:
    void on_qButtonTempo_pressed();

    void on_qButtonChan_pressed();

    void on_qButtonPage_pressed();

    void on_qButtonMode_pressed();

    void on_qButtonLength_pressed();

    void on_qButtonCam_pressed();

    /**
     * Show/hide a frame around BPM status based on
     * whether Tempo button is toggled on/off.
     **/
    void on_qButtonTempo_toggled(bool checked);

    /**
     * Show/hide a frame around Channel number based on
     * whether Channel button is toggled on/off.
     **/
    void on_qButtonChan_toggled(bool checked);

private:
    Ui::AvonWidget *ui;
    void setPageNamed(QString pageName);
    void initButtons(QButtonGroup* menuButtons);


};

#endif // AVONWIDGET_H

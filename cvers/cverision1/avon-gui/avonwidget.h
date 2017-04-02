#ifndef AVONWIDGET_H
#define AVONWIDGET_H

#include <QWidget>
#include <iostream>
#include <QButtonGroup>
#include <QLabel>

using namespace std;

namespace Ui {
class AvonWidget;
}

class AvonWidget : public QWidget
{
    Q_OBJECT

public:
    explicit AvonWidget(QWidget *parent = 0);
    void highlightLabel(QLabel *myLabel, bool highlighted);
    ~AvonWidget();

private slots:
    void on_qButtonTempo_pressed();

    void on_qButtonChan_pressed();

    void on_qButtonBar_pressed();

    void on_qButtonMode_pressed();

    void on_qButtonLength_pressed();

    void on_qButtonCam_pressed();

private:
    Ui::AvonWidget *ui;
    void setPageNamed(QString pageName);
};

#endif // AVONWIDGET_H

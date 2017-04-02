#ifndef AVONWIDGET_H
#define AVONWIDGET_H

#include <QWidget>
#include <iostream>
#include <QButtonGroup>

using namespace std;

namespace Ui {
class AvonWidget;
}

class AvonWidget : public QWidget
{
    Q_OBJECT

public:
    explicit AvonWidget(QWidget *parent = 0);
    void highlightBpmVal(bool highlighted);
    ~AvonWidget();

private slots:
    void on_qButtonTempo_pressed();

private:
    Ui::AvonWidget *ui;
    QWidget *getMenuPageNamed(string page);
    void setPageNamed(string pageName);
};

#endif // AVONWIDGET_H

#include "avonwidget.h"
#include <QApplication>
#include "../main.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    AvonWidget w;
    w.show();

    return a.exec();

}

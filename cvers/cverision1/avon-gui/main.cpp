#include "avonwidget.h"
#include <QApplication>
//#include "../global.h"
#include "../main.h"


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    AvonWidget mrBarks;
    mrBarks.show();

    initialize();

    return a.exec();

}

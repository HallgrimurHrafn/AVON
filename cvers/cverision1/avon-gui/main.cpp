#include "avonwidget.h"
#include <QApplication>
//#include "../main.h"

//#include "../global.h"


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    AvonWidget mrBarks;
    mrBarks.show();

    initialize();
    return a.exec();

}

#include "avonwidget.h"
#include "avongui.h"
#include "ui_avonwidget.h"


AvonWidget::AvonWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AvonWidget)
{
    ui->setupUi(this);

    /**
     * Add buttons to a buttonGroup to make them exclusive (like a radio
     * group).
     *
     * @brief menuButtons
     */
    QButtonGroup* menuButtons = new QButtonGroup(this);
    menuButtons->addButton(ui->qButtonBar);
    menuButtons->addButton(ui->qButtonCam);
    menuButtons->addButton(ui->qButtonChan);
    menuButtons->addButton(ui->qButtonLength);
    menuButtons->addButton(ui->qButtonMode);
    menuButtons->addButton(ui->qButtonTempo);


    menuButtons->setExclusive(true);
}

/**
 * Draw a rectangle around bpm value if highlighted = true.
 *
 * @brief AvonWidget::highlightBpmVal
 * @param highlighted = true if rectangle should be drawn around BPM value.
 */
void AvonWidget::highlightBpmVal(bool highlighted)
{
    if (highlighted == true)
        ui->qLabelBpmVal->setFrameStyle(1);
    else
        ui->qLabelBpmVal->setFrameStyle(0);
}

AvonWidget::~AvonWidget()
{
    delete ui;
}


QWidget* AvonWidget::getMenuPageNamed(string page)
{
//    QWidget *q = ui->menuDetails->findChild-><QWidget *>(page);
    string temp = page;
    return ui->menuDetails->findChild<QWidget *>("pageTempo");

}


/**
 * Reveal page within QStackedWidget with name pageName.
 * @brief AvonWidget::setPageNamed
 * @param pageName = name of page to reveal.
 */
void AvonWidget::setPageNamed(string pageName)
{
    QWidget * pageWidget = getMenuPageNamed(pageName);
    ui->menuDetails->setCurrentWidget(pageWidget);
}

/* Activates when tempo menu item is selected. */
void AvonWidget::on_qButtonTempo_pressed()
{
    highlightBpmVal(true);
    setPageNamed("pageTempo");
}




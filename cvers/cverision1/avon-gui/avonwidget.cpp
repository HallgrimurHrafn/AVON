#include "avonwidget.h"
#include "avongui.h"
#include "ui_avonwidget.h"


AvonWidget::AvonWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AvonWidget)
{
    ui->setupUi(this);

    QButtonGroup* menuButtons = new QButtonGroup(this);
    initButtons(menuButtons);

}

/**
 * Add buttons to a buttonGroup to make them exclusive (like a radio
 * group).
 *
 * @brief menuButtons
 */
void AvonWidget::initButtons(QButtonGroup* menuButtons)
{
    menuButtons->addButton(ui->qButtonPage);
    menuButtons->addButton(ui->qButtonCam);
    menuButtons->addButton(ui->qButtonChan);
    menuButtons->addButton(ui->qButtonLength);
    menuButtons->addButton(ui->qButtonMode);
    menuButtons->addButton(ui->qButtonTempo);

    menuButtons->setExclusive(true);

    ui->qButtonTempo->setChecked(true);
    highlightFrame(ui->qBpmFrame);
}

/**
 * Draw a rectangle around bpm value if highlighted = true.
 *
 * @brief AvonWidget::highlightBpmVal
 * @param highlighted = true if rectangle should be drawn around BPM value.
 */
void AvonWidget::highlightFrame(QFrame * myFrame, bool highlighted)
{
    if (highlighted == true)
        myFrame->setFrameStyle(6);
    else
        myFrame->setFrameStyle(0);

}

AvonWidget::~AvonWidget()
{
    delete ui;
}





/**
 * Reveal page within QStackedWidget with name pageName.
 * @brief AvonWidget::setPageNamed
 * @param pageName = name of page to reveal.
 */
void AvonWidget::setPageNamed(QString pageName)
{
    QWidget * pageWidget = ui->menuDetails->findChild<QWidget *>(pageName);

    cout << pageWidget->objectName().toStdString() << endl;
    ui->menuDetails->setCurrentWidget(pageWidget);
}

/* Activates when tempo menu item is selected. */
void AvonWidget::on_qButtonTempo_pressed()
{
    setPageNamed("pageTempo");
}


void AvonWidget::on_qButtonChan_pressed()
{
    setPageNamed("pageChan");
}

void AvonWidget::on_qButtonPage_pressed()
{
    setPageNamed("pageStep");
}

void AvonWidget::on_qButtonMode_pressed()
{
    setPageNamed("pageMode");
}

void AvonWidget::on_qButtonLength_pressed()
{
    setPageNamed("pageLength");
}

void AvonWidget::on_qButtonCam_pressed()
{
    setPageNamed("pageCam");
}


void AvonWidget::on_qButtonTempo_toggled(bool checked)
{
    highlightFrame(ui->qBpmFrame, checked);
}

void AvonWidget::on_qButtonChan_toggled(bool checked)
{
    highlightFrame(ui->qChanFrame, checked);
}

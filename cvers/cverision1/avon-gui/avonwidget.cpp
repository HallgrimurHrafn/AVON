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
void AvonWidget::highlightLabel(QLabel * myLabel, bool highlighted)
{
    if (highlighted == true)
        myLabel->setFrameStyle(1);
    else
        myLabel->setFrameStyle(0);

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
    QLabel * q = ui->qLabelBpmVal;
    highlightLabel(q, true);
    setPageNamed("pageTempo");
}


void AvonWidget::on_qButtonChan_pressed()
{
    QLabel * q = ui->qLabelBpmVal;
    highlightLabel(q, false);
    setPageNamed("pageChan");
}

void AvonWidget::on_qButtonBar_pressed()
{
    QLabel * q = ui->qLabelBpmVal;
    highlightLabel(q, false);
    setPageNamed("pageBar");
}

void AvonWidget::on_qButtonMode_pressed()
{
    QLabel * q = ui->qLabelBpmVal;
    highlightLabel(q, false);
    setPageNamed("pageMode");
}

void AvonWidget::on_qButtonLength_pressed()
{
    QLabel * q = ui->qLabelBpmVal;
    highlightLabel(q, false);
    setPageNamed("pageLength");
}

void AvonWidget::on_qButtonCam_pressed()
{
    QLabel * q = ui->qLabelBpmVal;
    highlightLabel(q, false);
    setPageNamed("pageCam");
}

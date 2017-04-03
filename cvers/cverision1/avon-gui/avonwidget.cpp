#include "avonwidget.h"
#include "ui_avonwidget.h"
#include "../global.h"

//MainInteractions maininteractions;



// Constructor
AvonWidget::AvonWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AvonWidget)
//    maininteractions(*this)

{
    ui->setupUi(this);

    QButtonGroup* menuButtons = new QButtonGroup(this);
    initButtons(menuButtons);
    std::cout << "Outer: " << this << std::endl;
}

/**
 * Add buttons to a buttonGroup to make them exclusive (like a radio
 * group).
 *
 * @brief menuButtons
 */
void AvonWidget::initButtons(QButtonGroup* menuButtons)
{
    menuButtons->addButton(ui->qButtonStep);
    menuButtons->addButton(ui->qButtonCam);
    menuButtons->addButton(ui->qButtonChan);
    menuButtons->addButton(ui->qButtonLength);
    menuButtons->addButton(ui->qButtonMode);
    menuButtons->addButton(ui->qButtonTempo);

    menuButtons->setExclusive(true);

    ui->menuDetails->setCurrentIndex(0);
    ui->qButtonTempo->setChecked(true);
    highlightFrame(ui->qBpmFrame, true);
}

/**
 * Display current tempo on screen.
 * @todo check that it's properly using the real metro!
 *
 * @brief AvonWidget::refreshTempo
 * @param metro
 */
void AvonWidget::refreshTempo(Metro &metro)
{
    QString s = QString::number(metro.getTempo());
    ui->qLabelBpmVal->setText(s);
}

/**
 * Update channel number on screen.
 * @brief AvonWidget::refreshChan
 */
void AvonWidget::refreshChan()
{
    QString s = QString::number(channel);
}

/**
 * Update sequencer step size on screen.
 * @brief AvonWidget::refreshStep
 */
void AvonWidget::refreshStep()
{
    switch(bar) {
        case 4  : ui->qStepBox->setCurrentText("1/4 note");
        case 8  : ui->qStepBox->setCurrentText("1/8 note");
    }
}

/**
 * Update mode on screen.
 * @brief AvonWidget::refreshMode
 */
void AvonWidget::refreshMode()
{
    switch(live) {
        case 0  : {
            ui->qModePage->setCurrentIndex(0);
            ui->qButtonMode->setText("Sequencer");
        }
        case 1  : {
            ui->qModePage->setCurrentIndex(1);
            ui->qButtonMode->setText("Live Mode");
        }
    }
}

/**
 * Update note length/sustain on screen.
 * @brief AvonWidget::refreshLength
 */
void AvonWidget::refreshLength()
{
    ui->qLengthBar->setValue(100*length);
}

/**
 * Update camera status on screen.
 * @brief AvonWidget::refreshCam
 */
void AvonWidget::refreshCam()
{
    int ind = (int)cam;
    ui->qCamBox->setCurrentIndex(ind);
    if (cam)
        ui->qButtonCam->setText("Camera: ON");
    else
        ui->qButtonCam->setText("Camera: OFF");
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

void AvonWidget::on_qButtonStep_pressed()
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

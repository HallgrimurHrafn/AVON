/********************************************************************************
** Form generated from reading UI file 'avonwidget.ui'
**
** Created by: Qt User Interface Compiler version 5.3.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AVONWIDGET_H
#define UI_AVONWIDGET_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_AvonWidget
{
public:
    QWidget *layoutWidget;
    QHBoxLayout *qLayoutAll;
    QGroupBox *menuBar;
    QVBoxLayout *verticalLayout;
    QPushButton *qButtonTempo;
    QPushButton *qButtonChan;
    QPushButton *qButtonStep;
    QPushButton *qButtonMode;
    QPushButton *qButtonLength;
    QPushButton *qButtonCam;
    QVBoxLayout *qLayoutRight;
    QFrame *statusBar;
    QHBoxLayout *horizontalLayout;
    QFrame *qBpmFrame;
    QHBoxLayout *horizontalLayout_2;
    QLabel *qLabelBpmVal;
    QLabel *qLabelBpm;
    QFrame *qChanFrame;
    QHBoxLayout *horizontalLayout_3;
    QLabel *qLabelChan;
    QLabel *qLabelChanVal;
    QStackedWidget *menuDetails;
    QWidget *pageTempo;
    QWidget *pageChan;
    QWidget *pageStep;
    QWidget *layoutWidget1;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label;
    QComboBox *qStepBox;
    QPlainTextEdit *plainTextEdit;
    QWidget *pageMode;
    QVBoxLayout *verticalLayout_3;
    QStackedWidget *qModePage;
    QWidget *qModePageSeq;
    QTextEdit *qTextSeq;
    QWidget *qModePageLive;
    QTextEdit *qTextLive;
    QWidget *pageLength;
    QWidget *layoutWidget2;
    QVBoxLayout *verticalLayout_4;
    QPlainTextEdit *plainTextEdit_2;
    QProgressBar *qLengthBar;
    QWidget *pageCam;
    QComboBox *qCamBox;
    QLabel *label_3;

    void setupUi(QWidget *AvonWidget)
    {
        if (AvonWidget->objectName().isEmpty())
            AvonWidget->setObjectName(QStringLiteral("AvonWidget"));
        AvonWidget->resize(320, 240);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(AvonWidget->sizePolicy().hasHeightForWidth());
        AvonWidget->setSizePolicy(sizePolicy);
        AvonWidget->setMinimumSize(QSize(320, 240));
        AvonWidget->setMaximumSize(QSize(320, 240));
        QFont font;
        font.setFamily(QStringLiteral("Menlo"));
        font.setPointSize(12);
        AvonWidget->setFont(font);
        AvonWidget->setLocale(QLocale(QLocale::English, QLocale::UnitedStates));
        layoutWidget = new QWidget(AvonWidget);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(0, 0, 321, 241));
        qLayoutAll = new QHBoxLayout(layoutWidget);
        qLayoutAll->setSpacing(0);
        qLayoutAll->setContentsMargins(11, 11, 11, 11);
        qLayoutAll->setObjectName(QStringLiteral("qLayoutAll"));
        qLayoutAll->setSizeConstraint(QLayout::SetMinAndMaxSize);
        qLayoutAll->setContentsMargins(0, 0, 0, 0);
        menuBar = new QGroupBox(layoutWidget);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setEnabled(true);
        sizePolicy.setHeightForWidth(menuBar->sizePolicy().hasHeightForWidth());
        menuBar->setSizePolicy(sizePolicy);
        menuBar->setMinimumSize(QSize(120, 0));
        menuBar->setMaximumSize(QSize(120, 240));
        menuBar->setBaseSize(QSize(120, 0));
        QFont font1;
        font1.setFamily(QStringLiteral("Menlo"));
        menuBar->setFont(font1);
        menuBar->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        menuBar->setFlat(true);
        menuBar->setCheckable(false);
        menuBar->setChecked(false);
        verticalLayout = new QVBoxLayout(menuBar);
        verticalLayout->setSpacing(0);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        qButtonTempo = new QPushButton(menuBar);
        qButtonTempo->setObjectName(QStringLiteral("qButtonTempo"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(qButtonTempo->sizePolicy().hasHeightForWidth());
        qButtonTempo->setSizePolicy(sizePolicy1);
        qButtonTempo->setMaximumSize(QSize(16777215, 50));
        qButtonTempo->setFont(font1);
        qButtonTempo->setCheckable(true);
        qButtonTempo->setChecked(false);
        qButtonTempo->setAutoRepeat(false);
        qButtonTempo->setAutoExclusive(false);
        qButtonTempo->setDefault(false);
        qButtonTempo->setFlat(false);

        verticalLayout->addWidget(qButtonTempo);

        qButtonChan = new QPushButton(menuBar);
        qButtonChan->setObjectName(QStringLiteral("qButtonChan"));
        sizePolicy1.setHeightForWidth(qButtonChan->sizePolicy().hasHeightForWidth());
        qButtonChan->setSizePolicy(sizePolicy1);
        qButtonChan->setMaximumSize(QSize(16777215, 50));
        qButtonChan->setFont(font1);
        qButtonChan->setCheckable(true);
        qButtonChan->setChecked(false);
        qButtonChan->setAutoRepeat(false);
        qButtonChan->setAutoExclusive(false);
        qButtonChan->setFlat(false);

        verticalLayout->addWidget(qButtonChan);

        qButtonStep = new QPushButton(menuBar);
        qButtonStep->setObjectName(QStringLiteral("qButtonStep"));
        sizePolicy1.setHeightForWidth(qButtonStep->sizePolicy().hasHeightForWidth());
        qButtonStep->setSizePolicy(sizePolicy1);
        qButtonStep->setMaximumSize(QSize(16777215, 50));
        qButtonStep->setFont(font1);
        qButtonStep->setCheckable(true);
        qButtonStep->setChecked(false);
        qButtonStep->setAutoRepeat(false);
        qButtonStep->setAutoExclusive(false);
        qButtonStep->setFlat(false);

        verticalLayout->addWidget(qButtonStep);

        qButtonMode = new QPushButton(menuBar);
        qButtonMode->setObjectName(QStringLiteral("qButtonMode"));
        sizePolicy1.setHeightForWidth(qButtonMode->sizePolicy().hasHeightForWidth());
        qButtonMode->setSizePolicy(sizePolicy1);
        qButtonMode->setMaximumSize(QSize(16777215, 50));
        qButtonMode->setFont(font1);
        qButtonMode->setCheckable(true);
        qButtonMode->setChecked(false);
        qButtonMode->setAutoRepeat(false);
        qButtonMode->setAutoExclusive(false);
        qButtonMode->setFlat(false);

        verticalLayout->addWidget(qButtonMode);

        qButtonLength = new QPushButton(menuBar);
        qButtonLength->setObjectName(QStringLiteral("qButtonLength"));
        sizePolicy1.setHeightForWidth(qButtonLength->sizePolicy().hasHeightForWidth());
        qButtonLength->setSizePolicy(sizePolicy1);
        qButtonLength->setMaximumSize(QSize(16777215, 50));
        qButtonLength->setFont(font1);
        qButtonLength->setCheckable(true);
        qButtonLength->setChecked(false);
        qButtonLength->setAutoRepeat(false);
        qButtonLength->setAutoExclusive(false);
        qButtonLength->setFlat(false);

        verticalLayout->addWidget(qButtonLength);

        qButtonCam = new QPushButton(menuBar);
        qButtonCam->setObjectName(QStringLiteral("qButtonCam"));
        sizePolicy1.setHeightForWidth(qButtonCam->sizePolicy().hasHeightForWidth());
        qButtonCam->setSizePolicy(sizePolicy1);
        qButtonCam->setMaximumSize(QSize(16777215, 50));
        qButtonCam->setFont(font1);
        qButtonCam->setCheckable(true);
        qButtonCam->setChecked(false);
        qButtonCam->setAutoRepeat(false);
        qButtonCam->setAutoExclusive(false);
        qButtonCam->setFlat(false);

        verticalLayout->addWidget(qButtonCam);


        qLayoutAll->addWidget(menuBar);

        qLayoutRight = new QVBoxLayout();
        qLayoutRight->setSpacing(6);
        qLayoutRight->setObjectName(QStringLiteral("qLayoutRight"));
        qLayoutRight->setSizeConstraint(QLayout::SetMinAndMaxSize);
        statusBar = new QFrame(layoutWidget);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Maximum);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(statusBar->sizePolicy().hasHeightForWidth());
        statusBar->setSizePolicy(sizePolicy2);
        statusBar->setMinimumSize(QSize(100, 41));
        statusBar->setMaximumSize(QSize(16777215, 41));
        statusBar->setFrameShape(QFrame::NoFrame);
        statusBar->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(statusBar);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 8, 6, 0);
        qBpmFrame = new QFrame(statusBar);
        qBpmFrame->setObjectName(QStringLiteral("qBpmFrame"));
        QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Preferred);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(qBpmFrame->sizePolicy().hasHeightForWidth());
        qBpmFrame->setSizePolicy(sizePolicy3);
        qBpmFrame->setMinimumSize(QSize(86, 0));
        qBpmFrame->setMaximumSize(QSize(86, 16777215));
        qBpmFrame->setFrameShape(QFrame::NoFrame);
        qBpmFrame->setFrameShadow(QFrame::Plain);
        horizontalLayout_2 = new QHBoxLayout(qBpmFrame);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        qLabelBpmVal = new QLabel(qBpmFrame);
        qLabelBpmVal->setObjectName(QStringLiteral("qLabelBpmVal"));
        qLabelBpmVal->setFont(font1);
        qLabelBpmVal->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_2->addWidget(qLabelBpmVal);

        qLabelBpm = new QLabel(qBpmFrame);
        qLabelBpm->setObjectName(QStringLiteral("qLabelBpm"));
        qLabelBpm->setFont(font1);

        horizontalLayout_2->addWidget(qLabelBpm);

        qLabelBpm->raise();
        qLabelBpmVal->raise();

        horizontalLayout->addWidget(qBpmFrame);

        qChanFrame = new QFrame(statusBar);
        qChanFrame->setObjectName(QStringLiteral("qChanFrame"));
        sizePolicy3.setHeightForWidth(qChanFrame->sizePolicy().hasHeightForWidth());
        qChanFrame->setSizePolicy(sizePolicy3);
        qChanFrame->setMinimumSize(QSize(90, 0));
        qChanFrame->setMaximumSize(QSize(90, 16777215));
        qChanFrame->setFrameShape(QFrame::NoFrame);
        qChanFrame->setFrameShadow(QFrame::Plain);
        horizontalLayout_3 = new QHBoxLayout(qChanFrame);
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        qLabelChan = new QLabel(qChanFrame);
        qLabelChan->setObjectName(QStringLiteral("qLabelChan"));
        QSizePolicy sizePolicy4(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(qLabelChan->sizePolicy().hasHeightForWidth());
        qLabelChan->setSizePolicy(sizePolicy4);
        qLabelChan->setMinimumSize(QSize(63, 0));
        qLabelChan->setMaximumSize(QSize(63, 16777215));
        qLabelChan->setFont(font1);
        qLabelChan->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_3->addWidget(qLabelChan);

        qLabelChanVal = new QLabel(qChanFrame);
        qLabelChanVal->setObjectName(QStringLiteral("qLabelChanVal"));
        sizePolicy4.setHeightForWidth(qLabelChanVal->sizePolicy().hasHeightForWidth());
        qLabelChanVal->setSizePolicy(sizePolicy4);
        qLabelChanVal->setMinimumSize(QSize(18, 0));
        qLabelChanVal->setMaximumSize(QSize(18, 16777215));
        qLabelChanVal->setSizeIncrement(QSize(0, 0));
        qLabelChanVal->setBaseSize(QSize(0, 0));
        qLabelChanVal->setFont(font1);

        horizontalLayout_3->addWidget(qLabelChanVal);


        horizontalLayout->addWidget(qChanFrame);


        qLayoutRight->addWidget(statusBar);

        menuDetails = new QStackedWidget(layoutWidget);
        menuDetails->setObjectName(QStringLiteral("menuDetails"));
        pageTempo = new QWidget();
        pageTempo->setObjectName(QStringLiteral("pageTempo"));
        menuDetails->addWidget(pageTempo);
        pageChan = new QWidget();
        pageChan->setObjectName(QStringLiteral("pageChan"));
        menuDetails->addWidget(pageChan);
        pageStep = new QWidget();
        pageStep->setObjectName(QStringLiteral("pageStep"));
        layoutWidget1 = new QWidget(pageStep);
        layoutWidget1->setObjectName(QStringLiteral("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(0, 40, 193, 141));
        verticalLayout_2 = new QVBoxLayout(layoutWidget1);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        label = new QLabel(layoutWidget1);
        label->setObjectName(QStringLiteral("label"));
        QFont font2;
        font2.setFamily(QStringLiteral("Menlo"));
        font2.setPointSize(12);
        font2.setBold(true);
        font2.setWeight(75);
        label->setFont(font2);

        horizontalLayout_4->addWidget(label);

        qStepBox = new QComboBox(layoutWidget1);
        qStepBox->setObjectName(QStringLiteral("qStepBox"));
        QFont font3;
        font3.setBold(false);
        font3.setWeight(50);
        qStepBox->setFont(font3);

        horizontalLayout_4->addWidget(qStepBox);


        verticalLayout_2->addLayout(horizontalLayout_4);

        plainTextEdit = new QPlainTextEdit(layoutWidget1);
        plainTextEdit->setObjectName(QStringLiteral("plainTextEdit"));
        plainTextEdit->setEnabled(false);
        plainTextEdit->setAutoFillBackground(true);
        plainTextEdit->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        plainTextEdit->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        plainTextEdit->setUndoRedoEnabled(true);
        plainTextEdit->setReadOnly(true);

        verticalLayout_2->addWidget(plainTextEdit);

        menuDetails->addWidget(pageStep);
        pageMode = new QWidget();
        pageMode->setObjectName(QStringLiteral("pageMode"));
        verticalLayout_3 = new QVBoxLayout(pageMode);
        verticalLayout_3->setSpacing(0);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        qModePage = new QStackedWidget(pageMode);
        qModePage->setObjectName(QStringLiteral("qModePage"));
        qModePageSeq = new QWidget();
        qModePageSeq->setObjectName(QStringLiteral("qModePageSeq"));
        qTextSeq = new QTextEdit(qModePageSeq);
        qTextSeq->setObjectName(QStringLiteral("qTextSeq"));
        qTextSeq->setEnabled(false);
        qTextSeq->setGeometry(QRect(0, 70, 191, 111));
        qTextSeq->setAutoFillBackground(true);
        qTextSeq->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        qTextSeq->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        qTextSeq->setReadOnly(true);
        qModePage->addWidget(qModePageSeq);
        qModePageLive = new QWidget();
        qModePageLive->setObjectName(QStringLiteral("qModePageLive"));
        qTextLive = new QTextEdit(qModePageLive);
        qTextLive->setObjectName(QStringLiteral("qTextLive"));
        qTextLive->setEnabled(false);
        qTextLive->setGeometry(QRect(0, 70, 191, 111));
        qTextLive->setAutoFillBackground(true);
        qTextLive->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        qTextLive->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        qTextLive->setReadOnly(true);
        qModePage->addWidget(qModePageLive);

        verticalLayout_3->addWidget(qModePage);

        menuDetails->addWidget(pageMode);
        pageLength = new QWidget();
        pageLength->setObjectName(QStringLiteral("pageLength"));
        layoutWidget2 = new QWidget(pageLength);
        layoutWidget2->setObjectName(QStringLiteral("layoutWidget2"));
        layoutWidget2->setGeometry(QRect(0, 0, 191, 141));
        verticalLayout_4 = new QVBoxLayout(layoutWidget2);
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setContentsMargins(11, 11, 11, 11);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        plainTextEdit_2 = new QPlainTextEdit(layoutWidget2);
        plainTextEdit_2->setObjectName(QStringLiteral("plainTextEdit_2"));
        plainTextEdit_2->setEnabled(false);
        plainTextEdit_2->setMinimumSize(QSize(0, 100));
        plainTextEdit_2->setMaximumSize(QSize(16777215, 100));
        plainTextEdit_2->setSizeIncrement(QSize(0, 100));
        QFont font4;
        font4.setPointSize(11);
        plainTextEdit_2->setFont(font4);
        plainTextEdit_2->setAutoFillBackground(true);
        plainTextEdit_2->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        plainTextEdit_2->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        plainTextEdit_2->setUndoRedoEnabled(true);
        plainTextEdit_2->setReadOnly(true);

        verticalLayout_4->addWidget(plainTextEdit_2);

        qLengthBar = new QProgressBar(layoutWidget2);
        qLengthBar->setObjectName(QStringLiteral("qLengthBar"));
        QSizePolicy sizePolicy5(QSizePolicy::Expanding, QSizePolicy::Preferred);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(qLengthBar->sizePolicy().hasHeightForWidth());
        qLengthBar->setSizePolicy(sizePolicy5);
        qLengthBar->setMinimumSize(QSize(0, 20));
        qLengthBar->setMaximumSize(QSize(16777215, 20));
        qLengthBar->setSizeIncrement(QSize(0, 20));
        qLengthBar->setBaseSize(QSize(0, 20));
        qLengthBar->setAutoFillBackground(true);
        qLengthBar->setMinimum(1);
        qLengthBar->setValue(100);
        qLengthBar->setAlignment(Qt::AlignCenter);
        qLengthBar->setTextVisible(true);
        qLengthBar->setInvertedAppearance(false);

        verticalLayout_4->addWidget(qLengthBar);

        menuDetails->addWidget(pageLength);
        pageCam = new QWidget();
        pageCam->setObjectName(QStringLiteral("pageCam"));
        qCamBox = new QComboBox(pageCam);
        qCamBox->setObjectName(QStringLiteral("qCamBox"));
        qCamBox->setGeometry(QRect(50, 50, 101, 91));
        QFont font5;
        font5.setPointSize(24);
        font5.setBold(false);
        font5.setWeight(50);
        qCamBox->setFont(font5);
        qCamBox->setAutoFillBackground(false);
        qCamBox->setFrame(true);
        label_3 = new QLabel(pageCam);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(40, 20, 121, 31));
        label_3->setFont(font2);
        label_3->setAlignment(Qt::AlignCenter);
        menuDetails->addWidget(pageCam);

        qLayoutRight->addWidget(menuDetails);


        qLayoutAll->addLayout(qLayoutRight);

        qLayoutAll->setStretch(0, 320);
        qLayoutAll->setStretch(1, 240);

        retranslateUi(AvonWidget);

        menuDetails->setCurrentIndex(0);
        qStepBox->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(AvonWidget);
    } // setupUi

    void retranslateUi(QWidget *AvonWidget)
    {
        AvonWidget->setWindowTitle(QApplication::translate("AvonWidget", "AvonWidget", 0));
        menuBar->setTitle(QString());
        qButtonTempo->setText(QApplication::translate("AvonWidget", "Tempo", 0));
        qButtonChan->setText(QApplication::translate("AvonWidget", "Channel", 0));
        qButtonStep->setText(QApplication::translate("AvonWidget", "Step: 1/8", 0));
        qButtonMode->setText(QApplication::translate("AvonWidget", "Sequencer", 0));
        qButtonLength->setText(QApplication::translate("AvonWidget", "Note Length", 0));
        qButtonCam->setText(QApplication::translate("AvonWidget", "Camera OFF", 0));
        qLabelBpmVal->setText(QApplication::translate("AvonWidget", "120", 0));
        qLabelBpm->setText(QApplication::translate("AvonWidget", "bpm", 0));
        qLabelChan->setText(QApplication::translate("AvonWidget", "Channel", 0));
        qLabelChanVal->setText(QApplication::translate("AvonWidget", "1", 0));
        label->setText(QApplication::translate("AvonWidget", "Step Size:", 0));
        qStepBox->clear();
        qStepBox->insertItems(0, QStringList()
         << QApplication::translate("AvonWidget", "1/4 note", 0)
         << QApplication::translate("AvonWidget", "1/8 note", 0)
        );
        plainTextEdit->setPlainText(QApplication::translate("AvonWidget", "The duration represented by each column of the sequencer grid.", 0));
        qTextSeq->setHtml(QApplication::translate("AvonWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Menlo'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In <span style=\" font-weight:600;\">Sequencer Mode </span>(Default) the grid represents a repeating pattern of notes played in a series.  </p></body></html>", 0));
        qTextLive->setHtml(QApplication::translate("AvonWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Menlo'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In <span style=\" font-weight:600;\">Live Mode</span>. each button on the grid can be pressed to trigger a note on an external instrument.</p></body></html>", 0));
        plainTextEdit_2->setPlainText(QApplication::translate("AvonWidget", "The percentage of the time a note is held before it is released. For example, 100% represents a note held until the moment the next one begins (legato). ", 0));
        qCamBox->clear();
        qCamBox->insertItems(0, QStringList()
         << QApplication::translate("AvonWidget", "OFF", 0)
         << QApplication::translate("AvonWidget", "ON", 0)
        );
        label_3->setText(QApplication::translate("AvonWidget", "Camera Status:", 0));
    } // retranslateUi

};

namespace Ui {
    class AvonWidget: public Ui_AvonWidget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AVONWIDGET_H

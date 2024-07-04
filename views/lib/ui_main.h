/********************************************************************************
** Form generated from reading UI file 'mainFEJpnv.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAINFEJPNV_H
#define MAINFEJPNV_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QWidget *gridLayoutWidget_3;
    QGridLayout *gridLayout_function;
    QGridLayout *gridLayout_param;
    QPushButton *pushButton_scan_ip;
    QGridLayout *gridLayout_param_input;
    QLineEdit *lineEdit_10;
    QLineEdit *lineEdit_9;
    QLabel *label_52;
    QLabel *label_51;
    QLabel *label_53;
    QLineEdit *lineEdit_8;
    QLineEdit *lineEdit_11;
    QLabel *label_50;
    QPushButton *pushButton_save;
    QLabel *label_param_area;
    QGridLayout *gridLayout_operate;
    QCheckBox *checkBox_all_ip;
    QPushButton *pushButton_add;
    QProgressBar *progressBar_transform;
    QPushButton *pushButton_send;
    QPushButton *pushButton_delete;
    QPushButton *pushButton_zip;
    QLabel *label_operate_area;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QHBoxLayout *horizontalLayout;
    QTextEdit *textEdit_log;
    QListWidget *listWidget_file;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(814, 396);
        MainWindow->setMinimumSize(QSize(0, 0));
        QIcon icon;
        icon.addFile(QString::fromUtf8("logo.png"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindow->setWindowIcon(icon);
        MainWindow->setLocale(QLocale(QLocale::Chinese, QLocale::China));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayoutWidget_3 = new QWidget(centralwidget);
        gridLayoutWidget_3->setObjectName(QString::fromUtf8("gridLayoutWidget_3"));
        gridLayoutWidget_3->setGeometry(QRect(430, 10, 371, 361));
        gridLayout_function = new QGridLayout(gridLayoutWidget_3);
        gridLayout_function->setObjectName(QString::fromUtf8("gridLayout_function"));
        gridLayout_function->setContentsMargins(0, 0, 0, 0);
        gridLayout_param = new QGridLayout();
        gridLayout_param->setObjectName(QString::fromUtf8("gridLayout_param"));
        pushButton_scan_ip = new QPushButton(gridLayoutWidget_3);
        pushButton_scan_ip->setObjectName(QString::fromUtf8("pushButton_scan_ip"));

        gridLayout_param->addWidget(pushButton_scan_ip, 1, 0, 1, 1);

        gridLayout_param_input = new QGridLayout();
        gridLayout_param_input->setObjectName(QString::fromUtf8("gridLayout_param_input"));
        lineEdit_10 = new QLineEdit(gridLayoutWidget_3);
        lineEdit_10->setObjectName(QString::fromUtf8("lineEdit_10"));

        gridLayout_param_input->addWidget(lineEdit_10, 1, 1, 1, 1);

        lineEdit_9 = new QLineEdit(gridLayoutWidget_3);
        lineEdit_9->setObjectName(QString::fromUtf8("lineEdit_9"));

        gridLayout_param_input->addWidget(lineEdit_9, 3, 1, 1, 1);

        label_52 = new QLabel(gridLayoutWidget_3);
        label_52->setObjectName(QString::fromUtf8("label_52"));
        label_52->setLayoutDirection(Qt::LeftToRight);
        label_52->setAlignment(Qt::AlignCenter);

        gridLayout_param_input->addWidget(label_52, 3, 0, 1, 1);

        label_51 = new QLabel(gridLayoutWidget_3);
        label_51->setObjectName(QString::fromUtf8("label_51"));
        label_51->setLayoutDirection(Qt::LeftToRight);
        label_51->setAlignment(Qt::AlignCenter);

        gridLayout_param_input->addWidget(label_51, 1, 0, 1, 1);

        label_53 = new QLabel(gridLayoutWidget_3);
        label_53->setObjectName(QString::fromUtf8("label_53"));
        label_53->setAlignment(Qt::AlignCenter);

        gridLayout_param_input->addWidget(label_53, 2, 0, 1, 1);

        lineEdit_8 = new QLineEdit(gridLayoutWidget_3);
        lineEdit_8->setObjectName(QString::fromUtf8("lineEdit_8"));

        gridLayout_param_input->addWidget(lineEdit_8, 2, 1, 1, 1);

        lineEdit_11 = new QLineEdit(gridLayoutWidget_3);
        lineEdit_11->setObjectName(QString::fromUtf8("lineEdit_11"));

        gridLayout_param_input->addWidget(lineEdit_11, 0, 1, 1, 1);

        label_50 = new QLabel(gridLayoutWidget_3);
        label_50->setObjectName(QString::fromUtf8("label_50"));

        gridLayout_param_input->addWidget(label_50, 0, 0, 1, 1);


        gridLayout_param->addLayout(gridLayout_param_input, 0, 0, 1, 2);

        pushButton_save = new QPushButton(gridLayoutWidget_3);
        pushButton_save->setObjectName(QString::fromUtf8("pushButton_save"));

        gridLayout_param->addWidget(pushButton_save, 1, 1, 1, 1);


        gridLayout_function->addLayout(gridLayout_param, 5, 1, 1, 2);

        label_param_area = new QLabel(gridLayoutWidget_3);
        label_param_area->setObjectName(QString::fromUtf8("label_param_area"));
        label_param_area->setLineWidth(1);
        label_param_area->setTextFormat(Qt::AutoText);
        label_param_area->setScaledContents(false);
        label_param_area->setAlignment(Qt::AlignCenter);

        gridLayout_function->addWidget(label_param_area, 0, 1, 1, 2);

        gridLayout_operate = new QGridLayout();
        gridLayout_operate->setObjectName(QString::fromUtf8("gridLayout_operate"));
        checkBox_all_ip = new QCheckBox(gridLayoutWidget_3);
        checkBox_all_ip->setObjectName(QString::fromUtf8("checkBox_all_ip"));
        checkBox_all_ip->setLayoutDirection(Qt::LeftToRight);
        checkBox_all_ip->setAutoExclusive(false);

        gridLayout_operate->addWidget(checkBox_all_ip, 3, 0, 1, 1);

        pushButton_add = new QPushButton(gridLayoutWidget_3);
        pushButton_add->setObjectName(QString::fromUtf8("pushButton_add"));

        gridLayout_operate->addWidget(pushButton_add, 0, 0, 1, 1);

        progressBar_transform = new QProgressBar(gridLayoutWidget_3);
        progressBar_transform->setObjectName(QString::fromUtf8("progressBar_transform"));
        progressBar_transform->setValue(24);

        gridLayout_operate->addWidget(progressBar_transform, 3, 1, 1, 1);

        pushButton_send = new QPushButton(gridLayoutWidget_3);
        pushButton_send->setObjectName(QString::fromUtf8("pushButton_send"));

        gridLayout_operate->addWidget(pushButton_send, 2, 1, 1, 1);

        pushButton_delete = new QPushButton(gridLayoutWidget_3);
        pushButton_delete->setObjectName(QString::fromUtf8("pushButton_delete"));

        gridLayout_operate->addWidget(pushButton_delete, 2, 0, 1, 1);

        pushButton_zip = new QPushButton(gridLayoutWidget_3);
        pushButton_zip->setObjectName(QString::fromUtf8("pushButton_zip"));

        gridLayout_operate->addWidget(pushButton_zip, 0, 1, 1, 1);


        gridLayout_function->addLayout(gridLayout_operate, 7, 1, 1, 2);

        label_operate_area = new QLabel(gridLayoutWidget_3);
        label_operate_area->setObjectName(QString::fromUtf8("label_operate_area"));
        label_operate_area->setLineWidth(1);
        label_operate_area->setTextFormat(Qt::AutoText);
        label_operate_area->setScaledContents(false);
        label_operate_area->setAlignment(Qt::AlignCenter);

        gridLayout_function->addWidget(label_operate_area, 6, 1, 1, 2);

        scrollArea = new QScrollArea(centralwidget);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setGeometry(QRect(10, 210, 411, 161));
        scrollArea->setMinimumSize(QSize(100, 17));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 409, 159));
        horizontalLayout = new QHBoxLayout(scrollAreaWidgetContents);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        textEdit_log = new QTextEdit(scrollAreaWidgetContents);
        textEdit_log->setObjectName(QString::fromUtf8("textEdit_log"));

        horizontalLayout->addWidget(textEdit_log);

        scrollArea->setWidget(scrollAreaWidgetContents);
        listWidget_file = new QListWidget(centralwidget);
        listWidget_file->setObjectName(QString::fromUtf8("listWidget_file"));
        listWidget_file->setGeometry(QRect(10, 10, 411, 191));
        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "\345\261\200\345\237\237\347\275\221\346\226\207\344\273\266\344\274\240\350\276\223\345\212\251\345\212\251\346\211\213  \345\242\236\345\274\272\347\211\210", nullptr));
        pushButton_scan_ip->setText(QApplication::translate("MainWindow", "IP\346\211\253\346\217\217", nullptr));
        lineEdit_10->setPlaceholderText(QApplication::translate("MainWindow", "\350\257\267\350\276\223\345\205\245\344\270\273\346\234\272\347\253\257\347\231\273\345\275\225\345\257\206\347\240\201\357\274\214\351\273\230\350\256\244\344\270\272ros", nullptr));
        lineEdit_9->setPlaceholderText(QApplication::translate("MainWindow", "\350\257\267\350\276\223\345\205\245IP \347\275\221\346\256\265\357\274\214\345\246\202192.168.0.0/255", nullptr));
        label_52->setText(QApplication::translate("MainWindow", "IP \347\275\221\346\256\265", nullptr));
        label_51->setText(QApplication::translate("MainWindow", "\344\270\273\346\234\272\345\257\206\347\240\201", nullptr));
        label_53->setText(QApplication::translate("MainWindow", "\344\274\240\350\276\223\350\267\257\345\276\204", nullptr));
        lineEdit_8->setPlaceholderText(QApplication::translate("MainWindow", "\350\257\267\350\276\223\345\205\245\344\274\240\350\276\223\345\210\260\344\270\273\346\234\272\347\232\204\350\267\257\345\276\204", nullptr));
        lineEdit_11->setPlaceholderText(QApplication::translate("MainWindow", "\350\257\267\350\276\223\345\205\245\344\270\273\346\234\272\347\253\257\347\231\273\345\275\225\347\224\250\346\210\267\345\220\215\357\274\214\351\273\230\350\256\244\344\270\272tianbot", nullptr));
        label_50->setText(QApplication::translate("MainWindow", "\344\270\273\346\234\272\347\224\250\346\210\267\345\220\215", nullptr));
        pushButton_save->setText(QApplication::translate("MainWindow", "\344\277\235\345\255\230", nullptr));
        label_param_area->setText(QApplication::translate("MainWindow", "\345\217\202\346\225\260\351\205\215\347\275\256\345\214\272", nullptr));
        label_param_area->setProperty("class", QVariant(QApplication::translate("MainWindow", "h2", nullptr)));
        checkBox_all_ip->setText(QApplication::translate("MainWindow", "IP\345\205\250\351\200\211", nullptr));
        pushButton_add->setText(QApplication::translate("MainWindow", "\346\267\273\345\212\240", nullptr));
        pushButton_send->setText(QApplication::translate("MainWindow", "\345\217\221\351\200\201", nullptr));
        pushButton_delete->setText(QApplication::translate("MainWindow", "\345\210\240\351\231\244", nullptr));
        pushButton_zip->setText(QApplication::translate("MainWindow", "\345\216\213\347\274\251", nullptr));
        label_operate_area->setText(QApplication::translate("MainWindow", "\347\224\250\346\210\267\346\223\215\344\275\234\345\214\272", nullptr));
        label_operate_area->setProperty("class", QVariant(QApplication::translate("MainWindow", "h2", nullptr)));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAINFEJPNV_H

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screen1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 1264)
        MainWindow.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(798, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")

        self.gridLayout.addWidget(self.btn_exit, 0, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(110, 80, 261, 21))
        self.password.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 49, 16))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.login = QLineEdit(self.widget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(110, 40, 261, 21))
        self.login.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 49, 16))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(420, 30, 81, 61))
        self.btn_login.setStyleSheet(u"border-image:url(\"/picture/LOOKBACK.jpg\");")
        self.btn_create = QPushButton(self.widget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(680, 20, 101, 91))
        self.btn_create.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PW :", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u" \ud68c\uc6d0\uac00\uc785", None))
    # retranslateUi


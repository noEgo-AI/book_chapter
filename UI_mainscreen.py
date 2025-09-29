# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainscreen.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(943, 705)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:rgb(255, 253, 185)")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setSpacing(110)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_menu2 = QPushButton(self.widget_3)
        self.btn_menu2.setObjectName(u"btn_menu2")
        icon = QIcon()
        icon.addFile(u":/newPrefix/picture/menu.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu2.setIcon(icon)
        self.btn_menu2.setCheckable(False)

        self.verticalLayout_9.addWidget(self.btn_menu2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(80)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_profile2 = QPushButton(self.widget_3)
        self.btn_profile2.setObjectName(u"btn_profile2")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/picture/profile.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_profile2.setIcon(icon1)
        self.btn_profile2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.btn_profile2)

        self.btn_calendar2 = QPushButton(self.widget_3)
        self.btn_calendar2.setObjectName(u"btn_calendar2")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/picture/calendar.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_calendar2.setIcon(icon2)
        self.btn_calendar2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.btn_calendar2)

        self.btn_iword2 = QPushButton(self.widget_3)
        self.btn_iword2.setObjectName(u"btn_iword2")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/picture/insertword.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_iword2.setIcon(icon3)
        self.btn_iword2.setIconSize(QSize(16, 16))
        self.btn_iword2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.btn_iword2)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_logout2 = QPushButton(self.widget_3)
        self.btn_logout2.setObjectName(u"btn_logout2")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/picture/hard.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout2.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.btn_logout2)

        self.btn_exit2 = QPushButton(self.widget_3)
        self.btn_exit2.setObjectName(u"btn_exit2")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/picture/total end.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit2.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.btn_exit2)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:rgb(255, 253, 185)")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setSpacing(110)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_menu1 = QPushButton(self.widget_2)
        self.btn_menu1.setObjectName(u"btn_menu1")
        self.btn_menu1.setIcon(icon)
        self.btn_menu1.setCheckable(False)
        self.btn_menu1.setChecked(False)

        self.verticalLayout_10.addWidget(self.btn_menu1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(80)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_profile1 = QPushButton(self.widget_2)
        self.btn_profile1.setObjectName(u"btn_profile1")
        self.btn_profile1.setIcon(icon1)
        self.btn_profile1.setCheckable(True)

        self.verticalLayout.addWidget(self.btn_profile1)

        self.btn_calendar1 = QPushButton(self.widget_2)
        self.btn_calendar1.setObjectName(u"btn_calendar1")
        self.btn_calendar1.setIcon(icon2)
        self.btn_calendar1.setCheckable(True)

        self.verticalLayout.addWidget(self.btn_calendar1)

        self.btn_iword1 = QPushButton(self.widget_2)
        self.btn_iword1.setObjectName(u"btn_iword1")
        self.btn_iword1.setIcon(icon3)
        self.btn_iword1.setCheckable(True)

        self.verticalLayout.addWidget(self.btn_iword1)


        self.verticalLayout_10.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 101, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_logout1 = QPushButton(self.widget_2)
        self.btn_logout1.setObjectName(u"btn_logout1")
        self.btn_logout1.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.btn_logout1)

        self.btn_exit1 = QPushButton(self.widget_2)
        self.btn_exit1.setObjectName(u"btn_exit1")
        self.btn_exit1.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.btn_exit1)


        self.verticalLayout_10.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 224, 192);")
        self.stackedWidget.setLineWidth(2)
        self.page_iword = QWidget()
        self.page_iword.setObjectName(u"page_iword")
        self.insertword = QLineEdit(self.page_iword)
        self.insertword.setObjectName(u"insertword")
        self.insertword.setGeometry(QRect(10, 20, 731, 91))
        self.insertword.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font: 700 36pt \"Segoe UI\";")
        self.insertword.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.save_toggle = QCheckBox(self.page_iword)
        self.save_toggle.setObjectName(u"save_toggle")
        self.save_toggle.setGeometry(QRect(750, 30, 41, 20))
        self.scrollArea = QScrollArea(self.page_iword)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 120, 731, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 729, 519))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lb_mean = QLabel(self.scrollAreaWidgetContents)
        self.lb_mean.setObjectName(u"lb_mean")
        self.lb_mean.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font: 700 18pt \"Segoe UI\";")
        self.lb_mean.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_5.addWidget(self.lb_mean, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page_iword)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_profile = QWidget()
        self.page_profile.setObjectName(u"page_profile")
        self.gridLayout_3 = QGridLayout(self.page_profile)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.page_profile)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_picture = QLabel(self.widget)
        self.lb_picture.setObjectName(u"lb_picture")
        self.lb_picture.setMaximumSize(QSize(291, 321))
        self.lb_picture.setPixmap(QPixmap(u":/newPrefix/picture/LOOKBACK.jpg"))
        self.lb_picture.setScaledContents(True)

        self.gridLayout_2.addWidget(self.lb_picture, 0, 0, 2, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.check_mf = QCheckBox(self.widget)
        self.check_mf.setObjectName(u"check_mf")
        self.check_mf.setMaximumSize(QSize(75, 20))
        self.check_mf.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.check_mf.setCheckable(True)
        self.check_mf.setChecked(False)

        self.horizontalLayout_6.addWidget(self.check_mf)

        self.lb_state = QLabel(self.widget)
        self.lb_state.setObjectName(u"lb_state")
        self.lb_state.setStyleSheet(u"font: 700 24pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")
        self.lb_state.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_state)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 81))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(61, 61))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/picture/name.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.edit_name = QLineEdit(self.frame)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.edit_name.setReadOnly(True)

        self.horizontalLayout.addWidget(self.edit_name)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 81))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(61, 61))
        self.label_3.setPixmap(QPixmap(u":/newPrefix/picture/age.jpg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.edit_age = QLineEdit(self.frame_2)
        self.edit_age.setObjectName(u"edit_age")
        self.edit_age.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.edit_age.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.edit_age)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 81))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QSize(61, 61))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/picture/password.jpg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.edit_pw = QLineEdit(self.frame_3)
        self.edit_pw.setObjectName(u"edit_pw")
        self.edit_pw.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.edit_pw.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.edit_pw)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(541, 231))
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.edit_detail = QLineEdit(self.widget_4)
        self.edit_detail.setObjectName(u"edit_detail")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_detail.sizePolicy().hasHeightForWidth())
        self.edit_detail.setSizePolicy(sizePolicy1)
        self.edit_detail.setMinimumSize(QSize(132, 100))
        self.edit_detail.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.edit_detail.setReadOnly(True)

        self.gridLayout_6.addWidget(self.edit_detail, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_save = QPushButton(self.widget_4)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_4.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(self.widget_4)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_4.addWidget(self.btn_cancel)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 2, 0, 1, 2)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_profile)
        self.page_calendar = QWidget()
        self.page_calendar.setObjectName(u"page_calendar")
        self.verticalLayout_8 = QVBoxLayout(self.page_calendar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_5 = QWidget(self.page_calendar)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 42))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_lastmonth = QPushButton(self.widget_5)
        self.btn_lastmonth.setObjectName(u"btn_lastmonth")

        self.horizontalLayout_5.addWidget(self.btn_lastmonth)

        self.btn_yearchange = QPushButton(self.widget_5)
        self.btn_yearchange.setObjectName(u"btn_yearchange")

        self.horizontalLayout_5.addWidget(self.btn_yearchange)

        self.sbox_year = QSpinBox(self.widget_5)
        self.sbox_year.setObjectName(u"sbox_year")
        self.sbox_year.setMinimum(-9999)
        self.sbox_year.setMaximum(9999)
        self.sbox_year.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_5.addWidget(self.sbox_year)

        self.cbox_month = QComboBox(self.widget_5)
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.addItem("")
        self.cbox_month.setObjectName(u"cbox_month")

        self.horizontalLayout_5.addWidget(self.cbox_month)

        self.btn_nextmonth = QPushButton(self.widget_5)
        self.btn_nextmonth.setObjectName(u"btn_nextmonth")

        self.horizontalLayout_5.addWidget(self.btn_nextmonth)


        self.verticalLayout_8.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.page_calendar)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 15, 15, 15)
        self.Wednesday = QLabel(self.widget_6)
        self.Wednesday.setObjectName(u"Wednesday")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Wednesday.sizePolicy().hasHeightForWidth())
        self.Wednesday.setSizePolicy(sizePolicy2)
        self.Wednesday.setMinimumSize(QSize(0, 80))
        self.Wednesday.setMaximumSize(QSize(16777215, 16777215))
        self.Wednesday.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")
        self.Wednesday.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.Wednesday, 1, 5, 1, 1)

        self.btn_6 = QPushButton(self.widget_6)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy3)
        self.btn_6.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_6, 3, 7, 1, 1)

        self.btn_17 = QPushButton(self.widget_6)
        self.btn_17.setObjectName(u"btn_17")
        sizePolicy3.setHeightForWidth(self.btn_17.sizePolicy().hasHeightForWidth())
        self.btn_17.setSizePolicy(sizePolicy3)
        self.btn_17.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_17, 5, 4, 1, 1)

        self.btn_32 = QPushButton(self.widget_6)
        self.btn_32.setObjectName(u"btn_32")
        sizePolicy3.setHeightForWidth(self.btn_32.sizePolicy().hasHeightForWidth())
        self.btn_32.setSizePolicy(sizePolicy3)
        self.btn_32.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_32, 8, 5, 1, 1)

        self.btn_7 = QPushButton(self.widget_6)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy3.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy3)
        self.btn_7.setStyleSheet(u"background-color:rgb(87, 107, 239);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_7, 3, 8, 1, 1)

        self.btn_24 = QPushButton(self.widget_6)
        self.btn_24.setObjectName(u"btn_24")
        sizePolicy3.setHeightForWidth(self.btn_24.sizePolicy().hasHeightForWidth())
        self.btn_24.setSizePolicy(sizePolicy3)
        self.btn_24.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_24, 7, 4, 1, 1)

        self.btn_29 = QPushButton(self.widget_6)
        self.btn_29.setObjectName(u"btn_29")
        sizePolicy3.setHeightForWidth(self.btn_29.sizePolicy().hasHeightForWidth())
        self.btn_29.setSizePolicy(sizePolicy3)
        self.btn_29.setStyleSheet(u"background-color:rgb(255, 158, 158);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_29, 8, 1, 1, 1)

        self.btn_15 = QPushButton(self.widget_6)
        self.btn_15.setObjectName(u"btn_15")
        sizePolicy3.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy3)
        self.btn_15.setStyleSheet(u"background-color:rgb(255, 158, 158);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_15, 5, 1, 1, 1)

        self.btn_11 = QPushButton(self.widget_6)
        self.btn_11.setObjectName(u"btn_11")
        sizePolicy3.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy3)
        self.btn_11.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_11, 4, 5, 1, 1)

        self.btn_35 = QPushButton(self.widget_6)
        self.btn_35.setObjectName(u"btn_35")
        sizePolicy3.setHeightForWidth(self.btn_35.sizePolicy().hasHeightForWidth())
        self.btn_35.setSizePolicy(sizePolicy3)
        self.btn_35.setStyleSheet(u"background-color:rgb(87, 107, 239);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_35, 8, 8, 1, 1)

        self.btn_16 = QPushButton(self.widget_6)
        self.btn_16.setObjectName(u"btn_16")
        sizePolicy3.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy3)
        self.btn_16.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_16, 5, 3, 1, 1)

        self.btn_30 = QPushButton(self.widget_6)
        self.btn_30.setObjectName(u"btn_30")
        sizePolicy3.setHeightForWidth(self.btn_30.sizePolicy().hasHeightForWidth())
        self.btn_30.setSizePolicy(sizePolicy3)
        self.btn_30.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_30, 8, 3, 1, 1)

        self.sunday = QLabel(self.widget_6)
        self.sunday.setObjectName(u"sunday")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sunday.sizePolicy().hasHeightForWidth())
        self.sunday.setSizePolicy(sizePolicy4)
        self.sunday.setMinimumSize(QSize(0, 80))
        self.sunday.setMaximumSize(QSize(16777215, 16777215))
        self.sunday.setStyleSheet(u"background-color:rgb(255, 158, 158);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";\n"
"")
        self.sunday.setTextFormat(Qt.TextFormat.AutoText)
        self.sunday.setScaledContents(False)
        self.sunday.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.sunday, 1, 1, 1, 1)

        self.monday = QLabel(self.widget_6)
        self.monday.setObjectName(u"monday")
        sizePolicy2.setHeightForWidth(self.monday.sizePolicy().hasHeightForWidth())
        self.monday.setSizePolicy(sizePolicy2)
        self.monday.setMinimumSize(QSize(0, 80))
        self.monday.setMaximumSize(QSize(16777215, 16777215))
        self.monday.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")
        self.monday.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.monday, 1, 3, 1, 1)

        self.btn_2 = QPushButton(self.widget_6)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy3.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy3)
        self.btn_2.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_2, 3, 3, 1, 1)

        self.btn_4 = QPushButton(self.widget_6)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy3.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy3)
        self.btn_4.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_4, 3, 5, 1, 1)

        self.btn_5 = QPushButton(self.widget_6)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy3.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy3)
        self.btn_5.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_5, 3, 6, 1, 1)

        self.btn_23 = QPushButton(self.widget_6)
        self.btn_23.setObjectName(u"btn_23")
        sizePolicy3.setHeightForWidth(self.btn_23.sizePolicy().hasHeightForWidth())
        self.btn_23.setSizePolicy(sizePolicy3)
        self.btn_23.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_23, 7, 3, 1, 1)

        self.btn_41 = QPushButton(self.widget_6)
        self.btn_41.setObjectName(u"btn_41")
        sizePolicy3.setHeightForWidth(self.btn_41.sizePolicy().hasHeightForWidth())
        self.btn_41.setSizePolicy(sizePolicy3)
        self.btn_41.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_41, 9, 7, 1, 1)

        self.Saturday = QLabel(self.widget_6)
        self.Saturday.setObjectName(u"Saturday")
        sizePolicy2.setHeightForWidth(self.Saturday.sizePolicy().hasHeightForWidth())
        self.Saturday.setSizePolicy(sizePolicy2)
        self.Saturday.setMinimumSize(QSize(0, 80))
        self.Saturday.setMaximumSize(QSize(16777215, 16777215))
        self.Saturday.setStyleSheet(u"background-color:rgb(87, 107, 239);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";\n"
"")
        self.Saturday.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.Saturday, 1, 8, 1, 1)

        self.btn_20 = QPushButton(self.widget_6)
        self.btn_20.setObjectName(u"btn_20")
        sizePolicy3.setHeightForWidth(self.btn_20.sizePolicy().hasHeightForWidth())
        self.btn_20.setSizePolicy(sizePolicy3)
        self.btn_20.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_20, 5, 7, 1, 1)

        self.btn_22 = QPushButton(self.widget_6)
        self.btn_22.setObjectName(u"btn_22")
        sizePolicy3.setHeightForWidth(self.btn_22.sizePolicy().hasHeightForWidth())
        self.btn_22.setSizePolicy(sizePolicy3)
        self.btn_22.setStyleSheet(u"background-color:rgb(255, 158, 158);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_22, 7, 1, 1, 1)

        self.btn_13 = QPushButton(self.widget_6)
        self.btn_13.setObjectName(u"btn_13")
        sizePolicy3.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy3)
        self.btn_13.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_13, 4, 7, 1, 1)

        self.btn_33 = QPushButton(self.widget_6)
        self.btn_33.setObjectName(u"btn_33")
        sizePolicy3.setHeightForWidth(self.btn_33.sizePolicy().hasHeightForWidth())
        self.btn_33.setSizePolicy(sizePolicy3)
        self.btn_33.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_33, 8, 6, 1, 1)

        self.btn_34 = QPushButton(self.widget_6)
        self.btn_34.setObjectName(u"btn_34")
        sizePolicy3.setHeightForWidth(self.btn_34.sizePolicy().hasHeightForWidth())
        self.btn_34.setSizePolicy(sizePolicy3)
        self.btn_34.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_34, 8, 7, 1, 1)

        self.btn_39 = QPushButton(self.widget_6)
        self.btn_39.setObjectName(u"btn_39")
        sizePolicy3.setHeightForWidth(self.btn_39.sizePolicy().hasHeightForWidth())
        self.btn_39.setSizePolicy(sizePolicy3)
        self.btn_39.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_39, 9, 5, 1, 1)

        self.btn_26 = QPushButton(self.widget_6)
        self.btn_26.setObjectName(u"btn_26")
        sizePolicy3.setHeightForWidth(self.btn_26.sizePolicy().hasHeightForWidth())
        self.btn_26.setSizePolicy(sizePolicy3)
        self.btn_26.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_26, 7, 6, 1, 1)

        self.btn_36 = QPushButton(self.widget_6)
        self.btn_36.setObjectName(u"btn_36")
        sizePolicy3.setHeightForWidth(self.btn_36.sizePolicy().hasHeightForWidth())
        self.btn_36.setSizePolicy(sizePolicy3)
        self.btn_36.setStyleSheet(u"background-color:rgb(255, 158, 158);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_36, 9, 1, 1, 1)

        self.btn_42 = QPushButton(self.widget_6)
        self.btn_42.setObjectName(u"btn_42")
        sizePolicy3.setHeightForWidth(self.btn_42.sizePolicy().hasHeightForWidth())
        self.btn_42.setSizePolicy(sizePolicy3)
        self.btn_42.setStyleSheet(u"background-color:rgb(87, 107, 239);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_42, 9, 8, 1, 1)

        self.btn_40 = QPushButton(self.widget_6)
        self.btn_40.setObjectName(u"btn_40")
        sizePolicy3.setHeightForWidth(self.btn_40.sizePolicy().hasHeightForWidth())
        self.btn_40.setSizePolicy(sizePolicy3)
        self.btn_40.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_40, 9, 6, 1, 1)

        self.btn_3 = QPushButton(self.widget_6)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy3.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy3)
        self.btn_3.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_3, 3, 4, 1, 1)

        self.btn_12 = QPushButton(self.widget_6)
        self.btn_12.setObjectName(u"btn_12")
        sizePolicy3.setHeightForWidth(self.btn_12.sizePolicy().hasHeightForWidth())
        self.btn_12.setSizePolicy(sizePolicy3)
        self.btn_12.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_12, 4, 6, 1, 1)

        self.btn_38 = QPushButton(self.widget_6)
        self.btn_38.setObjectName(u"btn_38")
        sizePolicy3.setHeightForWidth(self.btn_38.sizePolicy().hasHeightForWidth())
        self.btn_38.setSizePolicy(sizePolicy3)
        self.btn_38.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_38, 9, 4, 1, 1)

        self.Tuesday = QLabel(self.widget_6)
        self.Tuesday.setObjectName(u"Tuesday")
        sizePolicy2.setHeightForWidth(self.Tuesday.sizePolicy().hasHeightForWidth())
        self.Tuesday.setSizePolicy(sizePolicy2)
        self.Tuesday.setMinimumSize(QSize(0, 80))
        self.Tuesday.setMaximumSize(QSize(16777215, 16777215))
        self.Tuesday.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")
        self.Tuesday.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.Tuesday, 1, 4, 1, 1)

        self.btn_18 = QPushButton(self.widget_6)
        self.btn_18.setObjectName(u"btn_18")
        sizePolicy3.setHeightForWidth(self.btn_18.sizePolicy().hasHeightForWidth())
        self.btn_18.setSizePolicy(sizePolicy3)
        self.btn_18.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_18, 5, 5, 1, 1)

        self.btn_8 = QPushButton(self.widget_6)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy3.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy3)
        self.btn_8.setStyleSheet(u"background-color:rgb(255, 158, 158);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_8, 4, 1, 1, 1)

        self.btn_14 = QPushButton(self.widget_6)
        self.btn_14.setObjectName(u"btn_14")
        sizePolicy3.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy3)
        self.btn_14.setStyleSheet(u"background-color:rgb(87, 107, 239);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_14, 4, 8, 1, 1)

        self.btn_1 = QPushButton(self.widget_6)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy3.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy3)
        self.btn_1.setStyleSheet(u"background-color:rgb(255, 158, 158);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_1, 3, 1, 1, 1)

        self.btn_19 = QPushButton(self.widget_6)
        self.btn_19.setObjectName(u"btn_19")
        sizePolicy3.setHeightForWidth(self.btn_19.sizePolicy().hasHeightForWidth())
        self.btn_19.setSizePolicy(sizePolicy3)
        self.btn_19.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_19, 5, 6, 1, 1)

        self.btn_25 = QPushButton(self.widget_6)
        self.btn_25.setObjectName(u"btn_25")
        sizePolicy3.setHeightForWidth(self.btn_25.sizePolicy().hasHeightForWidth())
        self.btn_25.setSizePolicy(sizePolicy3)
        self.btn_25.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_25, 7, 5, 1, 1)

        self.btn_10 = QPushButton(self.widget_6)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy3.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy3)
        self.btn_10.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_10, 4, 4, 1, 1)

        self.btn_37 = QPushButton(self.widget_6)
        self.btn_37.setObjectName(u"btn_37")
        sizePolicy3.setHeightForWidth(self.btn_37.sizePolicy().hasHeightForWidth())
        self.btn_37.setSizePolicy(sizePolicy3)
        self.btn_37.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_37, 9, 3, 1, 1)

        self.btn_9 = QPushButton(self.widget_6)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy3.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy3)
        self.btn_9.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_9, 4, 3, 1, 1)

        self.Friday = QLabel(self.widget_6)
        self.Friday.setObjectName(u"Friday")
        sizePolicy2.setHeightForWidth(self.Friday.sizePolicy().hasHeightForWidth())
        self.Friday.setSizePolicy(sizePolicy2)
        self.Friday.setMinimumSize(QSize(0, 80))
        self.Friday.setMaximumSize(QSize(16777215, 16777215))
        self.Friday.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")
        self.Friday.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.Friday, 1, 7, 1, 1)

        self.btn_21 = QPushButton(self.widget_6)
        self.btn_21.setObjectName(u"btn_21")
        sizePolicy3.setHeightForWidth(self.btn_21.sizePolicy().hasHeightForWidth())
        self.btn_21.setSizePolicy(sizePolicy3)
        self.btn_21.setStyleSheet(u"background-color:rgb(87, 107, 239);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_21, 5, 8, 1, 1)

        self.btn_27 = QPushButton(self.widget_6)
        self.btn_27.setObjectName(u"btn_27")
        sizePolicy3.setHeightForWidth(self.btn_27.sizePolicy().hasHeightForWidth())
        self.btn_27.setSizePolicy(sizePolicy3)
        self.btn_27.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_27, 7, 7, 1, 1)

        self.Thursday = QLabel(self.widget_6)
        self.Thursday.setObjectName(u"Thursday")
        sizePolicy2.setHeightForWidth(self.Thursday.sizePolicy().hasHeightForWidth())
        self.Thursday.setSizePolicy(sizePolicy2)
        self.Thursday.setMinimumSize(QSize(0, 80))
        self.Thursday.setMaximumSize(QSize(16777215, 16777215))
        self.Thursday.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")
        self.Thursday.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.Thursday, 1, 6, 1, 1)

        self.btn_28 = QPushButton(self.widget_6)
        self.btn_28.setObjectName(u"btn_28")
        sizePolicy3.setHeightForWidth(self.btn_28.sizePolicy().hasHeightForWidth())
        self.btn_28.setSizePolicy(sizePolicy3)
        self.btn_28.setStyleSheet(u"background-color:rgb(87, 107, 239);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_28, 7, 8, 1, 1)

        self.btn_31 = QPushButton(self.widget_6)
        self.btn_31.setObjectName(u"btn_31")
        sizePolicy3.setHeightForWidth(self.btn_31.sizePolicy().hasHeightForWidth())
        self.btn_31.setSizePolicy(sizePolicy3)
        self.btn_31.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"font: 700 30pt \"KoPubWorld\ub3cb\uc6c0\uccb4 Bold\";")

        self.gridLayout_4.addWidget(self.btn_31, 8, 4, 1, 1)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.page_calendar)

        self.gridLayout.addWidget(self.stackedWidget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 943, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_yearchange.clicked.connect(self.sbox_year.show)
        self.sbox_year.editingFinished.connect(self.btn_yearchange.show)
        self.btn_yearchange.clicked.connect(self.btn_yearchange.hide)
        self.btn_menu2.clicked.connect(self.widget_2.show)
        self.btn_menu2.clicked.connect(self.widget_3.hide)
        self.btn_menu1.clicked.connect(self.widget_3.show)
        self.btn_menu1.clicked.connect(self.widget_2.hide)
        self.btn_profile2.toggled.connect(self.btn_profile1.toggle)
        self.btn_calendar2.toggled.connect(self.btn_calendar1.toggle)
        self.sbox_year.editingFinished.connect(self.sbox_year.hide)
        self.btn_iword2.clicked["bool"].connect(self.btn_iword1.toggle)

        self.stackedWidget.setCurrentIndex(0)
        self.cbox_month.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu2.setText("")
        self.btn_profile2.setText("")
        self.btn_calendar2.setText("")
        self.btn_iword2.setText("")
        self.btn_logout2.setText("")
        self.btn_exit2.setText("")
        self.btn_menu1.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_profile1.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.btn_calendar1.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.btn_iword1.setText(QCoreApplication.translate("MainWindow", u"Iword", None))
        self.btn_logout1.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btn_exit1.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.insertword.setText("")
        self.save_toggle.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.lb_mean.setText("")
        self.lb_picture.setText("")
        self.check_mf.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815\ud558\uae30", None))
        self.lb_state.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\ud558\uae30", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"\ucde8\uc18c\ud558\uae30", None))
        self.btn_lastmonth.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_yearchange.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cbox_month.setItemText(0, QCoreApplication.translate("MainWindow", u"1\uc6d4", None))
        self.cbox_month.setItemText(1, QCoreApplication.translate("MainWindow", u"2\uc6d4", None))
        self.cbox_month.setItemText(2, QCoreApplication.translate("MainWindow", u"3\uc6d4", None))
        self.cbox_month.setItemText(3, QCoreApplication.translate("MainWindow", u"4\uc6d4", None))
        self.cbox_month.setItemText(4, QCoreApplication.translate("MainWindow", u"5\uc6d4", None))
        self.cbox_month.setItemText(5, QCoreApplication.translate("MainWindow", u"6\uc6d4", None))
        self.cbox_month.setItemText(6, QCoreApplication.translate("MainWindow", u"7\uc6d4", None))
        self.cbox_month.setItemText(7, QCoreApplication.translate("MainWindow", u"8\uc6d4", None))
        self.cbox_month.setItemText(8, QCoreApplication.translate("MainWindow", u"9\uc6d4", None))
        self.cbox_month.setItemText(9, QCoreApplication.translate("MainWindow", u"10\uc6d4", None))
        self.cbox_month.setItemText(10, QCoreApplication.translate("MainWindow", u"11\uc6d4", None))
        self.cbox_month.setItemText(11, QCoreApplication.translate("MainWindow", u"12\uc6d4", None))

        self.btn_nextmonth.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Wednesday.setText(QCoreApplication.translate("MainWindow", u"\uc218", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_17.setText("")
        self.btn_32.setText("")
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_24.setText("")
        self.btn_29.setText("")
        self.btn_15.setText("")
        self.btn_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_35.setText("")
        self.btn_16.setText("")
        self.btn_30.setText("")
        self.sunday.setText(QCoreApplication.translate("MainWindow", u"\uc77c", None))
        self.monday.setText(QCoreApplication.translate("MainWindow", u"\uc6d4", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_23.setText("")
        self.btn_41.setText("")
        self.Saturday.setText(QCoreApplication.translate("MainWindow", u"\ud1a0", None))
        self.btn_20.setText("")
        self.btn_22.setText("")
        self.btn_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_33.setText("")
        self.btn_34.setText("")
        self.btn_39.setText("")
        self.btn_26.setText("")
        self.btn_36.setText("")
        self.btn_42.setText("")
        self.btn_40.setText("")
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_38.setText("")
        self.Tuesday.setText(QCoreApplication.translate("MainWindow", u"\ud654", None))
        self.btn_18.setText("")
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_14.setText("")
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_19.setText("")
        self.btn_25.setText("")
        self.btn_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_37.setText("")
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Friday.setText(QCoreApplication.translate("MainWindow", u"\uae08", None))
        self.btn_21.setText("")
        self.btn_27.setText("")
        self.Thursday.setText(QCoreApplication.translate("MainWindow", u"\ubaa9", None))
        self.btn_28.setText("")
        self.btn_31.setText("")
    # retranslateUi


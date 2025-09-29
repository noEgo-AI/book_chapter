# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_create_form(object):
    def setupUi(self, create_form):
        if not create_form.objectName():
            create_form.setObjectName(u"create_form")
        create_form.resize(300, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(create_form.sizePolicy().hasHeightForWidth())
        create_form.setSizePolicy(sizePolicy)
        create_form.setBaseSize(QSize(300, 400))
        self.gridLayout = QGridLayout(create_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 6, -1)
        self.widget_id = QWidget(create_form)
        self.widget_id.setObjectName(u"widget_id")
        self.horizontalLayout = QHBoxLayout(self.widget_id)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_id)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515 ExtraBold"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.widget_id)

        self.create_id = QLineEdit(create_form)
        self.create_id.setObjectName(u"create_id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(250)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.create_id.sizePolicy().hasHeightForWidth())
        self.create_id.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.create_id)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.create_check = QPushButton(create_form)
        self.create_check.setObjectName(u"create_check")

        self.verticalLayout.addWidget(self.create_check)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.description = QLabel(create_form)
        self.description.setObjectName(u"description")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy2)
        self.description.setStyleSheet(u"font: 700 9pt \"\ub098\ub214\uace0\ub515 ExtraBold\";")
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.description, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 6, -1)
        self.widget_pw = QWidget(create_form)
        self.widget_pw.setObjectName(u"widget_pw")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_pw)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget_pw)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_3.addWidget(self.widget_pw)

        self.create_pw = QLineEdit(create_form)
        self.create_pw.setObjectName(u"create_pw")
        sizePolicy1.setHeightForWidth(self.create_pw.sizePolicy().hasHeightForWidth())
        self.create_pw.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.create_pw)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, -1, 6, -1)
        self.widget_name = QWidget(create_form)
        self.widget_name.setObjectName(u"widget_name")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_name)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_name)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.widget_name)

        self.create_name = QLineEdit(create_form)
        self.create_name.setObjectName(u"create_name")
        sizePolicy1.setHeightForWidth(self.create_name.sizePolicy().hasHeightForWidth())
        self.create_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.create_name)


        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(8, -1, 6, -1)
        self.widget_age = QWidget(create_form)
        self.widget_age.setObjectName(u"widget_age")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_age)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.widget_age)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_7.addWidget(self.widget_age)

        self.create_age = QLineEdit(create_form)
        self.create_age.setObjectName(u"create_age")
        sizePolicy1.setHeightForWidth(self.create_age.sizePolicy().hasHeightForWidth())
        self.create_age.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.create_age)


        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)

        self.create_save = QPushButton(create_form)
        self.create_save.setObjectName(u"create_save")

        self.gridLayout.addWidget(self.create_save, 5, 0, 1, 1)


        self.retranslateUi(create_form)

        QMetaObject.connectSlotsByName(create_form)
    # setupUi

    def retranslateUi(self, create_form):
        create_form.setWindowTitle(QCoreApplication.translate("create_form", u"Form", None))
        self.label.setText(QCoreApplication.translate("create_form", u"*ID", None))
        self.create_check.setText(QCoreApplication.translate("create_form", u"\uc911\ubcf5\ud655\uc778", None))
        self.description.setText(QCoreApplication.translate("create_form", u"*\ub294 \ud544\uc218\ub85c \uae30\uc785\ud574\uc57c \ud569\ub2c8\ub2e4.", None))
        self.label_2.setText(QCoreApplication.translate("create_form", u"*PW", None))
        self.label_3.setText(QCoreApplication.translate("create_form", u"\uc774\ub984", None))
        self.label_4.setText(QCoreApplication.translate("create_form", u"\ub098\uc774", None))
        self.create_save.setText(QCoreApplication.translate("create_form", u"\uc800\uc7a5\ud558\uae30", None))
    # retranslateUi


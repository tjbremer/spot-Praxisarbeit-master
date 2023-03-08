# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login-ScreenwRiKhw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login-ScreenKapgOM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginScreen(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(668, 232)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.Username_input = QLineEdit(Dialog)
        self.Username_input.setObjectName(u"Username_input")
        sizePolicy1.setHeightForWidth(self.Username_input.sizePolicy().hasHeightForWidth())
        self.Username_input.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Username_input, 0, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.Password_input = QLineEdit(Dialog)
        self.Password_input.setObjectName(u"Password_input")
        sizePolicy1.setHeightForWidth(self.Password_input.sizePolicy().hasHeightForWidth())
        self.Password_input.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Password_input, 0, 3, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.Hostname_input = QLineEdit(Dialog)
        self.Hostname_input.setObjectName(u"Hostname_input")
        sizePolicy1.setHeightForWidth(self.Hostname_input.sizePolicy().hasHeightForWidth())
        self.Hostname_input.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Hostname_input, 0, 5, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.button_login = QPushButton(Dialog)
        self.button_login.setObjectName(u"button_login")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_login.sizePolicy().hasHeightForWidth())
        self.button_login.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.button_login, 2, 0, 1, 1)

        self.info_label = QLabel(Dialog)
        self.info_label.setObjectName(u"info_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy3)
        self.info_label.setStyleSheet(u"QLabel{color: red; font-weight: bold}")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(False)
        self.info_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_2.addWidget(self.info_label, 3, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Please provide the Username, the Password and the Hostname (IP) for your robot!", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username: ", None))
        self.Username_input.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password: ", None))
        self.Password_input.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Hostname: ", None))
        self.Hostname_input.setText("")
        self.button_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.info_label.setText("")
    # retranslateUi


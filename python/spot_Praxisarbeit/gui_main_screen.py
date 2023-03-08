# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main-Screen-Dialogvostkz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainScreen(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(882, 483)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.data_dropdown = QComboBox(Dialog)
        self.data_dropdown.addItem("")
        self.data_dropdown.addItem("")
        self.data_dropdown.addItem("")
        self.data_dropdown.addItem("")
        self.data_dropdown.setObjectName(u"data_dropdown")

        self.verticalLayout.addWidget(self.data_dropdown)

        self.button_send_data_request = QPushButton(Dialog)
        self.button_send_data_request.setObjectName(u"button_send_data_request")

        self.verticalLayout.addWidget(self.button_send_data_request)

        self.response_box = QTextEdit(Dialog)
        self.response_box.setObjectName(u"response_box")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.response_box.sizePolicy().hasHeightForWidth())
        self.response_box.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.response_box)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.image_dropdown = QComboBox(Dialog)
        self.image_dropdown.addItem("")
        self.image_dropdown.addItem("")
        self.image_dropdown.addItem("")
        self.image_dropdown.addItem("")
        self.image_dropdown.addItem("")
        self.image_dropdown.setObjectName(u"image_dropdown")

        self.verticalLayout_2.addWidget(self.image_dropdown)

        self.show_image_label = QLabel(Dialog)
        self.show_image_label.setObjectName(u"show_image_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.show_image_label.sizePolicy().hasHeightForWidth())
        self.show_image_label.setSizePolicy(sizePolicy1)
        self.show_image_label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.show_image_label)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, -1, -1, 200)
        self.button_turn_left = QPushButton(Dialog)
        self.button_turn_left.setObjectName(u"button_turn_left")
        self.button_turn_left.setAutoRepeat(True)
        self.button_turn_left.setAutoRepeatDelay(300)
        self.button_turn_left.setAutoRepeatInterval(600)

        self.gridLayout.addWidget(self.button_turn_left, 2, 0, 1, 1)

        self.button_move_right = QPushButton(Dialog)
        self.button_move_right.setObjectName(u"button_move_right")
        self.button_move_right.setAutoRepeat(True)
        self.button_move_right.setAutoRepeatInterval(600)

        self.gridLayout.addWidget(self.button_move_right, 3, 2, 1, 1)

        self.button_sit = QPushButton(Dialog)
        self.button_sit.setObjectName(u"button_sit")

        self.gridLayout.addWidget(self.button_sit, 4, 0, 1, 1)

        self.button_start_robot = QPushButton(Dialog)
        self.button_start_robot.setObjectName(u"button_start_robot")

        self.gridLayout.addWidget(self.button_start_robot, 5, 0, 1, 1)

        self.button_move_forward = QPushButton(Dialog)
        self.button_move_forward.setObjectName(u"button_move_forward")
        self.button_move_forward.setAutoRepeat(True)
        self.button_move_forward.setAutoRepeatInterval(600)

        self.gridLayout.addWidget(self.button_move_forward, 2, 1, 1, 1)

        self.button_turn_right = QPushButton(Dialog)
        self.button_turn_right.setObjectName(u"button_turn_right")
        self.button_turn_right.setAutoRepeat(True)
        self.button_turn_right.setAutoRepeatInterval(600)

        self.gridLayout.addWidget(self.button_turn_right, 2, 2, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.button_stand = QPushButton(Dialog)
        self.button_stand.setObjectName(u"button_stand")

        self.gridLayout.addWidget(self.button_stand, 4, 2, 1, 1)

        self.button_toggle_estop = QPushButton(Dialog)
        self.button_toggle_estop.setObjectName(u"button_toggle_estop")

        self.gridLayout.addWidget(self.button_toggle_estop, 5, 1, 1, 1)

        self.button_shutdown_robot = QPushButton(Dialog)
        self.button_shutdown_robot.setObjectName(u"button_shutdown_robot")

        self.gridLayout.addWidget(self.button_shutdown_robot, 5, 2, 1, 1)

        self.button_move_backwards = QPushButton(Dialog)
        self.button_move_backwards.setObjectName(u"button_move_backwards")
        self.button_move_backwards.setAutoRepeat(True)
        self.button_move_backwards.setAutoRepeatInterval(600)

        self.gridLayout.addWidget(self.button_move_backwards, 4, 1, 1, 1)

        self.button_toggle_power = QPushButton(Dialog)
        self.button_toggle_power.setObjectName(u"button_toggle_power")

        self.gridLayout.addWidget(self.button_toggle_power, 3, 1, 1, 1)

        self.button_move_left = QPushButton(Dialog)
        self.button_move_left.setObjectName(u"button_move_left")
        self.button_move_left.setAutoRepeat(True)
        self.button_move_left.setAutoRepeatInterval(600)

        self.gridLayout.addWidget(self.button_move_left, 3, 0, 1, 1)

        self.estop_label = QLabel(Dialog)
        self.estop_label.setObjectName(u"estop_label")
        self.estop_label.setAutoFillBackground(False)
        self.estop_label.setStyleSheet(u"QLabel { background-color : red; color : black; }")
        self.estop_label.setAlignment(Qt.AlignCenter)
        self.estop_label.setWordWrap(False)

        self.gridLayout.addWidget(self.estop_label, 1, 0, 1, 1)

        self.star_shutdown_label = QLabel(Dialog)
        self.star_shutdown_label.setObjectName(u"star_shutdown_label")
        self.star_shutdown_label.setStyleSheet(u"QLabel { background-color : red; color : black; }")
        self.star_shutdown_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.star_shutdown_label, 1, 1, 1, 1)

        self.power_label = QLabel(Dialog)
        self.power_label.setObjectName(u"power_label")
        self.power_label.setStyleSheet(u"QLabel { background-color : red; color : black; }")
        self.power_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.power_label, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.info_label = QLabel(Dialog)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setStyleSheet(u"QLabel{color: red; font-weight: bold}")
        self.info_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.info_label)


        self.retranslateUi(Dialog)

        self.data_dropdown.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Requesting data", None))
        self.data_dropdown.setItemText(0, QCoreApplication.translate("Dialog", u"ID", None))
        self.data_dropdown.setItemText(1, QCoreApplication.translate("Dialog", u"Status", None))
        self.data_dropdown.setItemText(2, QCoreApplication.translate("Dialog", u"Hardware-Info", None))
        self.data_dropdown.setItemText(3, QCoreApplication.translate("Dialog", u"Metrics", None))

        self.button_send_data_request.setText(QCoreApplication.translate("Dialog", u"Sending Request", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Image", None))
        self.image_dropdown.setItemText(0, QCoreApplication.translate("Dialog", u"frontleft_fisheye_image", None))
        self.image_dropdown.setItemText(1, QCoreApplication.translate("Dialog", u"frontright_fisheye_image", None))
        self.image_dropdown.setItemText(2, QCoreApplication.translate("Dialog", u"left_fisheye_image", None))
        self.image_dropdown.setItemText(3, QCoreApplication.translate("Dialog", u"right_fisheye_image", None))
        self.image_dropdown.setItemText(4, QCoreApplication.translate("Dialog", u"back_fisheye_image", None))

        self.show_image_label.setText("")
        self.button_turn_left.setText(QCoreApplication.translate("Dialog", u"turn left", None))
        self.button_move_right.setText(QCoreApplication.translate("Dialog", u"right", None))
        self.button_sit.setText(QCoreApplication.translate("Dialog", u"sit", None))
        self.button_start_robot.setText(QCoreApplication.translate("Dialog", u"startRobot", None))
        self.button_move_forward.setText(QCoreApplication.translate("Dialog", u"forward", None))
        self.button_turn_right.setText(QCoreApplication.translate("Dialog", u"turn right", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Moving Controls", None))
        self.button_stand.setText(QCoreApplication.translate("Dialog", u"stand", None))
        self.button_toggle_estop.setText(QCoreApplication.translate("Dialog", u"estop on/off", None))
        self.button_shutdown_robot.setText(QCoreApplication.translate("Dialog", u"shutdownRobot", None))
        self.button_move_backwards.setText(QCoreApplication.translate("Dialog", u"backwards", None))
        self.button_toggle_power.setText(QCoreApplication.translate("Dialog", u"power on/off", None))
        self.button_move_left.setText(QCoreApplication.translate("Dialog", u"left", None))
        self.estop_label.setText(QCoreApplication.translate("Dialog", u"E-Stop OFF!", None))
        self.star_shutdown_label.setText(QCoreApplication.translate("Dialog", u"Robot OFF", None))
        self.power_label.setText(QCoreApplication.translate("Dialog", u"Power OFF!", None))
        self.info_label.setText("")
    # retranslateUi


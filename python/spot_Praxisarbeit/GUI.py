# Classes that initialize and show the screens and connect the buttons and input fields with the underlying methods

from PySide2 import QtWidgets

import base_config
import camera_image
import data_aquisition
import move_robot
from gui_login_screen import Ui_LoginScreen
from gui_main_screen import Ui_MainScreen
from functools import partial
from PySide2.QtGui import *
from PySide2.QtCore import *
from bosdyn.client.robot_command import *


# class that initializes and shows the login screen and connects the buttons and input fields with the underlying
# methods
class LoginScreen(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        # Slots einrichten
        self.ui.button_login.clicked.connect(partial(self.onLogin, parent))
        self.setModal(True)
        #self.exec_()

    # Is called when the login button is clicked
    # creates robot- and move_robot-objects
    # closes if login successful
    def onLogin(self, parent, GUI=None):
        # Read username, password, hostname
        username = self.ui.Username_input.text()
        password = self.ui.Password_input.text()
        hostname = self.ui.Hostname_input.text()
        if not username or not password or not hostname:
            self.ui.info_label.setText("At least one Credential is missing")
            return
        # call to create robot-object
        MainScreen.robot = base_config.connect_and_authenticate(username=username, password=password, hostname=hostname)
        # if login was not successful
        if not MainScreen.robot:
            self.ui.info_label.setText("Something went wrong, either the communication with the robot or you entered "
                                       "wrong credentials")
            return
        # call to create move_robot-object
        MainScreen.move_robot = move_robot.MoveRobot(MainScreen.robot)
        # close after logging in successfully
        self.accept()


# class that initializes and shows the main Screen and connects the buttons and input fields with the underlying
# methods
class MainScreen(QtWidgets.QDialog):
    robot = None
    move_robot = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)
        # Setup Slots
        self.ui.button_send_data_request.clicked.connect(self.sendDataRequest)
        self.ui.button_sit.pressed.connect(self.sendSitCommand)
        self.ui.button_stand.pressed.connect(self.sendStandCommand)
        self.ui.button_move_forward.pressed.connect(self.sendMoveForwardCommand)
        self.ui.button_move_backwards.pressed.connect(self.sendMoveBackwardsCommand)
        self.ui.button_move_left.pressed.connect(self.sendMoveLeftCommand)
        self.ui.button_move_right.pressed.connect(self.sendMoveRightCommand)
        self.ui.button_turn_left.pressed.connect(self.sendTurnLeftCommand)
        self.ui.button_turn_right.pressed.connect(self.sendTurnRightCommand)
        self.ui.button_toggle_power.clicked.connect(self.sendTogglePowerCommand)
        self.ui.button_toggle_estop.clicked.connect(self.sendToggleEStopCommand)
        self.ui.button_start_robot.clicked.connect(self.sendStartRobotCommand)
        self.ui.button_shutdown_robot.clicked.connect(self.sendShutdownRobotCommand)

        # create timer to call updating_robot_state_screens
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updating_robot_state_screens)
        self.timer.start()

        self.exec()

# Is called when the Main Screen Window is closed, to shutdown the robot safely
    def closeEvent(self, event):
        if self.robot:
            self.robot.power_off(cut_immediately=False)
        event.accept()

# Is called when the request-data-button is clicked
# sends Data Request to the robot and shows the returned data in the textbox
    def sendDataRequest(self):
        dataType = self.ui.data_dropdown.currentText()
        if dataType == "ID":
            data = data_aquisition.get_id(MainScreen.robot)
        elif dataType == "Status":
            data = data_aquisition.get_state(MainScreen.robot)
        elif dataType == "Hardware-Info":
            data = data_aquisition.get_hardware(MainScreen.robot)
        else:
            data = data_aquisition.get_metrics(MainScreen.robot)
        # Write data to textbox
        # convert protobuf-message to string with str()
        self.ui.response_box.setText(str(data))

# Is called when the sit-button is clicked
# sends the sit command to the robot
    def sendSitCommand(self):
        try:
            MainScreen.move_robot.sit()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the stand-button is clicked
# sends the stand command to the robot
    def sendStandCommand(self):
        try:
            MainScreen.move_robot.stand()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the forward-button is pressed
# sends the move forward command to the robot
    def sendMoveForwardCommand(self):
        try:
            MainScreen.move_robot.move_forward()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the backwards-button is clicked
# sends the move backwards command to the robot
    def sendMoveBackwardsCommand(self):
        try:
            MainScreen.move_robot.move_backwards()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the left-button is clicked
# sends the move left command to the robot
    def sendMoveLeftCommand(self):
        try:
            MainScreen.move_robot.move_left()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the right-button is clicked
# sends the move right command to the robot
    def sendMoveRightCommand(self):
        try:
            MainScreen.move_robot.move_right()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the turn left-button is clicked
# sends the turn left command to the robot
    def sendTurnLeftCommand(self):
        try:
            MainScreen.move_robot.turn_left()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the turn right-button is clicked
# sends the move turn right command to the robot
    def sendTurnRightCommand(self):
        try:
            MainScreen.move_robot.turn_right()
        except NotPoweredOnError:
            self.ui.info_label.setText("The Robot is not powered on")

# Is called when the power on/off-button is clicked
# sends the toggle power command to the robot
    def sendTogglePowerCommand(self):
        try:
            MainScreen.move_robot.toggle_power()
        except ResponseError as err:
            self.ui.info_label.setText("Robot is Estopped. Power can not be turned on.")
        except:
            self.ui.info_label.setText("No Lease on the Robot. Power can not be turned on. Start the Robot first before powering on.")

# Is called when the estop on/off-button is clicked
# sends the toggle estop command to the robot
    def sendToggleEStopCommand(self):
        MainScreen.move_robot.toggle_estop()

# Is called when the startrobot-button is clicked
# sends the start robot command to the robot
    def sendStartRobotCommand(self):
        MainScreen.move_robot.start()

# Is called when the shutdownRobot-button is clicked
# sends the shutdown robot command to the robot
    def sendShutdownRobotCommand(self):
        MainScreen.move_robot.shutdown()

# Is called once per second by the timer started in line 75
# Request information about the power-state, estop-state and lease-state and
# shows the states in the red or green tiles
# calls get_image-method for chosen camera and shows the image in te middle of the screen
    def updating_robot_state_screens(self):
        if self.robot:
            if MainScreen.robot.is_powered_on():
                self.ui.power_label.setStyleSheet("QLabel{background-color: green; color: black}")
                self.ui.power_label.setText("Power ON!")
            else:
                self.ui.power_label.setStyleSheet("QLabel{background-color: red; color: black}")
                self.ui.power_label.setText("Power OFF!")
            if not MainScreen.robot.is_estopped():
                self.ui.estop_label.setStyleSheet("QLabel{background-color: green; color: black}")
                self.ui.estop_label.setText("E-Stop OFF!")
            else:
                self.ui.estop_label.setStyleSheet("QLabel{background-color: red; color: black}")
                self.ui.estop_label.setText("E-Stop ON!")
            try:
                MainScreen.robot.lease_wallet.get_lease_state()
            except:
                self.ui.star_shutdown_label.setStyleSheet("QLabel{background-color: red; color: black}")
                self.ui.star_shutdown_label.setText("Robot OFF!")
            else:
                self.ui.star_shutdown_label.setStyleSheet("QLabel{background-color: green; color: black}")
                self.ui.star_shutdown_label.setText("Robot ON!")

            image_source = self.ui.image_dropdown.currentText()
            image_format = camera_image.get_image(MainScreen.robot, True, image_source)
            if image_format:
                image = QPixmap('image.jpg')
            else:
                image = QPixmap('image.png')
            self.ui.show_image_label.setPixmap(image)

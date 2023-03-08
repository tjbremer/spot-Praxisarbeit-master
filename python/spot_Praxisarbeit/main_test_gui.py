# Testfile for all Praxisarbeit files
import sys
import bosdyn.client.util
import GUI
from PySide2 import QtWidgets


def main():
    # setting the logger for information and error logging
    bosdyn.client.util.setup_logging()

    # starting the Widget-Application
    app = QtWidgets.QApplication(sys.argv)

    # starting the login-Screen
    login = GUI.LoginScreen()
    # exit program, if Login-window is closed forcibly
    if not login.exec_():
        sys.exit(-1)
    # start the Main-Screen if application is logged in to the robot
    GUI.MainScreen()

    return True


if __name__ == "__main__":
    if not main():
        sys.exit(1)  

# Basic Configuration, Connecting and disconnection from the robot

import bosdyn.client
from bosdyn.client import ResponseError, RpcError


# Method to connect to a robot and authenticate an user or an application at thr robot
def connect_and_authenticate(username, password, hostname):
    # create robot Object
    sdk = bosdyn.client.create_standard_sdk('Praxisarbeit')
    # connect to the robot
    robot = sdk.create_robot(hostname)
    if robot:
        robot.logger.info("Robot Object Created")
    else:
        robot.logger.error("Failed to create robot object")

    try:
        # authenticate to robot with username and password
        robot.authenticate(username, password)
        robot.logger.info("Robot Authenticated")
        # establish time-sync with the robot
        robot.time_sync.wait_for_sync()
        robot.logger.info("Robot time-synced")
    except (ResponseError, RpcError) as err:
        robot.logger.error("Failed to initialize robot communication: %s" % err)
        return False
    # Return the robot-object for further use
    return robot

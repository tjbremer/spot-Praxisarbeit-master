# Methods to move the robot
import time

from bosdyn.client.estop import EstopClient, EstopEndpoint, EstopKeepAlive
from bosdyn.client.lease import LeaseClient, LeaseKeepAlive
from bosdyn.client.power import PowerClient
from bosdyn.client.robot_command import RobotCommandClient, RobotCommandBuilder
import data_aquisition

# Setting Base Speed, turning speed, command duration and input rate for use in robot-command methods
VELOCITY_BASE_SPEED = 0.5  # m/s
VELOCITY_BASE_ANGULAR = 0.8  # rad/sec
VELOCITY_CMD_DURATION = 0.6  # seconds
COMMAND_INPUT_RATE = 0.1


# class that sends commands to the robot to move it around
class MoveRobot(object):

    # initialize the clients that are needed before the robot can power on and move
    def __init__(self, robot):
        self.robot = robot
        # Create Lease Client
        self.lease_client = robot.ensure_client(LeaseClient.default_service_name)
        self.robot.logger.info("Lease-Client created")
        try:
            # Create E-Stop-Client and E-Stop-Endpoint
            self.estop_client = robot.ensure_client(EstopClient.default_service_name)
            self.estop_endpoint = EstopEndpoint(self.estop_client, 'GNClient', 9.0)
            self.robot.logger.info("Estop-Client and Estop-endpoint created")
        except:
            # Not the estop
            self.estop_client = None
            self.estop_endpoint = None
            self.robot.logger.info("Not Estop_Endpoint")
        # Create Power Client
        self.power_client = robot.ensure_client(PowerClient.default_service_name)
        robot.logger.info("Power-Client created")
        # Create Robot Command Client
        self.robot_command_client = robot.ensure_client(RobotCommandClient.default_service_name)
        robot.logger.info("Robot-Command-Client created")
        # Create estop-keepalive, robot_id, lease and lease_keepalive
        # Set to None for later use
        self.estop_keepalive = None

        self.robot_id = None
        self.lease = None
        self.lease_keepalive = None

    # Performs all actions needed before the robot can power on
    def start(self):
        self.robot.logger.info("Starting Lease")
        # Taking Ownership of the robot
        self.lease = self.lease_client.acquire()
        self.lease_keepalive = LeaseKeepAlive(self.lease_client)
        self.robot.logger.info("Lease-KeepAlive started")
        # Getting robot_id for use in later versions
        self.robot.logger.info("Getting robot_id")
        self.robot_id = data_aquisition.get_id(self.robot)
        # Setting up E-Stop
        self.robot.logger.info("Setting Estop as sole estop")
        if self.estop_endpoint is not None:
            self.estop_endpoint.force_simple_setup()

    # Performs all actions needed to release the robot
    def shutdown(self):
        self.robot.logger.info("Shutting down Lease etc.")
        # Shutting down the E-Stop
        if self.estop_keepalive:
            self.estop_keepalive.shutdown()
            self.estop_keepalive = None
            self.robot.logger.info("Estop_Keepalive shutdown")
        # Returning the lease and releasing the robot
        if self.lease:
            self.lease_client.return_lease(self.lease)
            self.lease_keepalive.shutdown()
            self.lease = None
            self.lease_keepalive = None
            self.robot.logger.info("Lease returned")

    # turns E-Stop on and off
    def toggle_estop(self):
        self.robot.logger.info("Toggling estop")
        if self.estop_client is not None and self.estop_endpoint is not None:
            if not self.estop_keepalive:
                self.estop_keepalive = EstopKeepAlive(self.estop_endpoint)
                self.estop_keepalive.allow()
                assert not self.robot.is_estopped()
                self.robot.logger.info("Estop_Keepalive On")
                return True
            else:
                self.estop_keepalive.shutdown()
                self.estop_keepalive = None
                self.robot.logger.info("Estop_Keepalive Off")
                return False

    # Turns power on and off
    def toggle_power(self):
        # if robot is powered on, turn power off
        if self.robot.is_powered_on():
            self.robot.logger.info("Powering Off Robot safely")
            self.robot.power_off(cut_immediately=False, timeout_sec=20)
            assert not self.robot.is_powered_on(), "Robot power off failed"
            self.robot.logger.info("Robot powered off")
            return False
        # if robot is powered off, turn power on
        else:
            self.robot.logger.info("Powering On Robot")
            self.robot.power_on(timeout_sec=20)
            assert self.robot.is_powered_on(), "Robot power on failed"
            self.robot.logger.info("Robot powered on")
            return True

    # create stand-command and send it to the robot
    def stand(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_stand_command()
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(cmd)
        self.robot.logger.info("Robot standing")

    # create sit-command and send it to the robot
    def sit(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_sit_command()
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(cmd)
        self.robot.logger.info("Robot sitting")

    # create move forward-command and send it to the robot
    def move_forward(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_velocity_command(v_x=VELOCITY_BASE_SPEED, v_y=0.0, v_rot=0.0)
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(command=cmd, end_time_secs=time.time() + VELOCITY_CMD_DURATION)
        self.robot.logger.info("Robot moving forward")

    # create move backwards-command and send it to the robot
    def move_backwards(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_velocity_command(v_x=-VELOCITY_BASE_SPEED, v_y=0.0, v_rot=0.0)
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(command=cmd, end_time_secs=time.time() + VELOCITY_CMD_DURATION)
        self.robot.logger.info("Robot moving backwards")

    # create move left-command and send it to the robot
    def move_left(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_velocity_command(v_x=0.0, v_y=VELOCITY_BASE_SPEED, v_rot=0.0)
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(command=cmd, end_time_secs=time.time() + VELOCITY_CMD_DURATION)
        self.robot.logger.info("Robot moving left")

    # create move right-command and send it to the robot
    def move_right(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_velocity_command(v_x=0.0, v_y=-VELOCITY_BASE_SPEED, v_rot=0.0)
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(command=cmd, end_time_secs=time.time() + VELOCITY_CMD_DURATION)
        self.robot.logger.info("Robot moving right")

    # create turn left-command and send it to the robot
    def turn_left(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_velocity_command(v_x=0.0, v_y=0.0, v_rot=VELOCITY_BASE_ANGULAR)
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(command=cmd, end_time_secs=time.time() + VELOCITY_CMD_DURATION)
        self.robot.logger.info("Robot turning left")

    # create turn right-command and send it to the robot
    def turn_right(self):
        # Create command
        cmd = RobotCommandBuilder.synchro_velocity_command(v_x=0.0, v_y=0.0, v_rot=-VELOCITY_BASE_ANGULAR)
        # Send command to the robot via the robot_command_client
        self.robot_command_client.robot_command(command=cmd, end_time_secs=time.time() + VELOCITY_CMD_DURATION)
        self.robot.logger.info("Robot turning left")
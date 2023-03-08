# Retrieving Data from the robot, one of id, state, hardware or metrics


# Retrieves and returns the robot-id
# in the form of a protobuf-message found in robot_id.proto
def get_id(robot):
    # create robot-id-client
    id_client = robot.ensure_client('robot-id')
    robot.logger.info("ID-Client created")
    # retrieve data
    robot_id = id_client.get_id()
    return robot_id


# Retrieves and returns the robot-state data
# in the form of a protobuf-message found in robot_state.proto
def get_state(robot):
    # create robot-id-client
    state_client = robot.ensure_client('robot-state')
    robot.logger.info("State-Client created")
    # retrieve data
    robot_state = state_client.get_robot_state()
    return robot_state


# Retrieves and returns the robot-hardware-configuration data
# in the form of a protobuf-message found in robot_state.proto
def get_hardware(robot):
    # create robot-id-client
    robot_hardware_client = robot.ensure_client('robot-state')
    robot.logger.info("Hardware-Client created")
    # retrieve data
    robot_hardware = robot_hardware_client.get_robot_hardware_configuration()
    return robot_hardware


# Retrieves and returns the robot-metrics data
# in the form of a protobuf-message found in robot_state.proto
def get_metrics(robot):
    # create robot-id-client
    robot_metrics_client = robot.ensure_client('robot-state')
    robot.logger.info("Metrics-Client created")
    # retrieve data
    robot_metrics = robot_metrics_client.get_robot_metrics()
    return robot_metrics

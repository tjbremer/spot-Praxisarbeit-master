import logging
from concurrent import futures

from google.protobuf.timestamp_pb2 import Timestamp
import grpc
import SpotGlove_pb2
import SpotGlove_pb2_grpc
import base_config
import move_robot
import data_aquisition

robot_object = None
move_robot_object = None
spotStands = False


class SpotGloveServicer(SpotGlove_pb2_grpc.CommandSpotServicer):

    def Command(self, request, context):
        errorCode = 0
        result = True
        global spotStands
        if request.name == "stand" and spotStands is False:
            print("Spot needs to stand")
            move_robot_object.stand()
            spotStands = True
        elif request.name == "sit" and spotStands is True:
            print("Spot needs to sit")
            move_robot_object.sit()
            spotStands = False
        elif request.name == "shutdown":
            if robot_object.is_powered_on():
                move_robot_object.toggle_power()
            move_robot_object.shutdown()
            spotStands = False
        elif request.name == "estop_set":
            if move_robot_object.estop_keepalive:
                move_robot_object.toggle_estop()
                spotStands = False
            else:
                result = False
        elif request.name == "estop_remove":
            if not move_robot_object.lease:
                move_robot_object.start()
            if not move_robot_object.estop_keepalive:
                move_robot_object.toggle_estop()
            else:
                result = False
            if not robot_object.is_powered_on():
                move_robot_object.toggle_power()
        elif request.name == "move_forward" and spotStands is True:
            move_robot_object.move_forward()
        elif request.name == "move_backwards":
            move_robot_object.move_backwards()
        elif request.name == "move_left" and spotStands is True:
            move_robot_object.move_left()
        elif request.name == "move_right" and spotStands is True:
            move_robot_object.move_right()
        elif request.name == "turn_left" and spotStands is True:
            move_robot_object.turn_left()
        elif request.name == "turn_right" and spotStands is True:
            move_robot_object.turn_right()
        else:
            print("Unknown Command or Command can not be executed")
            result = False
            errorCode = 1
        print("Command received")
        timestamp = Timestamp()
        timestamp.GetCurrentTime()
        print(data_aquisition.get_state(robot_object).battery_states)
        return SpotGlove_pb2.CommandReply(timestamp=timestamp, result=result, errorCode=errorCode)


def serve():
    print("starting Server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SpotGlove_pb2_grpc.add_CommandSpotServicer_to_server(SpotGloveServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    robot_object = base_config.connect_and_authenticate("admin", "m2v97q65dllv", "192.168.80.3")
    move_robot_object = move_robot.MoveRobot(robot_object)

    # Start Robot
    move_robot_object.start()
    move_robot_object.toggle_estop()
    move_robot_object.toggle_power()
    print(data_aquisition.get_state(robot_object).battery_states)
    serve()

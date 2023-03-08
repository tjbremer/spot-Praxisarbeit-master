import logging
from concurrent import futures
import time

from google.protobuf.timestamp_pb2 import Timestamp
import grpc
import SpotGlove_pb2
import SpotGlove_pb2_grpc
import roslibpy

spiritStands = False


class SpotGloveServicer(SpotGlove_pb2_grpc.CommandSpotServicer):

    def Command(self, request, context):
        errorCode = 0
        result = True
        global spiritStands
        if request.name == "stand" and spiritStands is False:
            print("Spot needs to stand")
            behaviorIDPublisher.publish({'data': 2})
            time.sleep(1)
            behaviorIDPublisher.publish({'data': 2})
            time.sleep(1)
            behaviorIDPublisher.publish({'data': 2})
            time.sleep(1)
            behaviorIDPublisher.publish({'data': 2})
            time.sleep(1)
            behaviorIDPublisher.publish({'data': 2})
            time.sleep(1)
            behaviorIDPublisher.publish({'data': 2})
            behaviorModePublisher.publish({'data': 1})
            spiritStands = True
        elif request.name == "sit" and spiritStands is True:
            print("Spot needs to sit")
            behaviorIDPublisher.publish({'data': 0})
            behaviorModePublisher.publish({'data': 0})
            spiritStands = False
        elif request.name == "move_forward":
            movePublisher.publish(roslibpy.Message({'linear': {'x': 0.5, 'y': 0.0, 'z': 1}, 'angular': {'x':0.0, 'y': 0.0, 'z': 0.0}}))
        elif request.name == "move_backwards":
            movePublisher.publish(roslibpy.Message({'linear': {'x': -0.5, 'y': 0.0, 'z': 1}, 'angular': {'x':0.0, 'y': 0.0, 'z': 0.0}}))
        elif request.name == "move_left":
            movePublisher.publish(roslibpy.Message({'linear': {'x': 0.0, 'y': 0.5, 'z': 1}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}}))
        elif request.name == "move_right":
            movePublisher.publish(roslibpy.Message({'linear': {'x': 0.0, 'y': -0.5, 'z': 1}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}}))
        elif request.name == "turn_left" and spiritStands is True:
            movePublisher.publish(roslibpy.Message({'linear': {'x': 0.0, 'y': 0.0, 'z': 1}, 'angular': {'x':0.0, 'y': 0.0, 'z': 0.5}}))
        elif request.name == "turn_right" and spiritStands is True:
            movePublisher.publish(roslibpy.Message({'linear': {'x': 0.0, 'y': 0.0, 'z': 1}, 'angular': {'x':0.0, 'y': 0.0, 'z': -0.5}}))
        elif request.name == "estop_set":
            movePublisher.publish(roslibpy.Message({'linear': {'x': 0.0, 'y': 0.0, 'z': 1}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}}))
        else:
            print("Unknown Command or Command can not be executed")
            result = True
            errorCode = 1
        print("Command received")
        timestamp = Timestamp()
        timestamp.GetCurrentTime()
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
    client = roslibpy.Ros(host='192.168.168.105', port=9090)
    client.run()
    print('Is ROS connected? ', client.is_connected)
    movePublisher = roslibpy.Topic(client, '/mcu/command/manual_twist', 'geometry_msgs/Twist')
    behaviorIDPublisher = roslibpy.Topic(client, '/command/setBehaviorId', 'std_msgs/UInt32')
    behaviorModePublisher = roslibpy.Topic(client, '/command/setBehaviorMode', 'std_msgs/UInt32')
    controlModePublisher = roslibpy.Topic(client, '/command/setControlMode', 'std_msgs/UInt32')

    time.sleep(5)
    behaviorIDPublisher.publish({'data': 1})
    behaviorModePublisher.publish({'data': 1})
    controlModePublisher.publish({'data': 180})
    print("tried to stand")
    time.sleep(10)
    behaviorIDPublisher.publish({'data': 0})
    behaviorModePublisher.publish({'data': 0})
    print("tried to sit")

    serve()

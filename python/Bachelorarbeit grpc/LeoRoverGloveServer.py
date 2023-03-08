import logging
from concurrent import futures

from google.protobuf.timestamp_pb2 import Timestamp
import grpc
import SpotGlove_pb2
import SpotGlove_pb2_grpc
import roslibpy


class SpotGloveServicer(SpotGlove_pb2_grpc.CommandSpotServicer):

    def Command(self, request, context):
        errorCode = 0
        result = True
        if request.name == "move_forward":
            talker.publish(roslibpy.Message({'linear': {'x': 0.5, 'y': 0.0, 'z': 0.0}, 'angular': {'x':0.0, 'y': 0.0, 'z': 0.0}}))
        elif request.name == "move_backwards":
            talker.publish(roslibpy.Message({'linear': {'x': -0.5, 'y': 0.0, 'z': 0.0}, 'angular': {'x':0.0, 'y': 0.0, 'z': 0.0}}))
        elif request.name == "move_left":
            talker.publish(roslibpy.Message({'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x':0.0, 'y': 0.0, 'z': 0.5}}))
        elif request.name == "move_right":
            talker.publish(roslibpy.Message({'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x':0.0, 'y': 0.0, 'z': -0.5}}))
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
    client = roslibpy.Ros(host='192.168.104.43', port=9090)
    client.run()
    print('Is ROS connected? ', client.is_connected)
    talker = roslibpy.Topic(client, '/cmd_vel', 'geometry_msgs/String')
    serve()

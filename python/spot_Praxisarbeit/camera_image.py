# Retrieving one Image at a time from the robot

import bosdyn.client
import bosdyn.client.util
from bosdyn.client.image import ImageClient
from bosdyn.api import image_pb2
import cv2
import numpy as np


# Method to retrieve and save an image from one the robots cameras
def get_image(robot, auto_rotate, image_source, image_service=ImageClient.default_service_name):
    # create image_client
    image_client = robot.ensure_client(image_service)
    robot.logger.info("Image-Client created")

    # capture image
    image_responses = image_client.get_image_from_sources([image_source])
    robot.logger.info("Image captured")
    for image in image_responses:
        num_bytes = 1  # Assume a default of 1 byte encodings.
        if image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_DEPTH_U16:
            dtype = np.uint16
            extension = ".png"
        else:
            if image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_RGB_U8:
                num_bytes = 3
            elif image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_RGBA_U8:
                num_bytes = 4
            elif image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_GREYSCALE_U8:
                num_bytes = 1
            elif image.shot.image.pixel_format == image_pb2.Image.PIXEL_FORMAT_GREYSCALE_U16:
                num_bytes = 2
            dtype = np.uint8
            extension = ".jpg"

        img = np.frombuffer(image.shot.image.data, dtype=dtype)
        if image.shot.image.format == image_pb2.Image.FORMAT_RAW:
            try:
                # Attempt to reshape array into a RGB rows X cols shape.
                img = img.reshape((image.shot.image.rows, image.shot.image.cols, num_bytes))
            except ValueError:
                # Unable to reshape the image data, trying a regular decode.
                img = cv2.imdecode(img, -1)
        else:
            img = cv2.imdecode(img, -1)

        if auto_rotate:
            if image.source.name[0:5] == "front":
                img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

            elif image.source.name[0:5] == "right":
                img = cv2.rotate(img, cv2.ROTATE_180)
            robot.logger.info("Image rotated")
        # Write image to file and return True for jpeg-image and False for png-image
        if extension == ".jpg":
            cv2.imwrite('image.jpg', img)
            image = cv2.imread('image.jpg')
            robot.logger.info("Image converted to jpg")
            return True
        else:
            cv2.imwrite('image.png', img)
            image = cv2.imread('image.png')
            robot.logger.info("Image converted to png")
            return False



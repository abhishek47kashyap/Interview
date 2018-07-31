
# This sensor library has classes for commonly used sensors in self-driving cars.
# Additional methods and sensors can be added as necessary.

# NOTE: Some of the sensors bear little resemblance to data formats from actual sensors.

import random
import numpy as np


class Lidar:
    def __init__(self):
        pass

    def get_lidar_data(self):
        return random.uniform(0.1, 200.0)  # simulated proximity readings


class Camera:

    def __init__(self):
        pass

    # These are random simulated images, coming in sequentially.
    # With an actual camera, the OpenCV libraries should be used:
    #
    # camera = cv2.VideoCapture(0)
    #
    # while(True):
    #     # frame-wise capture
    #     ret, frame = camera.read()

    def get_camera_data(self, x, y):
        rows, col = x, y  # number of rows and columns per image
        return np.random.randint(256, size=(3, rows, col))


class Speedometer:

    def __init__(self):
        pass

    def get_vehicle_speed(self, previous_speed):
        return random.randint(previous_speed - 2, previous_speed + 2)


class PositionEncoder:

    def __init__(self):
        pass

    def get_wheel_encoder_data(self, previous_value):
        position_increment = random.uniform(0.01, 0.04)
        return previous_value + position_increment  # simulating encoder values


class GPS:

    def __init__(self):
        pass

    # latitudes range from 0 to 90
    # longitudes range from 0 to 180
    def get_GPS_data(self, previous_location):
        current_location = [previous_location[0] + random.uniform(-0.1, 0.1),
                            previous_location[1] + random.uniform(-0.1, 0.1)]

        if current_location[0] > 90:
            current_location[0] = current_location[0] - 90
        if current_location[0] < 0:
            current_location[0] = 90 - current_location[0]
        if current_location[1] > 180:
            current_location[1] = current_location[1] - 180
        if current_location[1] < 0:
            current_location[1] = 180 - current_location[1]

        return current_location


class IMU:

    def __init__(self):
        pass

    # simulates [a_x, a_y, a_z, g_x, g_y, g_z]
    def get_IMU_data(self):
        return np.random.uniform(low=-1.0, high=1.0, size=(1, 6))
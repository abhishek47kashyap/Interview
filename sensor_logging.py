# creating sensor framework

import sensor_library
import matplotlib.pyplot as plt
import numpy as np

# initializing sensor objects
overhead_LIDAR = sensor_library.Lidar()
wheel_1 = sensor_library.PositionEncoder()
wheel_2 = sensor_library.PositionEncoder()
wheel_3 = sensor_library.PositionEncoder()
wheel_4 = sensor_library.PositionEncoder()
front_camera = sensor_library.Camera()
gps = sensor_library.GPS()
imu = sensor_library.IMU()
vehicle_speed = sensor_library.Speedometer()

time_stamp = 1   # counter to acquire sensor data.

# initializing data storage lists
# some sensors keep track of previous values to generate more realistic simulated data
lidar_readings = []
wheel_1_readings, wheel_2_readings, wheel_3_readings, wheel_4_readings = \
    [[0, 0.0]], [[0, 0.0]], [[0, 0.0]], [[0, 0.0]]
gps_readings = [[35.6895, 139.6917]]
imu_readings = []
speedometer_readings = [[0, 40]]

# creating visualization windows
plt.ion()
fig_lidar = plt.figure('LIDAR readings')
ax_lidar = fig_lidar.add_subplot(111)
ax_lidar.set_ylim(-10, 210)
ax_lidar.set_title('Simulated LIDAR readings from get_lidar_data()')
ax_lidar.set_xlabel('Timestamps')
ax_lidar.set_ylabel('LIDAR readings')
line_lidar, = ax_lidar.plot([], [], 'r-')

fig_speedometer = plt.figure('Vehicle speed')
ax_speedometer = fig_speedometer.add_subplot(111)
ax_speedometer.set_title('Simulated speedometer readings from get_vehicle_speed()')
ax_speedometer.set_xlabel('Timestamps')
ax_speedometer.set_ylabel('Speedometer readings')
plt.grid(True)
line_speedometer, = ax_speedometer.plot([], [], 'b-')

fig_camera = plt.figure('Camera')

try:
    while 1:

        # Lidar readings
        lidar_readings.append([time_stamp, overhead_LIDAR.get_lidar_data()])
        x = [item[0] for item in lidar_readings[-50:]]
        y = [item[1] for item in lidar_readings[-50:]]
        line_lidar.set_xdata(x)
        line_lidar.set_ydata(y)
        ax_lidar.set_xlim(x[0], x[-1])
        # fig_lidar.canvas.draw()

        # Wheel position encoder readings
        wheel_1_readings.append([time_stamp,
                                 wheel_1.get_wheel_encoder_data(wheel_1_readings[-1][1])])
        wheel_2_readings.append([time_stamp,
                                 wheel_2.get_wheel_encoder_data(wheel_2_readings[-1][1])])
        wheel_3_readings.append([time_stamp,
                                 wheel_3.get_wheel_encoder_data(wheel_3_readings[-1][1])])
        wheel_4_readings.append([time_stamp,
                                 wheel_4.get_wheel_encoder_data(wheel_4_readings[-1][1])])

        # GPS readings
        gps_readings.append(gps.get_GPS_data(gps_readings[-1]))

        # Speedometer readings
        speedometer_readings.append([time_stamp,
                                     vehicle_speed.get_vehicle_speed(speedometer_readings[-1][1])])
        x = [item[0] for item in speedometer_readings[-50:]]
        y = [item[1] for item in speedometer_readings[-50:]]
        line_speedometer.set_xdata(x)
        line_speedometer.set_ydata(y)
        ax_speedometer.set_ylim(max(y)-25, min(y)+25)
        ax_speedometer.set_xlim(x[0], x[-1])
        # fig_speedometer.canvas.draw()

        # IMU readings
        imu_readings.append(imu.get_IMU_data())

        # Camera readings (slows down execution)
        # plt.imshow(front_camera.get_camera_data(256, 256))
        # plt.axis('off')

        time_stamp = time_stamp + 1


except KeyboardInterrupt:
    plt.close('all')
    print("Program ended!")

    # Converting to numpy arrays to dump values into csv files

    wheel_1_readings = np.asarray(wheel_1_readings)
    wheel_2_readings = np.asarray(wheel_2_readings)
    wheel_3_readings = np.asarray(wheel_3_readings)
    wheel_4_readings = np.asarray(wheel_4_readings)

    wheel_readings = np.concatenate((wheel_1_readings, wheel_2_readings[:, [1]],
                                     wheel_3_readings[:, [1]], wheel_4_readings[:, [1]]), axis=1)

    wheel_readings = np.delete(wheel_readings, 0, axis=0)  # deleting first row: timestamp = 0

    gps_readings = np.asarray(gps_readings)
    imu_readings = np.asarray(imu_readings)

    np.savetxt("wheel_encoder_readings.csv", wheel_readings, delimiter=",")
    np.savetxt("gps_readings.csv", gps_readings, delimiter=",")
    np.savetxt("imu_readings.csv", imu_readings, delimiter=";")

    print("Written data to csv files")

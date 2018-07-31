# creating sensor framework

import sensor_library
import matplotlib.pyplot as plt

# initializing sensor objects
overhead_LIDAR = sensor_library.Lidar()
wheel_1 = sensor_library.PositionEncoder()
wheel_2 = sensor_library.PositionEncoder()
wheel_3 = sensor_library.PositionEncoder()
wheel_4 = sensor_library.PositionEncoder()
front_camera = sensor_library.Camera()   # 100 readings from the front camera per second
bumper_camera = sensor_library.Camera()    # 50 readings from the bumper camera per second
gps = sensor_library.GPS()
imu = sensor_library.IMU()
vehicle_speed = sensor_library.Speedometer()  # 100 readings from the speedometer per second

time_stamp = 1   # counter to acquire sensor data.

# initializing data storage lists
# some sensors keep track of previous values for more realistic simulated sensor data
lidar_readings = []
wheel_1_readings, wheel_2_readings, wheel_3_readings, wheel_4_readings = \
    [[0, 0.0]], [[0, 0.0]], [[0, 0.0]], [[0, 0.0]]
gps_readings = [[0, [35.6895, 139.6917]]]
imu_readings = []
speedometer_readings = [[0, 40]]

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

try:
    while 1:

        # Lidar readings

        lidar_readings.append([time_stamp, overhead_LIDAR.get_lidar_data()])
        x = [item[0] for item in lidar_readings[-100:]]
        y = [item[1] for item in lidar_readings[-100:]]

        line1, = ax.plot(x, y, 'b-')
        line1.set_xdata(x)
        line1.set_ydata(y)
        plt.xlim(x[0], x[-1])
        fig.canvas.draw()

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
        gps_readings.append([time_stamp, gps.get_GPS_data(gps_readings[-1][1])])

        # Speedometer readings
        speedometer_readings.append([time_stamp,
                                     vehicle_speed.get_vehicle_speed(speedometer_readings[-1][1])])

        # IMU readings
        imu_readings.append([time_stamp, imu.get_IMU_data()])

        time_stamp = time_stamp + 1

        # if time_stamp >= 11:
        #     print x
        #     print y
        #     break

        # print time_stamp

except KeyboardInterrupt:
    print("Program ended!")

## Interview

`sensor_logging.py` is the main sensor platform which imports `sensor_library.py` which has classes for commonly used sensors in self-driving cars: LiDAR, Camera, Wheel Position Encoders, GPS, IMU.`sensor_logging.py` publishes LiDAR, Camera, and Speedometer readings to `pyplot` figures and the Positions Encoders, GPS, and IMU readings to .csv files. A total of 3 .csv files are created: *gps_readings.csv*, *imu_readings.csv*, and *wheel_encoder_readings.csv*.

`time_stamp` is not preserved for the sensors dumping their values into csv files as the row numbers themselves correspond to the time instances. The sole purpose of `time_stamp` is to visualize data in "real-time".

**To run the program:**<br/>
Python version used: 2.7.12<br/>
IDE used while writing this code: PyCharm<br/>
Have both `sensor_logging.py` and `sensor_library.py` in the same folder. Fire up your terminal, go to the folder where you stored the files, and type `python sensor_logging.py`.

**PROBLEMS with `sensor_logging.py`:**
- If the `pyplot` figure objects are used to visually represent data, hitting the 'Stop' button is not interpreted as `KeyboardInterrupt`, resulting in the Encoder, GPS, and IMU sensors not dumping their readings into .csv files. <br/>Commenting out the lines `fig_lidar.canvas.draw()` in the section `# Lidar readings`, `fig_speedometer.canvas.draw()` in `# Speedometer readings`, and `plt.imshow(front_camera.get_camera_data(256, 256))` followed by `plt.axis('off')` in `# Camera readings` allows the .csv files to be created successfully.
- The block `# Camera readings` slows down the program.

# SEN0311 (Ultrasonic) Sensor Node

This directory contains the ESPHome configuration for the DFRobot SEN0311 Ultrasonic distance sensor (uses `a02yyuw` platform).

## ROS 2 Node
The corresponding ROS 2 node for this sensor is `sen0311_node`. It polls the ESPHome web server to retrieve distance measurements and publishes them as a `sensor_msgs/Range` message.

- **ESPHome Endpoint:** `/sensor/distance`
- **Output Topic:** `/sen0311/Distance` (Range in meters)
- **Frame ID:** `sen0311_link`

### Usage
Run the node using:
```bash
colcon build
source install/setup.bash
ros2 run sen0311_node sen0311_driver --ros-args -p sensor_ip:="192.168.40.20"
```

# SEN0311 (Ultrasonic) Sensor Node

This directory contains the ESPHome configuration for the DFRobot SEN0311 Ultrasonic distance sensor (uses `a02yyuw` platform).

## ROS 2 Node
The corresponding ROS 2 node for this sensor is `sen0311_node`. It polls the ESPHome web server to retrieve distance measurements and publishes them as a `sensor_msgs/Range` message.

- **Default IP:** `192.168.105.67`
- **ESPHome Endpoint:** `/sensor/distance`
- **Output Topic:** `/sen0311/distance` (Range in meters)
- **Frame ID:** `sen0311_link`

### Usage
Run the node using:
```bash
source /mnt/c/KM/ROS2-Sensor-Nodes-RVZ/install/setup.bash
ros2 run rovozci_glsensor sen0311_node --ros-args -p sensor_ip:="192.168.105.67"
```

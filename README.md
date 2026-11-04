# SEN0311 (Ultrasonic) Sensor Node

This directory contains the ESPHome configuration for [DFRobot's SEN0311 Ultrasonic distance sensor](https://www.dfrobot.com/product-1935.html)
(uses the ESPHome platform `a02yyuw` platform), UART, 4.5m range, IP67.

## Directory Structure

- `firmware/`: Contains the ESPHome configuration (`atomlite-distance.yaml`)
  and related files for the
  [Atom Lite board](https://shop.m5stack.com/products/atom-lite-esp32-development-kit).
- `ros_node/`: Contains the `sen0311_driver` ROS 2 package to fetch data from
  the sensor over HTTP.

## Setup instruction

1. (Recommended, not necessary) Connect the M5 Atom Lite to a pc and flash it with the factory firmware
2. Go to 'web.esphome.io', and connect to your desired Wi-Fi network. Check the
   device IP and possibly modify `firmware/atomlite-distance.yaml` and
   `ros_node/sen0311_driver/sen0311_node.py` to reflect this
3. Compile and run the firmware using pixi (cf. below)
4. Verify that the device runs properly, either by checking the web server,
   endpoint (`curl -s http://<device_ip>/sensor/distance`) or ROS node (if
   something isn't working, I recommend debugging in this order)


## Wiring

- For wiring instructions see https://docs.m5stack.com/en/core/Atom-Lite,
https://docs.m5stack.com/en/accessory/cable/grove_cable, and
'https://wiki.dfrobot.com/sen0311/#tech_specs'.

| Cable Color Sensor  | Sensor Label | Groove Cable Color | Atom Lite Pin  | ESPHome Label |
| ------------------- | ------------ | ------------------ |--------------- |---------------|
| Red                 | VCC          | Red                | 5V             | -             |
| Black               | GND          | Black              | GND            | -             |
| Yellow              | RX           | Yellow             | G32            | rx_pin        |
| White               | TX           | White              | G26            | tx_pin        |

## Network Configuration

The sensor is configured to use a static IP address (`192.168.105.70`) on a
private network, which credentials must be set in `firmware/secrets.yaml`.
To switch to a different network, update the `secrets.yaml` and provide Wi-Fi
credentials or use the ESPHome captive portal that will be available when the
device cannot connect to the configured network.

Format of `secrets.yaml`:
```yaml
wifi_ssid: "YourWiFiSSID"
wifi_password: "YourWiFiPassword"
```

## Build and Flash Instructions

```bash
pixi run compile
pixi run upload
```

## ROS 2 Node

The corresponding ROS 2 node for this sensor is `sen0311_node`. It polls the
ESPHome web server to retrieve distance measurements and publishes them as a
`sensor_msgs/Range` message.

- **ESPHome Endpoint:** `/sensor/distance`
- **Output Topic:** `/sen0311/range`
- **Frame ID:** `sen0311_link`, configurable via ROS parameter `frame_id`

### Usage

Run the node using:
```bash
colcon build
source install/setup.bash
ros2 run sen0311_node sen0311_driver --ros-args -p sensor_ip:="192.168.40.20"
```
# Setup instruction
1. (Reccomended, not necesary) Connect the M5 Atom Lite to a pc and flash it with the factory firmware
2. Go to 'web.esphome.io', and connect to your desired wifi network. Check the device ip and modify 'firmware/atomlite-distance.yaml' and  'ros_node\sen0311_driver\sen0311_node.py' to reflect this
3. Compile and run the firmware using pixi 
'pixi run compile'
'pixi run upload --device {ip_address}'
4. Verify that the device runs properly, either by checking the web server, endpoint or ros node (if something isn't working, i reccommend debuging in this order)

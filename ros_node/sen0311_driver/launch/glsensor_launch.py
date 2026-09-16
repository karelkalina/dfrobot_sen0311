"""Launch file for the GL sensor node."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('sensor_ip', default_value='192.168.110.144',
                              description='IP address of the GL distance sensor'),
        DeclareLaunchArgument('frame_id', default_value='distance_sensor_link',
                              description='frame_id for the Range message'),
        DeclareLaunchArgument('poll_period', default_value='1.0',
                              description='Polling interval in seconds'),

        Node(
            package='rovozci_glsensor',
            executable='glsensor_node',
            name='glsensor_node',
            output='screen',
            parameters=[{
                'sensor_ip': LaunchConfiguration('sensor_ip'),
                'frame_id': LaunchConfiguration('frame_id'),
                'poll_period': LaunchConfiguration('poll_period'),
            }],
        ),
    ])

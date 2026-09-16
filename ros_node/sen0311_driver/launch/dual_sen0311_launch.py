from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rovozci_glsensor',
            executable='sen0311_node',
            name='sen0311_lift_node',
            parameters=[
                {'sensor_ip': '192.168.40.124'},
                {'frame_id': 'pallet_jack_lift_link'}
            ],
            remappings=[
                ('/sen0311/distance', '/sensors/lift_distance')
            ]
        ),
        Node(
            package='rovozci_glsensor',
            executable='sen0311_node',
            name='sen0311_forward_node',
            parameters=[
                {'sensor_ip': '192.168.40.105'},
                {'frame_id': 'forward_sensor_link'}
            ],
            remappings=[
                ('/sen0311/distance', '/sensors/forward_distance')
            ]
        )
    ])

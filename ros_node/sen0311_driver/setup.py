from setuptools import find_packages, setup

package_name = 'rovozci_glsensor'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/glsensor_launch.py', 'launch/dfrobot_launch.py', 'launch/dual_sen0311_launch.py']),
    ],
    install_requires=['setuptools', 'requests'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@example.com',
    description='ROS2 node for GL distance sensor over HTTP',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sen0311_node = rovozci_glsensor.sen0311_node:main',
        ],
    },
)

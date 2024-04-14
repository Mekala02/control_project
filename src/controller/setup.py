from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch"), glob("launch/*")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'state_publisher = controller.state_publisher:main',
            'waypoint_publisher = controller.waypoint_publisher:main',
            'waypoint_recorder = controller.waypoint_recorder:main',
            'pure_pursuit = controller.pure_pursuit:main',
            'stanley = controller.stanley:main',
            'pid = controller.pid:main',
        ],
    },
)

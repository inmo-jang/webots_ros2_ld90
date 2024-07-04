from setuptools import find_packages, setup

package_name = 'webots_ros2_ld90'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/protos', ['protos/LD90.proto']))
data_files.append(('share/' + package_name + '/protos', ['protos/LD90RearDistanceSensor.proto']))
data_files.append(('share/' + package_name + '/protos', ['protos/SickLms291.proto']))
data_files.append(('share/' + package_name + '/protos', ['protos/RPLidar.proto']))
data_files.append(('share/' + package_name + '/protos', ['protos/IntelRealSenseL515.proto']))
data_files.append(('share/' + package_name + '/protos/meshes', ['protos/meshes/LD_Platform.STL']))
data_files.append(('share/' + package_name + '/protos/meshes', ['protos/meshes/rplidar.dae']))
data_files.append(('share/' + package_name + '/protos/textures', ['protos/textures/sick_lms291_roughness.jpg']))
data_files.append(('share/' + package_name + '/protos/textures', ['protos/textures/sick_lms291.png']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/my_ld90.wbt']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/contest.wbt']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/no_human.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/ros2control.yaml']))
data_files.append(('share/' + package_name + '/resource', ['resource/LD90.urdf']))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name, ['package.xml']))


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='inmojang',
    maintainer_email='inmo3592@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

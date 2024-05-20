# webots_ros2_ld90

* URDF Source: [https://github.com/OmronAPAC/Omron_LD_ROS_Package](https://github.com/OmronAPAC/Omron_LD_ROS_Package)


![image](https://github.com/inmo-jang/webots_ros2_ld90/assets/42867523/abfe8694-f1bb-4448-94d9-75d692c491ae)


### How to use this

```
mkdir my_ros2_ws
cd my_ros2_ws
git clone https://github.com/inmo-jang/webots_ros2_ld90.git
git clone https://github.com/cyberbotics/webots_ros2.git
```
- Remove any unnecessary packages in `webots_ros2`, such as `webots_ros2_importer`

```
colcon build
source install/local_setup.bash
ros2 launch webots_ros2_ld90 robot_launch.py

```

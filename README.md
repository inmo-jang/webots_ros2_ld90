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

#### Webots with worlds
```
ros2 launch webots_ros2_ld90 robot_launch.py world:=no_human.wbt
```


#### Keyboard Teleoperation (Optional)
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

#### Rviz
At your workspace
```
ros2 run rviz2 rviz2 -d ./webots_ros2_ld90/resource/nav2_view.rviz
```

#### Nav2 with SLAM Mode
```
ros2 launch nav2_bringup bringup_launch.py params_file:=webots_ros2_ld90/resource/nav2_params.yaml map:=my_map.yaml slam:=True
```


#### Nav2 with Localisation Mode 
At your workspace
```
ros2 launch nav2_bringup bringup_launch.py params_file:=webots_ros2_ld90/resource/nav2_params.yaml map:=webots_ros2_ld90/resource/contest.yaml
```


Voxel Visualisation
```
ros2 run nav2_costmap_2d nav2_costmap_2d_markers voxel_grid:=/global_costmap/voxel_grid visualization_marker:=/global_cost_map_voxel

```

![image](https://github.com/inmo-jang/webots_ros2_ld90/assets/42867523/55ae909a-a74b-40fb-ba78-06a6bfac902c)
* This version can avoid unseen obstacles!


# Change Log
 
## 2024-07-04
  
### Added
- New worlds files: `contest.wbt` that has moving humans & `no-human.wbt` without the humans
- Map file for the new world: `contest.pgm`
- Two Side Lidars: using RPLidar
- `nav2_params.yaml` made by Group 1 of 2024 class at KAU

### Changed
- `ros2control.yaml`: `wheel_separation_multiplier` to improve `/odom`
 
### Fixed
- `LD90.proto`: rear casters' radius (boundingObject) as the robot didn't move
- `robot_launch.py`: Fixed and finalised ROSifying by following Inmo's lecture. 
- `nav2_params.yaml`: parameters tunned for collision avoidance

# To Do
- [ ] Side Lidar Visualisation Fix
- [ ] LD90 Visualisation Fix
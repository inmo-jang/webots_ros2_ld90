
# Change Log
 
## 2024-07-04
  
### Added
- New worlds files: `contest.wbt` that has moving humans & `no-human.wbt` without the humans

### Changed
- `ros2control.yaml`: `wheel_separation_multiplier` to improve `/odom`
 
### Fixed
- `LD90.proto`: rear casters' radius (boundingObject) as the robot didn't move
- `robot_launch.py`: Fixed and finalised ROSifying by following Inmo's lecture. 
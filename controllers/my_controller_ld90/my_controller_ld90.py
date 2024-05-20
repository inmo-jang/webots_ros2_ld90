from controller import Robot, DistanceSensor, Motor

# time in [ms] of a simulation step
TIME_STEP = 64
MAX_SPEED = 6.28
OBSTACLE_AVOIDANCE_DISTANCE = 0.15

# initialize the Webots API
robot = Robot()

# internal variables
avoid_obstacle_counter = 0


# initialize RotationalMotor
# https://cyberbotics.com/doc/reference/rotationalmotor?tab-language=python
wheels_names = [
    "left_wheel_joint", 
    "right_wheel_joint" 
]
wheels = [robot.getDevice(wheel_name) for wheel_name in wheels_names]
for wheel in wheels:
    wheel.setPosition(float('inf'))
    wheel.setVelocity(0.0)


# initialize PositionSensor
# https://cyberbotics.com/doc/reference/positionsensor?tab-language=python
js_names = [
    "left_wheel_joint_sensor", 
    "right_wheel_joint_sensor"]
js = [robot.getDevice(js_name) for js_name in js_names]
for joint_sensor in js:
    joint_sensor.enable(TIME_STEP)


# initialize Lidar
main_lidar = robot.getDevice('main_lidar')
main_lidar.enable(TIME_STEP)
main_lidar.enablePointCloud()

# initialize Rear DistanceSensors
ds_names = [
    "rear_sonar_1",
    "rear_sonar_2",
    "rear_sonar_3",
    "rear_sonar_4"        
]
ds = [robot.getDevice(ds_name) for ds_name in ds_names]
for distance_sensor in ds:
    distance_sensor.enable(TIME_STEP)

# feedback loop
while robot.step(TIME_STEP) != -1:
    # init speeds
    left_speed = 1.0
    right_speed = 1.0

    # if avoid_obstacle_counter > 0:
    #     avoid_obstacle_counter -= 1
    #     left_speed = 1.0
    #     right_speed = -1.0
    # else:
    #     # read sensors outputs 
    #     js_values = [js_value.getValue() for js_value in js]

    #     # increase counter in case of obstacle
    #     if js_values[0] < 950.0 or js_values[1] < 950.0:
    #         avoid_obstacle_counter = 100

    # write actuators inputs ########### 여기서 약간 이상해짐 ##########
    for i in range(len(wheels_names)):
        if i % 2 == 0:
            wheels[i].setVelocity(left_speed)
        else:
            wheels[i].setVelocity(right_speed)
# Rover
Gazebo and ROS simulation of Rover

## Authors
- [Gaurav Raut](https://github.com/gauraut) - M.Eng. Robotics student. 
- [Advait Patole](https://github.com/advaitp) - Graduate student at University of Maryland pursuing M.Eng. Robotics.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simulation Video Link https://youtu.be/IoMEVCYC8AU

Package Github link https://github.com/advaitp/rover

## Instructions to run the package
To start the simulation and the spawn the rover in the gazebo world
```
roslaunch rover rover.launch
```
Run the teleop node to send the rover near the object 
```
rosrun rover diff_teleop.py
```

To pickup the object
```
rosrun rover arm_control.py 3 4
```

To move the arm to top position in order to drop it at other position
```
rosrun rover arm_control.py 1 5
```

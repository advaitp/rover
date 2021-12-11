#!/usr/bin/env python3
from __future__ import print_function # Printing
import sys
import rospy # Python client library
import actionlib # ROS action library
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal # Controller messages
from std_msgs.msg import Float64 # 64-bit floating point numbers
from trajectory_msgs.msg import JointTrajectoryPoint # Robot trajectories
 
 
def move_robot_arm(joint_values):
  """
  Function to move the robot arm to desired joint angles.
  :param: joint_values A list of desired angles for the joints of a robot arm 
  """
  # Create the SimpleActionClient, passing the type of the action to the constructor
  arm_client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
 
  # Wait for the server to start up and start listening for goals.
  arm_client.wait_for_server()
     
  # Create a new goal to send to the Action Server
  arm_goal = FollowJointTrajectoryGoal()
 
  # Store the names of each joint of the robot arm
  arm_goal.trajectory.joint_names = ['shoulder_joint','bottom_wrist_joint' ,'elbow_joint', 'top_wrist_joint']
   
  # Create a trajectory point   
  point = JointTrajectoryPoint()
 
  # Store the desired joint values
  point.positions = joint_values
 
  # Set the time it should in seconds take to move the arm to the desired joint angles
  point.time_from_start = rospy.Duration(3)
 
  # Add the desired joint values to the goal
  arm_goal.trajectory.points.append(point)
 
  # Define timeout values
  exec_timeout = rospy.Duration(10)
  prmpt_timeout = rospy.Duration(5)
 
  # Send a goal to the ActionServer and wait for the server to finish performing the action
  arm_client.send_goal_and_wait(arm_goal, exec_timeout, prmpt_timeout)

def main(argv):
  rospy.init_node('arm_control')
  grip_pub = rospy.Publisher('/gripper_controller/command', Float64, queue_size=1000)
  for i in argv[1:]:
    if i=='1':
      move_robot_arm([0, 0.787, 0, 0.8])
      print("Arm Up!")

    elif i=='2':
      move_robot_arm([-0.4, 0.787, 0, 0.8])
      print("Arm Mid!")

    elif i=='3':
      move_robot_arm([-1.1, 0.787, 0, 1])
      print("Arm Down!")

    elif i=='4':
      grip_pub.publish(0.0)
      print("Gripper closed")

    elif i=='5':
      grip_pub.publish(0.8)
      print("Gripper open")

    else:
      print("Invalid input")

if __name__=='__main__':
  main(sys.argv)

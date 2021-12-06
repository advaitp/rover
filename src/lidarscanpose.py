#!/usr/bin/env python2.7
import numpy as np
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Point

global speed
speed = Twist()
x = 0
y = 0
theta = 0
align = False

def get_coordinates(msg):
	found = False
	storage = []
	for (index, dist) in enumerate(msg.ranges):
		if not found and dist<25:
			found = True
			storage.append(index)
		elif found  and dist>25:
			storage.append(index-1)
			break
	n = (storage[0]+storage[1])//2
	dist = msg.ranges[n]
	goal_theta = (0.25*n*np.pi)/180 - np.pi
	goal_x = dist*np.sin(goal_theta) - 0.08
	goal_y = dist*np.cos(goal_theta) - 0.2
	#goal_theta = np.arctan(goal_y/goal_x)
	c = [goal_x,goal_y,goal_theta]
	return c

def pos(msg):
	global x
	global y
	global theta

	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y

	rot_q = msg.pose.pose.orientation
	(roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def action(msg):
	global align
	coords = get_coordinates(msg)
	# rospy.loginfo(f"Found object at coordinates x: {coords[0]}, y: {coords[1]}. Now, moving")
	rospy.loginfo("Found object at coordinates x: %f" % coords[0])
	rospy.loginfo("Found object at coordinates y: %f" % coords[1])
	rospy.loginfo("Found object at theta: %f" % coords[2])
	odom = rospy.Subscriber("/mobile_base_controller/odom", Odometry, pos)
	vel = rospy.Publisher("/mobile_base_controller/cmd_vel", Twist, queue_size = 1)

	r = rospy.Rate(1000)

	goal = Point()
	goal.x = coords[0]
	goal.y = coords[1]

	while not rospy.is_shutdown():
		rospy.loginfo("My current pose: %f" % theta)
		if not align and abs(coords[2] - theta) > 0.08:
			speed.linear.x = 0
			speed.angular.z = -3.141
			vel.publish(speed)
			#rospy.loginfo("Aligning angle positive")
		elif msg.ranges[359] > 0.4:
			align == True
			speed.linear.x = -0.7
			speed.angular.z = 0
			vel.publish(speed)
			#rospy.loginfo("Moving forward")
		elif align and msg.ranges[359] < 0.4:
			speed.linear.x = 0
			speed.angular.z = 0
			vel.publish(speed)
			rospy.loginfo("Reached near object. Initiate arm.")
			break
	r.sleep()

if __name__=='__main__':
	rospy.init_node('vel_pub')
	sub = rospy.Subscriber('/laser/scan', LaserScan, action)
	rospy.spin()

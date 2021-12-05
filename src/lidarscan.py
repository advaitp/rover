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

def get_coordinates(msg):
	found = False
	storage = []
	for (index, dist) in enumerate(msg.ranges):
		if found == False and dist<25:
			found = True
			storage.append(index)
		elif found == True and dist>25:
			storage.append(index-1)
			break
	n = (storage[0]+storage[1])//2
	dist = msg.ranges[n]
	goal_theta = (0.25*n*np.pi)/180
	goal_x = dist*np.sin(theta)
	goal_y = dist*np.cos(theta)
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
	coords = get_coordinates(msg)
	# rospy.loginfo(f"Found object at coordinates x: {coords[0]}, y: {coords[1]}. Now, moving")
	rospy.loginfo("Found object at coordinates x: %f" % coords[0])
	rospy.loginfo("Found object at coordinates y: %f" % coords[1])
	odom = rospy.Subscriber("/mobile_base_controller/odom", Odometry, pos)
	vel = rospy.Publisher("/mobile_base_controller/cmd_vel", Twist, queue_size = 1)

	r = rospy.Rate(4)

	goal = Point()
	goal.x = coords[0]
	goal.y = coords[1]

	while not rospy.is_shutdown():
		inc_x = goal.x - x
		inc_y = goal.y - y

		if abs(coords[2] - theta) > 0.1:
			speed.linear.x = 0
			speed.angular.z = 0.3
		elif abs(coords[2] - theta) < 0.1 and msg.ranges[359] > 0.2:
			speed.linear.x = -0.7
			speed.angular.z = 0
		else:
			speed.linear.x = 0
			speed.angular.z = 0
			rospy.loginfo("Reached near object. Initiate arm.")
	vel.publish(speed)
	r.sleep()

if __name__=='__main__':
	rospy.init_node('vel_pub')
	sub = rospy.Subscriber('/laser/scan', LaserScan, action)
	rospy.spin()

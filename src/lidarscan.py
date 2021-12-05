#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def action(msg):
	print(len(msg.ranges))

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, action)
rospy.spin()

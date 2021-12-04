#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist 
import sys, select, termios, tty

msg = """
Control Your Batmobile!
---------------------------
Moving around:
		w
	a   s   d
		x
w : move forward
a : left turn
s : move back
d : right turn 
x : stop
space key, q : force stop
anything else : stop smoothly
"""

def getKey():
	tty.setraw(sys.stdin.fileno())
	rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
	if rlist:
		key = sys.stdin.read(1)
	else:
		key = ''

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

speed = 8
turn = 0.5

def vels(speed,turn):
	return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	rospy.init_node('teleop')
	
	front_wheel = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=10)
	pub_move = rospy.Publisher('/rear_drive_controller/command', Float64, queue_size=10)

	vel_msg = Twist()

	try:
		while(1):
			key = getKey()
			if key == 'w' :
				vel_msg.linear.x = -30.0
				front_wheel.publish(vel_msg) # publish the control speed. 
				pub_move.publish(-30.0) 

			elif key == 'a' :
				vel_msg.angular.z = 50.0
				front_wheel.publish(vel_msg)

			elif key == 's' :
				vel_msg.linear.x = 30.0
				front_wheel.publish(vel_msg) # publish tblish the control speed. 
				pub_move.publish(30.0) 

			elif key == 'd' :
				vel_msg.angular.z = -50.0
				front_wheel.publish(vel_msg)

			elif key == 'x' :
				vel_msg.angular.z = 0.0
				vel_msg.linear.x = 0.0
				front_wheel.publish(vel_msg)
				pub_move.publish(0.0) 

			elif key == 'q':
				break 

			else :
				vel_msg.angular.x = 0.0
				vel_msg.linear.x = 0.0
				front_wheel.publish(vel_msg)
				pub_move.publish(0.0) 

	except Exception as e:
		print (e)
		

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

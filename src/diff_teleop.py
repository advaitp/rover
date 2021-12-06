#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist 
import sys, select, termios, tty

msg = """
Control Your Rover!
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
	
	front_left = rospy.Publisher('/front_left_controller/command', Float64, queue_size=10)
	front_right = rospy.Publisher('/front_right_controller/command', Float64, queue_size=10)
	pub_move = rospy.Publisher('/rear_drive_controller/command', Float64, queue_size=10)

	vel_msg = Twist()
	r = rospy.Rate(10)

	try:
		while(1):
			key = getKey()
			if key == 'w' :
				# publish the control speed.
				front_left.publish(-20.0) 
				front_right.publish(-20.0) 
				pub_move.publish(-20.0) 

			elif key == 'a' :
				front_left.publish(30.0) 
				front_right.publish(-30.0) 
				pub_move.publish(-5.0) 

			elif key == 's' :
				front_left.publish(20.0) 
				front_right.publish(20.0) 
				pub_move.publish(20.0) 

			elif key == 'd' :
				front_left.publish(-30.0) 
				front_right.publish(30.0) 
				pub_move.publish(-5.0) 

			elif key == 'x' :
				front_left.publish(-0) 
				front_right.publish(0) 
				pub_move.publish(0) 

			elif key == 'q':
				break 

			else :
				front_left.publish(0) 
				front_right.publish(0) 
				pub_move.publish(0) 

		r.sleep()
		rospy.spin()

	except Exception as e:
		print (e)
		

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
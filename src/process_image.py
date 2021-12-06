import sys
import rospy
import cv2
from std_msgs.msg import String, Float64
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge, CvBridgeError

def drive_robot(vleft, vright, vrear) :
	rospy.loginfo("Moving the robot car")
	front_left = rospy.Publisher('/front_left_controller/command', Float64, queue_size=10)
	front_right = rospy.Publisher('/front_right_controller/command', Float64, queue_size=10)
	pub_move = rospy.Publisher('/rear_drive_controller/command', Float64, queue_size=10)

	front_left.publish(vleft)
	front_right.publish(vright)
	pub_move.publish(vrear)


def process_image_callback(img_msg) :
	rospy.loginfo("Starting process_image_callback") 
	red_pixel = 255 
	bridge = CvBridge()
	cv_image = bridge.imgmsg_to_cv2(img_msg, "bgr8")

	spotted = False 
	pos = []

	for i in range(cv_image.shape[0]) :
		for j in range(cv_image.shape[1]) :
			pixel = cv_image[j,i]
			# rospy.loginfo("Found object at blue x: %f" % pixel[0])
			# rospy.loginfo("Found object at green x: %f" % pixel[1])
			# rospy.loginfo("Found object at red x: %f" % pixel[2])
			if pixel[0] < 300 and pixel[1] > 0 and pixel[2] < 300 :
				spotted = True 
				# rospy.loginfo("Found object at coordinates x: %f" % cv_image.shape[0])
				pos = [i, j] 
			
	if not spotted : 
		drive_robot(0.0, 0.0, 0.0) 
	else :
		rospy.loginfo("Spotted")
		row = pos[0] ;
		col = pos[1] ;
		# GO LEFT
		if col < cv_image.shape[1]/3 :		
			rospy.loginfo("Moving LEFT")
			drive_robot(30.0, -30.0, 5.0) 

		# GO STRAIGHT
		elif col > cv_image.shape[1]/3 and col< (2*cv_image.shape[1]/3) :
			rospy.loginfo("Moving STRAIGHT")
			drive_robot(-20.0, -20.0, -20.0) 

		# GO RIGHT
		else :
			rospy.loginfo("Moving RIGHT") 
			drive_robot(-30.0, 30.0, -5.0) 
	

if __name__ == "__main__" :
	rospy.init_node('camera_node')
	rospy.loginfo("Starting process_image node") 
	sub = rospy.Subscriber("/camera/rgb/image_raw", Image, process_image_callback)
	rospy.spin()

	drive_robot(0.0, 0.0, 0.0)


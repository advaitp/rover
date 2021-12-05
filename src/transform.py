#!/usr/bin/env python2.7
import rospy
from geometry_msgs.msg import Pose
import tf2_ros
import tf2_geometry_msgs 


def transform_pose(input_pose, from_frame, to_frame):
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)

    pose_stamped = tf2_geometry_msgs.PoseStamped()
    pose_stamped.pose = input_pose
    pose_stamped.header.frame_id = from_frame
    pose_stamped.header.stamp = rospy.Time.now()

    try:
        output_pose_stamped = tf_buffer.transform(pose_stamped, to_frame, rospy.Duration(1))
        return output_pose_stamped.pose

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        raise


if __name__ == "__main__" :
    rospy.init_node("transform")

    my_pose = Pose()
    my_pose.position.x = -0.25
    my_pose.position.y = -0.50
    my_pose.position.z = +1.50
    my_pose.orientation.x = 0.634277921154
    my_pose.orientation.y = 0.597354098852
    my_pose.orientation.z = 0.333048372508
    my_pose.orientation.w = 0.360469667089

    transformed_pose = transform_pose(my_pose, "base_laser", "arn_base")

    print "New X position is: %f" % (transformed_pose.position.x)
    print "New Y position is: %f" % (transformed_pose.position.y)
    print "New Z position is: %f" % (transformed_pose.position.z)
    print "New X orientation is: %f" % (transformed_pose.orientation.x)
    print "New Y orientation is: %f" % (transformed_pose.orientation.y)
    print "New Z orientation is: %f" % (transformed_pose.orientation.z)
    print "New W orientation is: %f" % (transformed_pose.orientation.w)

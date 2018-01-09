#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

#ROS node that prints the distance to an obstacle directly in front of the robot

#scan_callback() prints the range measured to the object directly in front of the robot
def scan_callback(msg):

#by picking the middle element of the ranges field of the LaserScan message
range_ahead = msg.ranges[len(msg.ranges)/2]
print "range ahead: %0.1f" % range_ahead

rospy.init_node('range_ahead')
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
rospy.spin()

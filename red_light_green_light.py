#!/usr/bin/env python 
import rospy 
from geometry_msgs.msg import Twist

#Queue_size rospy will drop any messages beyond the queue size 
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) 
rospy.init_node('red_light_greeen_light')


#Robot will stop (all velocity subcomponents are zero)
red_light_twist = Twist()

#Robot will stop (all velocity subcomponents are zero)
green_light_twist = Twist()

#X component of linear velocity in a Twist message - Drive straight ahead in direction the robot is face at 0.5 meters / second
green_light_twist.linear.x = 0.5


driving_forward = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
if driving_forward:
cmd_vel_pub.publish(green_light_twist)
else:
cmd_vel_pub.publish(red_light_twist)


#Change behavior every 3 seconds from driving to stopping (rospy.Time measures the duration since last change in behavior)
if rospy.Time.now() > light_change_time: 
driving_forward = not driving_forward
light_change_time = rospy.Time.now() + rospy.Duration(3)

rate.sleep() 

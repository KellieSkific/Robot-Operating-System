#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#Import Twist and LaserScan

def scan_callback(msg):
  #global variable g_range_ahead stores the minimum range our laser scanner will detect in front of the robot
  global g_range_ahead
  g_range_ahead = min(msg.ranges)
  #scan_callback will then copy out the range to our global variable


g_range_ahead = 1 
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('wander')
state_change_time = rospy.Time.now()
driving_forward = True

#Rate to create loops to run at a mixed frequency - in this case 10Hz
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  if driving_forward:

    #drives forward until sees an obstacle within 0.8 meters or times out after 30 seconds
    if (g_range_ahead < 0.8 or rospy.Time.now() > state_change_time):
      driving_forward = False
      state_change_time = rospy.Time.now() + rospy.Duration(5)
   
  else: 
    #not in drive forward state - simply spins in place for 5 seconds then transitions back to driving forward 
    if rospy.Time.now() > state_change_time:
      driving_forward = True 
      state_change_time = rospy.Time.now() + rospy.Duration(30)
  
  twist = Twist()
  if driving_forward:
    twist.linear.x = 1
  else:
    twist.angular.z = 1
  cmd_vel_pub.publish(twist)

  rate.sleep()
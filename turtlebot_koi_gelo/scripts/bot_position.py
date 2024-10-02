#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

def callback(pos):
    
    
    str="Current position: x: {}, y:{}".format(pos.pose.pose.position.x, pos.pose.pose.position.y)
    
    pub.publish(str)

    rate.sleep()

if __name__=='__main__':

    rospy.init_node('position_subscriber',anonymous=True)
    pub=rospy.Publisher('/turtle_pos_xy', String, queue_size=10)
    rate=rospy.Rate(1)

    rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()

   
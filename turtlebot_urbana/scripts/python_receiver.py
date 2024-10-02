#!/usr/bin/env python3

import rospy
from turtlebot_urbana.msg import input_msg
from geometry_msgs.msg import Twist

class Receiver:
    def __init__(self)->None:
     
     rospy.init_node('python_subscriber', anonymous=True)
     
     self.pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)

     rospy.Subscriber('control_command', input_msg, self.cmd_clbk)

    def cmd_clbk(self,data):
     
     rospy.loginfo("Command received: {}".format(data))
     velocity=Twist()

     if data.dir =="forward":
       velocity.linear.x=data.vel
     
     elif data.dir =="backward":
       velocity.linear.x=-data.vel

     elif data.dir =="right":
       velocity.angular.z=data.vel

     elif data.dir =="left":
       velocity.angular.z=-data.vel

     self.pub.publish(velocity)

if __name__=='__main__':
    node= Receiver()
    rospy.spin()
     
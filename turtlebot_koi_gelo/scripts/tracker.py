#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from turtlebot_urbana.msg import input_msg


def clbk(cmd):
    rospy.loginfo("Given command is: {} {}".format(cmd.dir, cmd.vel))


if __name__=='__main__':
    rospy.init_node('tracker',anonymous=True)
    rospy.Subscriber('/control_command', input_msg, clbk)
    rospy.spin()
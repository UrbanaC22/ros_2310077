#!/usr/bin/env python3

import rospy
from turtlebot_urbana.msg import input_msg

class SendCommand:
    def __init__(self)->None:
        rospy.init_node('python_publisher', anonymous=True)

        self.pub=rospy.Publisher('control_command', input_msg, queue_size=10)

    def send(self, command):
        self.pub.publish(command)
        rospy.loginfo("Sending command: {}".format(command))

    def run(self):
        rospy.loginfo("Sending node is running...")

        while not rospy.is_shutdown():
            
            x, y=input("Enter command (e.g, forward 0.3): ").split()
            command = input_msg()
            command.dir=x
            command.vel=float(y)

            self.send(command)
            rospy.sleep(1)

if __name__=='__main__':
  node=SendCommand()
  node.run()
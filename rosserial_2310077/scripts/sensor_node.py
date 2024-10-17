#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

class sensor_node:

    def __init__(self) -> None:
        rospy.init_node('sensor_info', anonymous=True)

        self.pub=rospy.Publisher('/cmd_vel',Twist, queue_size=10)

        rospy.Subscriber('/sensor_data', Float32MultiArray, self.callback)

    def callback(self, sensor_data):
    
     velocity=Twist()

     velocity.linear.x=float(sensor_data[0])

    
     while sensor_data[1]<=20:
          velocity.linear.x=0
          velocity.angular.z=float(sensor_data[0])

     velocity.linear.x=float(sensor_data[0])


          
     self.pub.publish(velocity)

if __name__=='__main__':
   node= sensor_node()
   rospy.spin()


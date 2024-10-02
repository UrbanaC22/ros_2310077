#!/usr/bin/env python3

import rospy 
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class Obstacle_ache:

    def __init__(self)->None:
        rospy.init_node( 'obstacle_subscriber', anonymous= True)
        
        self.pub=rospy.Publisher('/obstacle', String, queue_size=10)
        
        rospy.Subscriber('/scan', LaserScan, self.callback)

        rospy.spin()

      
    def callback(self, obs):
        
        x=0
        for i in range(len(obs.ranges)):
           
          if (obs.ranges[i]<=30):
            x=x+1
        
        if x>0:
            str= "Obstacle Found"
            self.send(str)
               

    def send(self, str):
        self.pub.publish(str)
    
          
        
            
        
        
               

if __name__=='__main__':
    node= Obstacle_ache()
    rospy.spin()
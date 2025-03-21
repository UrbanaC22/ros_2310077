#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

battery=100
bat_pts=0

class bot_stats: 

   def __init__(self)->None:

    rospy.init_node('bot_info', anonymous=True)
    self.pub=rospy.Publisher('/rover_stats', Float32MultiArray, queue_size=10)
    rospy.Subscriber('/odom', Odometry, self.callback1)
    rospy.Subscriber('cmd_vel', Twist, self.callback2)
    self.rate=rospy.Rate(10)

   def callback1(self, msg):
       obtained_time=msg.header.stamp.to_sec()
       current_time=rospy.Time.now().to_sec()
       self.latency=current_time-obtained_time
       

   def callback2(self, msg):
        global battery
        global bat_pts
        
        final_data=Float32MultiArray()
        vx=msg.linear.x
        vz=msg.angular.z
        
        if vx!=0:
           velocity=vx
           bat_pts+=1
        

        elif vz!=0:
            velocity=vz
            bat_pts+=2
            
        
        else:
            velocity=0
            

        if bat_pts==5:
            battery-=1
            bat_pts=0

        rospy.loginfo(bat_pts)
        final_data.data=[battery, velocity, self.latency]
        
        
        self.pub.publish(final_data)
        rospy.loginfo("Battery: {}, Velocity: {}, Latency: {}".format(battery, velocity, self.latency))
        self.rate.sleep() 
 
   
        
if __name__=='__main__':
    node= bot_stats()
    rospy.spin()
        
        
        



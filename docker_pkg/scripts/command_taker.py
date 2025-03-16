#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from docker_pkg.msg import speech_msg

energy=100

class Receiver:
    def __init__(self)->None:
     
     rospy.init_node('command_receiver', anonymous=True)
     
     self.pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
 
     rospy.loginfo("Energy is: {}".format(energy))

     rospy.Subscriber('/speech_to_command', speech_msg, self.cmd_clbk)

    def cmd_clbk(self,data):
     global energy
     
     if data.dir=="forward" or data.dir=="backward" or data.dir=="right" or data.dir=="left" or data.dir=="kaboom":
      
      rospy.loginfo("Command received: {}".format(data))
      velocity=Twist()
      start_time=rospy.Time.now().to_sec()
      rate=rospy.Rate(1)

      if data.dir=="kaboom":
       energy+=1
       rospy.loginfo("Energy is: {}".format(energy))
       self.pub.publish(velocity)

     
     
      elif data.dir =="forward":
       velocity.linear.x=0.5
       
       while rospy.Time.now().to_sec()-start_time < data.time:
         self.pub.publish(velocity)
         energy-=1
         rospy.loginfo("Energy is: {}".format(energy))
         rate.sleep()
       velocity.linear.x=0
       self.pub.publish(velocity)


      elif data.dir =="backward":
       velocity.linear.x=-0.5
       
       while rospy.Time.now().to_sec()-start_time <data.time:
         self.pub.publish(velocity)
         energy-=1
         rospy.loginfo("Energy is: {}".format(energy))
         rate.sleep()
       velocity.linear.x=0
       self.pub.publish(velocity)


      elif data.dir =="right":
       velocity.angular.z=0.5
       
       while rospy.Time.now().to_sec()-start_time <data.time:
         self.pub.publish(velocity)
         energy-=1
         rospy.loginfo("Energy is: {}".format(energy))
         rate.sleep()
       velocity.angular.z=0
       self.pub.publish(velocity)

     
      elif data.dir =="left":
       velocity.angular.z=-0.5
       
       while rospy.Time.now().to_sec()-start_time <data.time:
         self.pub.publish(velocity)
         energy-=1
         rospy.loginfo("Energy is: {}".format(energy))
         rate.sleep()
       velocity.angular.z=0
       self.pub.publish(velocity)
     
     else:
        rospy.loginfo("Invalid command")
     

if __name__=='__main__':
    node= Receiver()
    rospy.spin()
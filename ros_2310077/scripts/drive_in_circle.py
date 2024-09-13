#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_in_circle():
    rospy.init_node('drive_in_circle', anonymous=True)
    
    # Create a publisher to the /cmd_vel topic
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Set the publishing rate
    rate = rospy.Rate(10)  # 10 Hz
    
    # Create a Twist message
    vel_msg = Twist()
    
    # Set linear velocity in the x direction
    vel_msg.linear.x = 1.0  # 1.0 m/s
    
    # Set angular velocity in the z direction
    vel_msg.angular.z = 1.0  # 1.0 rad/s
    
    rospy.loginfo("Starting to move the turtle in a circular path")
    
    # Keep publishing the velocity command until the node is shutdown
    while not rospy.is_shutdown():
        # Publish the velocity command
        pub.publish(vel_msg)
        
        # Log the published values
        rospy.loginfo(f"Linear Velocity: {vel_msg.linear.x}, Angular Velocity: {vel_msg.angular.z}")
        
        # Sleep for the remaining time to maintain the loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        move_in_circle()
    except rospy.ROSInterruptException:
        pass

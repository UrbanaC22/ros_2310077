#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray
import tkinter as tk


class gui_bot:

    def clbk(self, msg):
        self.bat=msg.data[0]
        self.vel=msg.data[1]
        self.lat=msg.data[2]

    def update_battery(self):
         new_bat=self.bat
         self.battery_var.set(new_bat)
         self.root.after(100, self.update_battery)

    def update_velocity(self):
         new_vel=self.vel
         self.velocity_var.set(new_vel)
         self.root.after(100, self.update_velocity)

    def update_latency(self):
         new_lat=self.lat
         self.latency_var.set(new_lat)
         self.root.after(100, self.update_latency)
    
    def __init__(self,root)->None:

        def move_forward(self):
            velocity=Twist()
            velocity.linear.x=0.5
            velocity.angular.z=0
            self.pub.publish(velocity)
            rospy.loginfo("Bot is moving forwards")
            self.rate.sleep()
        
        def move_backward(self):
            velocity=Twist()
            velocity.linear.x=-0.5
            velocity.angular.z=0
            self.pub.publish(velocity)
            rospy.loginfo("Bot is moving backwards")
            self.rate.sleep()
        
        def move_left(self):
            velocity=Twist()
            velocity.linear.x=0
            velocity.angular.z=0.5
            self.pub.publish(velocity)
            rospy.loginfo("Bot is turning left")
            self.rate.sleep()
        
        def move_right(self):
            velocity=Twist()
            velocity.linear.x=0
            velocity.angular.z=-0.5
            self.pub.publish(velocity)
            rospy.loginfo("Bot is turning right")
            self.rate.sleep()
        
        def stop(self):
            velocity=Twist()
            velocity.linear.x=0
            velocity.angular.z=0
            self.pub.publish(velocity)
            rospy.loginfo("Bot has stoppped")
            self.rate.sleep()

        


        self.root=root

        rospy.init_node('bot_info', anonymous=True)
        self.bat=100
        self.vel=0
        self.lat=0

        self.pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.subscriber=rospy.Subscriber('/rover_stats', Float32MultiArray, self.clbk)
        self.rate=rospy.Rate(10)
        
        self.battery_var= tk.DoubleVar()
        self.battery_var.set(self.bat)

        self.velocity_var= tk.DoubleVar()
        self.velocity_var.set(self.vel)

        self.latency_var= tk.DoubleVar()
        self.latency_var.set(self.lat)

        self.root.title("Robot Control App")
        self.root.geometry("800x400")
        self.root.minsize(500,300)
        self.root.configure(bg="#123456")

        self.button_forward= tk.Button(self.root, text="Forward", fg="black", highlightbackground="black", highlightthickness=1, bg="#FC8EAC", command=lambda: move_forward(self))
        self.button_forward.place(x=150, y=60, width=70, height=50)

        self.button_backward= tk.Button(self.root, text="Backward", fg="black", highlightbackground="black", highlightthickness=1, bg="#FC8EAC", command=lambda: move_backward(self))
        self.button_backward.place(x=150, y=280, width=70, height=50)

        self.button_left= tk.Button(self.root, text="Left", fg="black", highlightbackground="black", highlightthickness=1, bg="#FC8EAC", command=lambda: move_left(self))
        self.button_left.place(x=40, y=170, width=70, height=50)

        self.button_right= tk.Button(self.root, text="Right", fg="black", highlightbackground="black", highlightthickness=1, bg="#FC8EAC", command=lambda:move_right(self))
        self.button_right.place(x=260, y=170, width=70, height=50)

        self.button_stop= tk.Button(self.root, text="Stop", fg="black", highlightbackground="black", highlightthickness=1, bg="#FC8EAC", command=lambda: stop(self))
        self.button_stop.place(x=150, y=170, width=70, height=50)

        self.frame_bat= tk.Frame(self.root, width=160, height=40, highlightbackground="black", highlightthickness=1, bg="#FFEE8C")
        self.frame_bat.place(x=530, y=100)
        self.frame_bat.pack_propagate(False)
        self.label_bat1=tk.Label(self.frame_bat,text="Battery: ", bg="#FFEE8C")
        self.label_bat1.grid(row=0, column=0, padx=5, pady=5)
        self.label_bat2=tk.Label(self.frame_bat,textvariable=self.battery_var, bg="#FFEE8C")
        self.label_bat2.grid(row=0, column=1, padx=5, pady=5)


        self.frame_vel= tk.Frame(self.root, width=160, height=40, highlightbackground="black", highlightthickness=1, bg="#FFEE8C")
        self.frame_vel.place(x=530, y=180)
        self.frame_vel.pack_propagate(False)
        self.label_vel1=tk.Label(self.frame_vel,text="Velocity: ", bg="#FFEE8C")
        self.label_vel1.grid(row=0, column=0, padx=5, pady=5)
        self.label_vel2=tk.Label(self.frame_vel,textvariable=self.velocity_var, bg="#FFEE8C")
        self.label_vel2.grid(row=0, column=1, padx=10, pady=10)


        self.frame_lat= tk.Frame(self.root, width=160, height=40, highlightbackground="black", highlightthickness=1, bg="#FFEE8C")
        self.frame_lat.place(x=530, y=260)
        self.frame_lat.pack_propagate(False)
        self.label_lat1=tk.Label(self.frame_lat,text="Latency: ", bg="#FFEE8C")
        self.label_lat1.grid(row=0, column=0, padx=5, pady=5)
        self.label_lat2=tk.Label(self.frame_lat,textvariable=self.latency_var, bg="#FFEE8C")
        self.label_lat2.grid(row=0, column=2, padx=5, pady=5)

        self.update_battery()
        self.update_velocity()
        self.update_latency()
        
    
if __name__=='__main__':
    root= tk.Tk()
    app= gui_bot(root)
    root.mainloop()
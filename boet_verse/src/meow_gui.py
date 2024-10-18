#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import tkinter as tk


pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
x=10

def move_forward(dir,label_number):
    global x
    if x>=1:
        x-=1
        text_dir="Bot is moving Forward"
        msg=Twist()
        msg.linear.x=0.5
        
        rate=rospy.Rate(10)
        start_time=rospy.Time.now()
        while rospy.Time.now()-start_time<rospy.Duration(1):
         pub.publish(msg)
         rate.sleep()

        stop_command=Twist()
        stop_command.linear.x=0
        pub.publish(stop_command)

        rospy.loginfo("Button pressed:Forward")
        update_message_text(text_dir,dir)
        update_x(label_number)
        

def move_backward(dir,label_number):
    global x
    if x>=1:
        x-=1
        text_dir="Bot is moving Backward"
        msg=Twist()
        msg.linear.x=-0.5
        
        rate=rospy.Rate(10)
        start_time=rospy.Time.now()
        while rospy.Time.now()-start_time<rospy.Duration(1):
         pub.publish(msg)
         rate.sleep()

        stop_command=Twist()
        stop_command.linear.x=0
        pub.publish(stop_command)


        rospy.loginfo("Button pressed:Back")
        update_message_text(text_dir,dir)
        update_x(label_number)
        
    
def turn_right(dir,label_number):
    global x
    if x>=2:
        x-=2
        text_dir="Bot is turning Right"
        msg=Twist()
        msg.angular.z=-0.5
        
        rate=rospy.Rate(10)
        start_time=rospy.Time.now()
        while rospy.Time.now()-start_time<rospy.Duration(1):
         pub.publish(msg)
         rate.sleep()

        stop_command=Twist()
        stop_command.angular.z=0
        pub.publish(stop_command)


        rospy.loginfo("Button pressed:Right")
        update_message_text(text_dir,dir)
        update_x(label_number)  
        

def turn_left(dir,label_number):
    global x
    if x>=2:
        x-=2
        text_dir="Bot is turning Left"
        msg=Twist()
        msg.angular.z=0.5
        
        rate=rospy.Rate(10)
        start_time=rospy.Time.now()
        while rospy.Time.now()-start_time<rospy.Duration(1):
         pub.publish(msg)
         rate.sleep()

        stop_command=Twist()
        stop_command.angular.z=0
        pub.publish(stop_command)


        rospy.loginfo("Button pressed:Left")
        update_message_text(text_dir, dir)
        update_x(label_number)
    

def increase_meulas(dir,label_number):
    global x
    if x>=0 and x<=9:
        x+=1
        text_dir="Meula increased"
        msg=Twist()
        msg.linear.x=0
        msg.angular.z=1
        
        rate=rospy.Rate(10)
        start_time=rospy.Time.now()
        while rospy.Time.now()-start_time<rospy.Duration(7):
         pub.publish(msg)
         rate.sleep()

        stop_command=Twist()
        stop_command.angular.z=0
        pub.publish(stop_command)


        rospy.loginfo("Button pressed:Increase Meulas")
        update_message_text(text_dir, dir)
        update_x(label_number)
        

def update_message_text(text_dir,dir):
    global x
    if x>0:
     direction=text_dir
    else:
     direction="Error, no meulas"
    dir.set(direction)

def update_x(label_number):
    global x
    label_number.config(text=str(x))


def bot_controller():
  
    rospy.init_node("meow_control", anonymous=True)
    

    global x
 
    root= tk.Tk()
    root.title("BOETverse bot controller")
    root.geometry("500x400")
    root.minsize=(200,200)

    dir=tk.StringVar()
    dir.set("Welcome")

    frame_number=tk.Frame(root, width=40, height=40, highlightbackground="black", highlightthickness=1)
    frame_number.place(x=440, y=40)
    frame_number.pack_propagate(False)
    label_number=tk.Label(frame_number, text=str(x))
    label_number.pack(expand=True, fill="both")

    button_forward= tk.Button(root, text="Forward", highlightbackground="black", highlightthickness=1, command=lambda: move_forward(dir,label_number))
    button_forward.place(x=80, y=120, width=70, height=30)

    button_backward= tk.Button(root, text="Back",highlightbackground="black", highlightthickness=1, command=lambda: move_backward(dir,label_number))
    button_backward.place(x=80, y=250, width=70, height=30)

    button_right= tk.Button(root, text="Right",highlightbackground="black", highlightthickness=1, command=lambda: turn_right(dir,label_number))
    button_right.place(x=150, y=185, width=70, height=30)

    button_left= tk.Button(root, text="Left",highlightbackground="black", highlightthickness=1, command=lambda: turn_left(dir,label_number))
    button_left.place(x=10, y=185, width=70, height=30)

    frame_remaining= tk.Frame(root, width=140, height=40, highlightbackground="black", highlightthickness=1)
    frame_remaining.place(x=280, y=40)
    frame_remaining.pack_propagate(False)
    label_remaining= tk.Label(frame_remaining, text="Remaining Meulas:")
    label_remaining.pack(expand=True, fill="both")

    button_increase= tk.Button(root, text="Increase Meulas",highlightbackground="black", highlightthickness=1, command=lambda: increase_meulas(dir,label_number))
    button_increase.place(x=310, y=100, width=160, height=30)

    frame_message= tk.Frame(root, width=160, height=30, highlightbackground="black", highlightthickness=1)
    frame_message.place(x=280, y=250)
    frame_message.pack_propagate(False)
    label_message=tk.Label(frame_message, text="Message")
    label_message.pack(expand=True, fill="both")

    
    label_writing= tk.Label(root, textvariable=dir)
    label_writing.place(x=280, y=280, width=160, height=30)

    root.mainloop()

if __name__=="__main__":
    try: 
        bot_controller()
    except rospy.ROSInterruptException:
        pass
        
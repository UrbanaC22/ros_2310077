#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import tkinter as tk

class TeleopGUI:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400, 400)
        self.master.title("Turtlesim Teleop Controller")
        self.master.configure(bg='orange')

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)

        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.init_node('teleop_gui', anonymous=True)

        self.button_forward = tk.Button(master, text="Forward", width=10)
        self.button_forward.bind("<ButtonPress>", self.move_forward)
        self.button_forward.bind("<ButtonRelease>", self.stop)
        self.button_forward.grid(row = 0, column = 1, sticky = 'news', pady = 2)

        self.button_backward = tk.Button(master, text="Backward", width=10)
        self.button_backward.bind("<ButtonPress>", self.move_backward)
        self.button_backward.bind("<ButtonRelease>", self.stop)
        self.button_backward.grid(row = 2, column = 1, sticky = 'news', pady = 2)

        self.button_left = tk.Button(master, text="Left", width=10)
        self.button_left.bind("<ButtonPress>", self.move_left)
        self.button_left.bind("<ButtonRelease>", self.stop)
        self.button_left.grid(row = 1, column = 0, sticky = 'news', pady = 2)

        self.button_right = tk.Button(master, text="Right", width=10)
        self.button_right.bind("<ButtonPress>", self.move_right)
        self.button_right.bind("<ButtonRelease>", self.stop)
        self.button_right.grid(row = 1, column = 2, sticky = 'news', pady = 2)

    def move_forward(self, event):
        twist = Twist()
        twist.linear.x = 1.0
        self.pub.publish(twist)

    def move_backward(self, event):
        twist = Twist()
        twist.linear.x = -1.0
        self.pub.publish(twist)

    def move_left(self, event):
        twist = Twist()
        twist.angular.z = 1.0
        self.pub.publish(twist)

    def move_right(self, event):
        twist = Twist()
        twist.angular.z = -1.0
        self.pub.publish(twist)

    def stop(self, event):
        twist = Twist()
        self.pub.publish(twist)

if __name__ == "__main__":
    root = tk.Tk()
    app = TeleopGUI(root)
    root.mainloop()

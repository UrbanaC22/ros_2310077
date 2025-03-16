#!/usr/bin/env python3

import rospy
import speech_recognition as sr
from docker_pkg.msg import speech_msg
from std_msgs.msg import String
from word2number import w2n
 
def speech_recog():
    rospy.init_node('speech_input', anonymous=True)
    pub=rospy.Publisher('/speech_to_command', speech_msg, queue_size=10)
    mic=sr.Microphone()
    recog=sr.Recognizer()

    rospy.loginfo("Give a command:")

    while not rospy.is_shutdown():
       with mic as source:
        recog.adjust_for_ambient_noise(source)
        rospy.loginfo("Listening....")
        audio= recog.listen(source)

       try:
         cmd=recog.recognize_google(audio).lower().split()
         command=speech_msg()
         command.dir=cmd[0]
         if len(cmd)==1:
          command.time=2.0
         else:
           command.time=w2n.word_to_num(cmd[1])
         rospy.loginfo(command)
         pub.publish(command)
        
       except sr.UnknownValueError:
          rospy.logwarn("Could not understand command")

       except sr.RequestError:
          rospy.logwarn("Unable to implement command, check internet connection")

if __name__=='__main__':
   try:speech_recog()
   except rospy.ROSInterruptException:
    pass
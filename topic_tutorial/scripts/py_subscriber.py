#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def msgCallback(msg):
    rospy.loginfo("msg : %s", msg.data)

def listener():
    rospy.init_node("py_subscriber") #노드 이름 초기화

    #서브스크라이버 선언
    rospy.Subscriber("my_topic", String, msgCallback, queue_size=100) 
    #콜백함수에 자료형이 없어서 Subscriber에 자료형(String) 선언

    rospy.spin()

if __name__ == "__main__":
    listener()
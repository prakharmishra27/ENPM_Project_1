#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Float64

fr_angle=0.0 
fl_angle=0.0 
rear_speed=0.0

def fr_angle_com(msg):
  global fr_angle
  fr_angle= msg.data


def fl_angle_com(msg):
  global fl_angle
  fl_angle= msg.data


def rear_speed_com(msg):
  global rear_speed
  rear_speed= msg.data


def command_subcriber():
    while not rospy.is_shutdown():
        rospy.Subscriber(
            "front_right_steering_controller/command", Float64,
            callback=fr_angle_com)
        rospy.Subscriber(
            "front_left_steering_controller/command", Float64,
            callback=fl_angle_com)
        rospy.Subscriber(
            "rear_wheels_controller/command", Float64,
            callback=rear_speed_com)
        print("Moving in straight line with speed= " + str(rear_speed) )
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        rospy.init_node('mycar_drive_sub')
        command_subcriber()
    except rospy.ROSInterruptException:
        pass

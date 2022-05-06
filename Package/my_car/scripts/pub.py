#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import time

def straight():
    rate = rospy.Rate(200)  
    while not rospy.is_shutdown():
        front_right = rospy.Publisher(
            '/front_right_steering_controller/command',
            Float64,
            queue_size=1)
        front_left = rospy.Publisher(
            '/front_left_steering_controller/command',
            Float64,
            queue_size=1)
        rear = rospy.Publisher(
            '/rear_wheels_controller/command',
            Float64,
            queue_size=1)
        front_right.publish(angle)
        front_left.publish(angle)
        rear.publish(speed)
        print("Sending commands to move in a straight line")
        time.sleep(0.5)
        rate.sleep()


if __name__ == '__main__':
    try:
        angle = 0.0  
        speed = 5.0
        rospy.init_node('mycar_drive')
        straight()
    except rospy.ROSInterruptException:
        pass






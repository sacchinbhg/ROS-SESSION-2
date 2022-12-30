#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('straight_line_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    distance = int(input("How much distance do you want the bot to travel? "))

    vel_msg.linear.x = 2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.5

    while not rospy.is_shutdown():
        
        t0 = rospy.Time.now().to_sec()
        cur_distance = 0

        while(cur_distance < distance):
            velocity_publisher.publish(vel_msg)

            t1 = rospy.Time.now().to_sec()
            cur_distance = 2*(t1-t0)
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        exit()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: 
        pass
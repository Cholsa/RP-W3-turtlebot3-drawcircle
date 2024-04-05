#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def draw_circle():
    rospy.init_node('draw_circle_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    move_cmd = Twist()
    move_cmd.linear.x = 1.0
    move_cmd.angular.z = 1.0

    now = rospy.Time.now()
    duration = rospy.Duration.from_sec(6)

    while rospy.Time.now() < now + duration:
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        draw_circle()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def draw_star():
    rospy.init_node('draw_star_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    move_cmd = Twist()
    move_cmd.linear.x = 1.0

    for _ in range(5):
        # Move forward
        pub.publish(move_cmd)
        rospy.sleep(1.0)

        # Turn right (144 degrees)
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = -1.25  # Adjust this value for a perfect star
        pub.publish(move_cmd)
        rospy.sleep(1.0)

    # Stop
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        draw_star()
    except rospy.ROSInterruptException:
        pass

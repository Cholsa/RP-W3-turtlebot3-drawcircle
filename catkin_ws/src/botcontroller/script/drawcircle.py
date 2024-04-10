#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def draw_circle():
  rospy.init_node('draw_circle_node', anonymous=True)
  pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
  rate = rospy.Rate(10)

  move_cmd = Twist()
  # Adjust these values for desired circle size and speed
  move_cmd.linear.x = 0.2  # Small forward speed (optional)
  move_cmd.angular.z = 0.5  # Positive value for counter-clockwise turn (adjust for smoothness)

  while not rospy.is_shutdown():
    pub.publish(move_cmd)
    rate.sleep()

if __name__ == '__main__':
  try:
    draw_circle()
  except rospy.ROSInterruptException:
    pass

# -------------------------------------
import rospy
from geometry_msgs.msg import Twist

if __name__=="__main__":

    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    turtlebot3_model = rospy.get_param("model", "burger")

    status = 0
    target_linear_vel   = 0.0
    target_angular_vel  = 0.0
    control_linear_vel  = 0.0
    control_angular_vel = 0.0

# -------------------------------------

import rospy
from geometry_msgs.msg import Twist

def draw_circle():
    rospy.init_node('draw_circle_node', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
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
    turtlebot3_model = rospy.get_param("model", "burger")

    try:
        draw_circle()
    except rospy.ROSInterruptException:
        pass

# ---------------------------------------
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def draw_circle():
  # Initialize ROS node
  rospy.init_node('turtlebot3_draw_circle', anonymous=True)

  # Get angular velocity (rad/s) for desired circle radius (m)
  # Adjust velocity based on Burger's capabilities and desired circle size
  velocity = 0.5  # Adjust this value as needed

  # Create Twist publisher
  pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
  rate = rospy.Rate(10)

  # Create Twist message with linear velocity set to 0 and angular velocity set to calculated value
  twist = Twist()
  twist.linear.x = 0.0
  twist.angular.z = velocity

  # Publish Twist message repeatedly to make the robot turn
  while not rospy.is_shutdown():
    pub.publish(twist)
    rospy.sleep(1)  # Adjust sleep time as needed

if __name__ == '__main__':
  try:
    draw_circle()
  except rospy.ROSInterruptException:
    pass

# -------------------------------------

import rospy
from geometry_msgs.msg import Twist

def draw_star():
  rospy.init_node('draw_star_node', anonymous=True)
  pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
  # Service proxy for move_until_angle (replace with actual service name)
  move_until_angle_proxy = rospy.ServiceProxy('/move_to_angle', MoveToAngle)  # Replace with actual service type

  move_cmd = Twist()
  linear_speed = 0.5  # Adjust linear speed as needed

  # Star path definition (adjust angles and distances for desired shape)
  arm_length = 0.5  # Distance for each straight line segment
  angle_per_arm = 120  # Angle between each arm (adjust for number of points)

  # Move forward for first arm
  move_cmd.linear.x = linear_speed
  move_cmd.angular.z = 0.0
  # Publish for a duration to move forward
  duration = arm_length / linear_speed
  for _ in range(int(duration * rate.hz)):
    pub.publish(move_cmd)
    rate.sleep()

  # Loop for remaining arms
  for _ in range(4):
    # Call service to rotate for desired angle
    move_until_angle_proxy(target_angle=angle_per_arm)
    # Move forward for next arm segment
    move_cmd.linear.x = linear_speed
    move_cmd.angular.z = 0.0
    # Publish for a duration to move forward
    duration = arm_length / linear_speed
    for _ in range(int(duration * rate.hz)):
      pub.publish(move_cmd)
      rate.sleep()

if __name__ == '__main__':
  try:
    draw_star()
  except rospy.ROSInterruptException:
    pass

# ---------------------------------------------------------

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def draw_star():
  rospy.init_node('draw_star_node', anonymous=True)
  pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
  rate = rospy.Rate(10)

  move_cmd = Twist()
  linear_speed = 0.5  # Adjust linear speed as needed
  angular_speed = 1.0  # Adjust angular speed for turn sharpness

  # Define functions for moving forward and turning
  def move_forward(duration):
    move_cmd.linear.x = linear_speed
    move_cmd.angular.z = 0.0
    # Sleep for the specified duration using rate.sleep()
    rate.sleep(duration)

  def turn_right(duration):
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = -angular_speed  # Negative for right turn
    # Sleep for the specified duration using rate.sleep()
    rate.sleep(duration)

  # Star path definition (adjust angles and distances for desired shape)
  arm_length = 0.5  # Distance for each straight line segment
  angle_per_arm = 120  # Angle between each arm (adjust for number of points)

  # Move forward for first arm
  move_forward(arm_length / linear_speed)

  # Loop for remaining arms
  for _ in range(4):
    turn_right(angle_per_arm / angular_speed)
    move_forward(arm_length / linear_speed)

if __name__ == '__main__':
  try:
    draw_star()
  except rospy.ROSInterruptException:
    pass

# -------------------------------------------------


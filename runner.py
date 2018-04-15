#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

def runnerpath():
#Starts a new node runner 
       velocityRunner_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
       rospy.init_node('runner', anonymous=False)  #initializing a runner node
       rate = rospy.Rate(0.5)  #rate of sending data every 2 sec
#setting Linear and angular velocity
       runnerVel_msg = Twist() 
       runnerVel_msg.linear.y = 0
       runnerVel_msg.linear.z = 0
       runnerVel_msg.linear.x = 1
       
       

       while not rospy.is_shutdown():
           runnerVel_msg.angular.x = random.uniform(-1,1)
           runnerVel_msg.angular.y = random.uniform(-1,1)
           runnerVel_msg.angular.z = random.uniform(-1,1)
           velocityRunner_publisher.publish(runnerVel_msg)  #publishing velocity to runner node
           rate.sleep()

if __name__ == '__main__':
         try:
              runnerpath()
         except rospy.ROSInterruptException: 
                pass

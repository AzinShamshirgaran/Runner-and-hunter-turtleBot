#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from math import pow,atan2,sqrt,fabs, cos, sin
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from std_msgs.msg import String
from random import uniform
from turtlesim.srv import SpawnRequest

PI = 3.1415926535897




def follow():

      
      
      
      velocityHunter_publisher = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
      rospy.init_node('hunter', anonymous=False)   #initializing new node"hunter"
      rate = rospy.Rate(3)

      spawn_turtle=rospy.ServiceProxy('spawn', Spawn)
      spawn_turtle(uniform(0.0,9.5), uniform(0.0,9.5),uniform(0,3.14),"turtle2")
      
      rospy.Subscriber("/turtle1/pose", Pose, callback_runner)  #subscribe to the pose topic to get the position of turtle1
      rospy.Subscriber("/turtle2/pose", Pose, callback_hunter)  #subscribe to the pose topic to get the position of turtle1
      
      hunterVel_msg = Twist()

      hunterVel_msg.linear.y = 0
      hunterVel_msg.linear.z = 0
      
      hunterVel_msg.angular.x = 0
      hunterVel_msg.angular.y = 0

      while not rospy.is_shutdown():
            
            rate.sleep()
      
            distnace=math.sqrt(math.pow((runnerdata.x - hunterdata.x),2) + math.pow((runnerdata.y - hunterdata.y),2))  #computing distance between two turtle


      

            
            if distnace >1:  #If the distance is greater than 1, turtule 2 tries to follow turtle 1
               
               #setting linear velocity based on turtles distance
               hunterVel_msg.linear.x = (math.sqrt(math.pow((runnerdata.x - hunterdata.x), 2) + math.pow((runnerdata.y - hunterdata.y),2)))  
            
               #setting angular velocity based on their diference angle
               hunterVel_msg.angular.z =(math.atan2(runnerdata.y-hunterdata.y, runnerdata.x-hunterdata.x)-hunterdata.theta)
            
  
               velocityHunter_publisher.publish(hunterVel_msg)  #publish velocity to the hunter node
               #rate.sleep()
               #rate.sleep()
               rate.sleep()
               rate.sleep()
            elif distnace <=1:         #If the distance is not greater than 1, turtule 1 disaperead and spawn in new position
               
               kill_turtle= rospy.ServiceProxy('kill', Kill)  
               kill_turtle("turtle1")
               spawn_turtle= rospy.ServiceProxy('spawn', Spawn)
               spawn_turtle(uniform(0,9.5),uniform(0,9.5),uniform(0,3.14),"turtle1")
               rate.sleep()
               rate.sleep()
               rate.sleep()
               rate.sleep()
               rate.sleep()
               rate.sleep()
               rate.sleep()
               #rate.sleep()



      

def callback_runner(data):
   

    
    global runnerdata
    runnerdata=data

def callback_hunter(data):
    


    global hunterdata
    hunterdata=data 
    
             

if __name__ == '__main__':

        
    try:
        #Testing the function
        follow()
    except rospy.ROSInterruptException: pass      
           

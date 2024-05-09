#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("my_node", anonymous=False)
pub=rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

i = 0

msg=Twist()
msg.linear.x=2.0
msg.angular.z=1.57

rate=rospy.Rate(1)


while not rospy.is_shutdown():
    t1 = rospy.Time.now()
    print(t1)
        while i % 4 == 0:
            pub.publish(msg)
            msg.angular.z *= -1
            rate.sleep()
        
        if i == t1:
            pub.publish(msg)
            msg.linear.x=0.0
            msg.angular.z=0.0
            rate.sleep()

        i=i+1
    t2 = rospy.Time.now()
    print(t2)

    if (t2-t1==174601573027207):
        msg.linear.x = 0.0
        msg.angular.z = 0.0

		
		
		



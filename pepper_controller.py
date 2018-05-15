#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

class PepperController:

	def __init__(self):
		rospy.init_node('PepperController')

		self.goto_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)

		rospy.sleep(1)

	def goto(self, location):
		goto_msg = PoseStamped()
		goto_msg.header.stamp = rospy.Time.now()

		if(location == "bed"):
			goto_msg.pose.position.x = 1.23644733429
			goto_msg.pose.position.y = 1.61639630795
			goto_msg.pose.position.z = 0.0
			goto_msg.pose.orientation.x = 0.0
			goto_msg.pose.orientation.y = 0.0
			goto_msg.pose.orientation.z = -0.320656330448
			goto_msg.pose.orientation.w = 0.947195606907
		elif(location == "bedroom door"):
			goto_msg.pose.position.x = 0.587104797363
			goto_msg.pose.position.y = 0.86464124918
			goto_msg.pose.position.z = 0.0
			goto_msg.pose.orientation.x = 0.0
			goto_msg.pose.orientation.y = 0.0 
			goto_msg.pose.orientation.z = 0.409728096646
			goto_msg.pose.orientation.w = 0.912207699386
		elif(location == "front door"):
			goto_msg.pose.position.x = 0.587104797363
			goto_msg.pose.position.y = 0.86464124918
			goto_msg.pose.position.z = 0.0
			goto_msg.pose.orientation.x = 0.0
			goto_msg.pose.orientation.y = 0.0
			goto_msg.pose.orientation.z = 0.409728096646
			goto_msg.pose.orientation.w = 0.912207699386
		elif(location == "living room door"):
			goto_msg.pose.position.x = 2.02233695984
			goto_msg.pose.position.y = -1.51383209229
			goto_msg.pose.position.z = 0.0
			goto_msg.pose.orientation.x = 0.0
			goto_msg.pose.orientation.y = 0.0 
			goto_msg.pose.orientation.z = 0.0967589295703
			goto_msg.pose.orientation.w = 0.995307846623
		elif(location == "living room"):
			goto_msg.pose.position.x = 2.99114513397
			goto_msg.pose.position.y = -0.463173002005
			goto_msg.pose.position.z = 0.0
			goto_msg.pose.orientation.x = 0.0
			goto_msg.pose.orientation.y = 0.0
			goto_msg.pose.orientation.z = 0.447464056843
			goto_msg.pose.orientation.w = 0.894301916488
		elif(location == "kitchen door"):
			goto_msg.pose.position.x = 2.99114513397
			goto_msg.pose.position.y = -0.463173002005
			goto_msg.pose.position.z = 0.0
			goto_msg.pose.orientation.x = 0.0
			goto_msg.pose.orientation.y = 0.0
			goto_msg.pose.orientation.z = 0.447464056843
			goto_msg.pose.orientation.w = 0.894301916488
		elif(location == "kitchen table"):
			goto_msg.pose.position.x = 2.17325115204
			goto_msg.pose.position.y = -3.38277626038
			goto_msg.pose.position.z = 0.0
			goto_msg.pose.orientation.x = 0.0
			goto_msg.pose.orientation.y = 0.0
			goto_msg.pose.orientation.z = 0.877206332477
			goto_msg.pose.orientation.w = -0.480113580585

		self.goto_pub.publish(goto_msg)
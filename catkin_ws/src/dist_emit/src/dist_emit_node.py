#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import time
import RPi.GPIO as GPIO

class Dist_emit(object):
        def __init__(self):
                self.pub_dist = rospy.Publisher("~dist", Int32, queue_size=1)
                self.send_dist()
                

        def send_dist(self):
                rate = rospy.Rate(1)
                while not rospy.is_shutdown():                        
							GPIO.setmode(GPIO.BCM)
							GPIO_TRIGGER = 23
							GPIO_ECHO = 24
							GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
							GPIO.setup(GPIO_ECHO,GPIO.IN)
							GPIO.output(GPIO_TRIGGER, False)
							time.sleep(0.5)
							GPIO.output(GPIO_TRIGGER, True)
							time.sleep(0.00001)
							GPIO.output(GPIO_TRIGGER, False)
							start = time.time()
							while GPIO.input(GPIO_ECHO)==0:
								start = time.time()

							while GPIO.input(GPIO_ECHO)==1:
								stop = time.time()
							elapsed = stop-start
							distance = elapsed * 34000
							distance = distance / 2
							print("Distance : %.1f" % distance)
							GPIO.cleanup()
							override_msg = Int32()
							override_msg.data = distance
						        self.pub_dist.publish(override_msg)
							print("[led_publish_node] Publish successfully!")
							rate.sleep()
if __name__ == "__main__":
        rospy.init_node("emit", anonymous=False)
        dist_emit = Dist_emit()
        rospy.spin()


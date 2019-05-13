#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import sys
import Adafruit_DHT
import time

class Emit(object):
        def __init__(self):
                self.pub_data = rospy.Publisher("~data", Int32, queue_size=1)
                self.send_data()
                GPIO.setwarnings(False)
                 
        def send_data(self):
                rate = rospy.Rate(1)
                while not rospy.is_shutdown():                        
                            sensor_args = { '11': Adafruit_DHT.DHT11}
                            humidity, temperature = Adafruit_DHT.read_retry(11, 2)
                        
                            print(temperature, humidity)
                            try:  
                                    num = int(temperature)
                                    override_msg = Int32()
                                    override_msg.data = num
                                    self.pub_data.publish(override_msg)
                                    print("[emit_node] Publish successfully!")
                            except:
                                    print("int(temperature) Error")
                            
                            rate.sleep()
                                
if __name__ == "__main__":
        rospy.init_node("emit", anonymous=False)
        emit = Emit()
        rospy.spin()

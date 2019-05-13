#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO

class Receive(object):
        def __init__(self):
                self.sub_data = rospy.Subscriber("~data", Int32, self.change_light, queue_size=1)
                self.ledPin = 11
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(11, GPIO.OUT)
                self.pwm = GPIO.PWM(11, 80)
                self.pwm.start(0)
                
                
        def change_light(self, data_msg):
              
                print("receive_get data:",data_msg.data)
                data_msg = data_msg
                if(data_msg.data>37):
                    self.pwm.ChangeDutyCycle(100)
                else:
                    self.pwm.ChangeDutyCycle(0)
               # self.pwm.stop()
               # GPIO.cleanup()
                print('temperature:',data_msg.data) 
print("[led_subscribe_node] Successfully get the data!")               

if __name__ == "__main__":
        rospy.init_node("led_subscribe", anonymous=False)
        receive = Receive()
        rospy.spin()

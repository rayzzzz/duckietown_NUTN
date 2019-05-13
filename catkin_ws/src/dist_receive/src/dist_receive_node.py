#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO

class Dist_receive(object):
        def __init__(self):
                self.sub_dist = rospy.Subscriber("~dist", Int32, self.change_light, queue_size=1)
                self.ledPin = 13
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(13,GPIO.OUT)
                self.pwm = GPIO.PWM(13, 80)
                self.pwm.start(0)                
                print("start dist_receive!!!")

        def change_light(self, data_msg):
              
                print("dist_receive:",data_msg.data)
                data_msg = data_msg
                if(data_msg.data<30):
                    self.pwm.ChangeDutyCycle(100)                    
                    print('dangerous distance')

                else:
                     print('safe distances')
                     self.pwm.ChangeDutyCycle(0)
                print(data_msg.data)
print("[dist_receive_node] Successfully get the data!")

if __name__ == "__main__":
        rospy.init_node("dist_receive", anonymous=False)
        dist_receive = Dist_receive()
        rospy.spin()
                             

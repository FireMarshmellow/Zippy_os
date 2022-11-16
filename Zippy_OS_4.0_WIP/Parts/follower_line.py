import time
import motor_driver
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ir_one = 24
ir_two = 25

GPIO.setup(ir_one,GPIO.IN)
GPIO.setup(ir_two,GPIO.IN)



while True:
    try:
        if(GPIO.input(ir_one)==0 and GPIO.input(ir_two)==0): #both while move forward
            print('both')
            motor_driver.wheel_one_foword()
            motor_driver.wheel_two_foword()

        elif(GPIO.input(ir_one)==1 and GPIO.input(ir_two)==0): #turn right 
            print('turn right')
            motor_driver.wheel_two_foword()
            print('stop')


        elif(GPIO.input(ir_one)==0 and GPIO.input(ir_two)==1): #turn left
            print('turn left')
            motor_driver.wheel_one_foword()
            print('stop')

        else:  #stay still
            print('stop')
            motor_driver.stop()
    
    except KeyboardInterrupt:
        GPIO.cleanup()
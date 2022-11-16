from gpiozero import DistanceSensor
import motor_driver
from time import sleep
import RPi.GPIO as GPIO

ultrasonic = DistanceSensor(echo=27, trigger=4)

while True:
    try:
        how_far = int(ultrasonic.distance * 100)
        sleep(0.1)
        print(how_far)

        if how_far < 20 and how_far > 0:
            #print('terning')
            motor_driver.wheel_one_back()
            motor_driver.wheel_two_foword()
        else:
            #print('foword')
            motor_driver.wheel_one_foword()
            motor_driver.wheel_two_foword()

    except KeyboardInterrupt:
        GPIO.cleanup()
        print('stop')
        motor_driver.stop()
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

two_0 = 18
two_1 = 17

one_0 = 23
one_1 = 22

#set pins as outputs
GPIO.setup(two_0,GPIO.OUT)
GPIO.setup(two_1,GPIO.OUT)
GPIO.setup(one_0,GPIO.OUT)
GPIO.setup(one_1,GPIO.OUT)


def wheel_one_foword():
    GPIO.output(one_0,GPIO.HIGH)
    GPIO.output(one_1,GPIO.LOW)

def wheel_two_foword():
    GPIO.output(two_0,GPIO.LOW)
    GPIO.output(two_1,GPIO.HIGH)

def wheel_one_back():
    GPIO.output(one_0,GPIO.LOW)
    GPIO.output(one_1,GPIO.HIGH)

def wheel_two_back():
    GPIO.output(two_0,GPIO.HIGH)
    GPIO.output(two_1,GPIO.LOW)

def stop():
    GPIO.output(two_0,GPIO.HIGH)
    GPIO.output(two_1,GPIO.HIGH)
    GPIO.output(one_0,GPIO.HIGH)
    GPIO.output(one_1,GPIO.HIGH)
    
while True:
    try:
        stop()
        sleep(1)
        wheel_one_foword()
        sleep(1)
        stop()
        wheel_two_foword()
        sleep(1)
        stop()
        wheel_one_back()
        sleep(1)
        stop()
        wheel_two_back()
        sleep(1)

    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit  
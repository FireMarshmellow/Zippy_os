import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

two_1 = 17
two_0 = 18
one_1 = 22
one_0 = 23

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



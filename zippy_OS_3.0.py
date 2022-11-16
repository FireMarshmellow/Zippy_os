from time import sleep
from approxeng.input.selectbinder import ControllerResource
import RPi.GPIO as GPIO

two_0 = 18
two_1 = 17
one_0 = 22
one_1 = 23

red_led = 26
blue_lsd = 20
green_led = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(one_0, GPIO.OUT)
GPIO.setup(one_1, GPIO.OUT)
GPIO.setup(two_0, GPIO.OUT)
GPIO.setup(two_1, GPIO.OUT)

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_lsd, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

GPIO.output(one_0 , 0)
GPIO.output(one_1 , 0)

GPIO.output(two_0 , 0)
GPIO.output(two_1 , 0)

GPIO.output(red_led , 0)
GPIO.output(blue_lsd , 1)
GPIO.output(green_led , 0)

def wheel_one_foword():
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 1)

def wheel_two_foword():
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 1)

def wheel_one_back():
   GPIO.output(one_0 , 1)
   GPIO.output(one_1 , 0)

def wheel_two_back():
   GPIO.output(two_0 , 1)
   GPIO.output(two_1 , 0)

def stop():
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 0)
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 0)

def allgood():
    GPIO.output(red_led , 0)
    GPIO.output(blue_lsd , 0)
    GPIO.output(green_led , 1)

def ok():
    GPIO.output(red_led , 0)
    GPIO.output(blue_lsd , 1)
    GPIO.output(green_led , 0)

def bad():
    GPIO.output(red_led , 1)
    GPIO.output(blue_lsd , 0)
    GPIO.output(green_led , 0)

while True:
    try:
        with ControllerResource() as joystick:
            while joystick.connected:
                
                allgood()
                # This is an instance of approxeng.input.ButtonPresses
                presses = joystick.check_presses()

                #foword
                if presses['r2']:
                    wheel_one_foword()
                    print('r2')

                #back
                if presses['l2']:
                    wheel_two_foword()
                    print('l2')

                #left
                if presses['r1']:
                    wheel_one_back()
                    print('r1')
                
                #right
                if presses['l1']:
                    wheel_two_back()
                    print('l1')

                if presses['cross']:
                    wheel_one_foword()
                    wheel_two_foword()
                    print('cross')
                
                if presses['circle']:
                    wheel_one_back()
                    wheel_two_back()
                    print('circle')

                #stop
                if joystick.has_releases:
                    stop()
    except IOError:
        bad()
        # No joystick found, wait for a bit before trying again
        # print('Unable to find any joysticks')
        sleep(1.0)
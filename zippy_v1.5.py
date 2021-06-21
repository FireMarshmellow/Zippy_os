from time import sleep
from approxeng.input.selectbinder import ControllerResource
import RPi.GPIO as GPIO
from time import sleep

one_0 = 17
one_1 = 18

two_0 = 22
two_1 = 23

three_0 = 9
three_1 = 25

four_0 = 26
four_1 = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(one_0, GPIO.OUT)
GPIO.setup(one_1, GPIO.OUT)
GPIO.setup(two_0, GPIO.OUT)
GPIO.setup(two_1, GPIO.OUT)
GPIO.setup(three_0, GPIO.OUT)
GPIO.setup(three_1, GPIO.OUT)
GPIO.setup(four_0, GPIO.OUT)
GPIO.setup(four_1, GPIO.OUT)

GPIO.output(one_0 , 0)
GPIO.output(one_1 , 0)
GPIO.output(two_0 , 0)
GPIO.output(two_1 , 0)
GPIO.output(three_0 , 0)
GPIO.output(three_1 , 0)
GPIO.output(four_0 , 0)
GPIO.output(four_1 , 0)
print ("DOne")

def left_side():
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 1)
   GPIO.output(two_0 , 1)
   GPIO.output(two_1 , 0)
   GPIO.output(three_0 , 1)
   GPIO.output(three_1 , 0)
   GPIO.output(four_0 , 0)
   GPIO.output(four_1 , 1)

def right_side():
   GPIO.output(one_0 , 1)
   GPIO.output(one_1 , 0)
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 1)
   GPIO.output(three_0 , 0)
   GPIO.output(three_1 , 1)
   GPIO.output(four_0 , 1)
   GPIO.output(four_1 , 0)

def up_side():
   GPIO.output(one_0 , 1)
   GPIO.output(one_1 , 0)
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 1)
   GPIO.output(three_0 , 1)
   GPIO.output(three_1 , 0)
   GPIO.output(four_0 , 0)
   GPIO.output(four_1 , 1)

def down_side():
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 1)
   GPIO.output(two_0 , 1)
   GPIO.output(two_1 , 0)
   GPIO.output(three_0 , 0)
   GPIO.output(three_1 , 1)
   GPIO.output(four_0 , 1)
   GPIO.output(four_1 , 0)

def stop():
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 0)
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 0)
   GPIO.output(three_0 , 0)
   GPIO.output(three_1 , 0)
   GPIO.output(four_0 , 0)
   GPIO.output(four_1 , 0)

# Get a joystick
with ControllerResource() as joystick:
    # Loop until we're disconnected
    while joystick.connected:
        # This is an instance of approxeng.input.ButtonPresses
        presses = joystick.check_presses()
        #foword
        if presses['r2']:
            up_side()

        #back
        if presses['l2']:
            down_side()

        #left
        if presses['r1']:
            left_side()
        
        #right
        if presses['l1']:
            right_side()

        #stop
        if joystick.has_releases:
            stop()
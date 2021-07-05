from time import sleep
from approxeng.input.selectbinder import ControllerResource
import RPi.GPIO as GPIO



two_0 = 18
two_1 = 17

en = 25
one_0 = 23
one_1 = 24

red_led = 26
blue_lsd = 20
green_led = 16





GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(one_0, GPIO.OUT)
GPIO.setup(one_1, GPIO.OUT)
GPIO.setup(two_0, GPIO.OUT)
GPIO.setup(two_1, GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
p=GPIO.PWM(en,1000)
p.start(25)


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


def wheel_one_foword(speed):
    p.ChangeDutyCycle(speed)
    GPIO.output(one_0 , 1)
    GPIO.output(one_1 , 0)


def wheel_two_foword(speed):
    p.ChangeDutyCycle(speed)
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
                presses = joystick.check_presses()
                left_y = joystick['rt']
                wet1, dry1 = 0, 1.0
                plant1prosent = (int(((left_y - wet1) * 100) / (dry1 - wet1)))
                wheel_one_foword(plant1prosent)

                #back
                # if presses['l2']:
                #     wheel_two_foword()

                # #left
                # if presses['r1']:
                #     wheel_one_back()
                
                # #right
                # if presses['l1']:
                #     wheel_two_back()

                # if presses['l1']:
                #     wheel_two_back()

                # if presses['cross']:
                #     wheel_one_foword()
                #     wheel_two_foword()
                
                # if presses['circle']:
                #     wheel_one_back()
                #     wheel_two_back()



                #stop
                if joystick.has_releases:
                    stop()
    except IOError:
        bad()
        # No joystick found, wait for a bit before trying again
        # print('Unable to find any joysticks')
        sleep(1.0)               
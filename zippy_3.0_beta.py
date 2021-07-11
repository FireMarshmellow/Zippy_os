from time import sleep
from approxeng.input.selectbinder import ControllerResource
import RPi.GPIO as GPIO

en0 = 25
motor_one_0 = 23
motor_one_1 = 24

en1 = 17
motor_two_0 = 22
motor_two_1 = 27

red_led = 26
blue_lsd = 20
green_led = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(en0,GPIO.OUT)
GPIO.setup(motor_one_0, GPIO.OUT)
GPIO.setup(motor_one_1, GPIO.OUT)

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(motor_two_0, GPIO.OUT)
GPIO.setup(motor_two_1, GPIO.OUT)

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_lsd, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

GPIO.output(motor_one_0 , 0)
GPIO.output(motor_one_1 , 0)

GPIO.output(motor_two_0 , 0)
GPIO.output(motor_two_1 , 0)

GPIO.output(red_led , 0)
GPIO.output(blue_lsd , 1)
GPIO.output(green_led , 0)

pwm_0=GPIO.PWM(en0,1000)
pwm_1=GPIO.PWM(en1,1000)
pwm_0.start(25)
pwm_1.start(25)

def wheel_one_foword(right_trigger_speed):
    pwm_0.ChangeDutyCycle(right_trigger_speed)
    GPIO.output(motor_one_0 , 1)
    GPIO.output(motor_one_1 , 0)

def wheel_two_foword(left_trigger_speed):
    pwm_1.ChangeDutyCycle(left_trigger_speed)
    GPIO.output(motor_two_0 , 0)
    GPIO.output(motor_two_1 , 1)

def wheel_one_back():
    pwm_0.ChangeDutyCycle(50)
    GPIO.output(motor_one_0 , 0)
    GPIO.output(motor_one_1 , 1)


def wheel_two_back():
    pwm_1.ChangeDutyCycle(50)
    GPIO.output(motor_two_0 , 1)
    GPIO.output(motor_two_1 , 0)

def stop():
    GPIO.output(motor_one_0 , 0)
    GPIO.output(motor_one_1 , 0)
    GPIO.output(motor_two_0 , 0)
    GPIO.output(motor_two_1 , 0)

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

# def head_light():
    #tern lights on

# def battery_levals(): 
    #controler battery
    #lipo battery

# def arm():
    #move arm

while True:
    try:
        with ControllerResource() as joystick:
            while joystick.connected:
                allgood()
                presses = joystick.check_presses()


                right_trigger = joystick['rt']
                Slow_0, fast_0 = 0, 1.0
                right_trigger_speed = (int(((right_trigger - Slow_0) * 100) / (fast_0 - Slow_0)))
                if joystick['r1']:
                    wheel_one_back()
                else:
                    wheel_one_foword(right_trigger_speed)
                
                left_trigger = joystick['lt']
                slow_1, fast_1 = 0, 1.0
                left_trigger_speed = (int(((left_trigger - slow_1) * 100) / (fast_1 - slow_1)))
                if joystick['l1']:
                    wheel_two_back()
                else:
                    wheel_two_foword(left_trigger_speed)

                if joystick.has_releases:
                    stop()
    except IOError:
        bad()
        sleep(1.0)
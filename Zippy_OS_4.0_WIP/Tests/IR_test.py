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
        print(GPIO.input(ir_one),GPIO.input(ir_two))
        sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
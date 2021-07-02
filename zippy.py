from time import sleep
from machine import Pin
from machine import PWM

pwm = PWM(Pin(15))
pwm1 = PWM(Pin(14))
pwm.freq(50)
pwm1.freq(50)
#Function to set an angle
#The position is expected as a parameter
def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.01)

def setServoCycle1 (position):
    pwm1.duty_u16(position)
    sleep(0.01)



for pos in range(2000,7000,500):
    print(pos)
    pwm.duty_u16(4900)
    pwm1.duty_u16(4000)
    sleep(2)
    

 
from gpiozero import DistanceSensor
import time
ultrasonic = DistanceSensor(echo=27, trigger=4)
while True:
    print('Distance: ', ultrasonic.distance * 100)
    time.sleep(1)

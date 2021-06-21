from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)


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

a=1
@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
   data1="LEFT"
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 1)
   GPIO.output(two_0 , 1)
   GPIO.output(two_1 , 0)
   GPIO.output(three_0 , 1)
   GPIO.output(three_1 , 0)
   GPIO.output(four_0 , 0)
   GPIO.output(four_1 , 1)
   print('hello')
   return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   GPIO.output(one_0 , 1)
   GPIO.output(one_1 , 0)
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 1)
   GPIO.output(three_0 , 0)
   GPIO.output(three_1 , 1)
   GPIO.output(four_0 , 1)
   GPIO.output(four_1 , 0)
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   GPIO.output(one_0 , 1)
   GPIO.output(one_1 , 0)
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 1)
   GPIO.output(three_0 , 1)
   GPIO.output(three_1 , 0)
   GPIO.output(four_0 , 0)
   GPIO.output(four_1 , 1)
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 1)
   GPIO.output(two_0 , 1)
   GPIO.output(two_1 , 0)
   GPIO.output(three_0 , 0)
   GPIO.output(three_1 , 1)
   GPIO.output(four_0 , 1)
   GPIO.output(four_1 , 0)
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(one_0 , 0)
   GPIO.output(one_1 , 0)
   GPIO.output(two_0 , 0)
   GPIO.output(two_1 , 0)
   GPIO.output(three_0 , 0)
   GPIO.output(three_1 , 0)
   GPIO.output(four_0 , 0)
   GPIO.output(four_1 , 0)
   return  'true'

if __name__ == "__main__":
 app.run(host='0.0.0.0',port=5000, debug=True)

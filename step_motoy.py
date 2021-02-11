import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

STP = 19
DIR = 26

GPIO.setup(STP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

GPIO.output(STP, GPIO.HIGH)
GPIO.output(DIR, GPIO.HIGH)

input('Presione cualqiuer tecla: ')


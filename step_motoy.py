import Jetson.GPIO as GPIO
from time import sleep

STP = 18
DIR = 24
ENB = 25

STEPS_PER_REV = 200

def main():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(STP, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(DIR, GPIO.OUT, initial=GPIO.LOW)

    try:
        while True:
            GPIO.output(DIR, GPIO.LOW)

            for paso in range(STEPS_PER_REV):
                GPIO.output(STP, GPIO.HIGH)
                sleep_ms(0.010)
                GPIO.output(STP, GPIO.LOW)
                sleep_ms(0.010)
    finally:
        GPIO.cleanup()



if __name__ == '__main__':
    main()
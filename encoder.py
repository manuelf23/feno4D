import Jetson.GPIO as GPIO
from time import sleep

encoA = 27
encoB = 17

def get_encoder(prev_val, counter=0):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(encoA, GPIO.INPUT)
    GPIO.setup(encoB, GPIO.INPUT)
    

    actual_val = GPIO.input(encoA)

    if (actual_val != prev_val):
        if (GPIO.input(encoA != actual_val)):
            counter += 1
        else:
            counter -= 1

    prev_val = actual_val
    return prev_val, counter


def initial_state():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(encoA, GPIO.INPUT)
    return GPIO.input(encoA)

def main():
    initial_val = initial_state()
    prev_val, pos = get_encoder(initial_val)

    for i in range(10):
        prev_val, pos = get_encoder(prev_val, pos)
        print(pos)
        time.sleep(1)


if __name__ == '__main__':
    main()
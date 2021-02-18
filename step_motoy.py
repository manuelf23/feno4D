import Jetson.GPIO as GPIO
from time import sleep

STP = 18
DIR = 24
ENB = 25

STEPS_PER_REV = 200
t = float(input('Periodo en S: '))
grados = float(input('grados por paso: '))
steps = grados/1.8
def main():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(STP, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(DIR, GPIO.OUT, initial=GPIO.LOW)

    try:
        print('Para finalizar precione ctrl+c')
        while True:
            GPIO.output(DIR, GPIO.LOW)

            for paso in range(steps):
                GPIO.output(STP, GPIO.HIGH)
                sleep(1/t)
                GPIO.output(STP, GPIO.LOW)
                sleep(1/t)
            input('preciones ENTER para continuar')
    except KeyboardInterrupt:
        print('Ejecucuion Finalizada')

    finally:
        GPIO.cleanup()
        print('Puertos disponbles')



if __name__ == '__main__':
    main()
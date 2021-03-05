# coding=utf-8
import Jetson.GPIO as GPIO
import time

RX_JETSON = 18
TX_JETSON = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(TX_JETSON, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(RX_JETSON, GPIO.IN)


paso_base = int(input('ingrese los  pasos: '))
paso = 0

def medir():
    print('midiendo')
    time.sleep(1)
    print('fin de medicion')

while(1):
    medir()
    GPIO.output(TX_JETSON, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(TX_JETSON, GPIO.LOW)
    time.sleep(0.5)
    rotado = GPIO.input(RX_JETSON)
    while (not GPIO.input(RX_JETSON)):
        pass
    paso += paso_base
    print('espera mientras planta se estabiliza')
    time.sleep(2)
    if paso % 60 == 0:
        input('Vuelta completa. ENTER PARA CONTINUAR:')

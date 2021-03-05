# coding=utf-8
import os
jetson_venv_dir = '/home/ubuntu/feno4d_venv/lib/python3.8/site-packages'
if os.path.isdir(jetson_venv_dir):
    os.sys.path.append(jetson_venv_dir)

from read_frames_lidar import save_lidar_csv_file
from take_parrot import take_photos_parrot

from datetime import datetime
import argparse

if 


parser = argparse.ArgumentParser()
parser.add_argument("interface", help="Interfaz de la red a la cua está conectado el lidar", type=str)
parser.add_argument("angle_motor", help="cada cuantos pasos se toma data", type=int)

args = parser.parse_args()

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y--%H-%M-%S")
dt_string += '--' + str(args.angle_motor)
base_path = './' + dt_string

num_psckets = 1
# net_interface = 'en6'
net_interface = args.interface

STEPS_PER_REV_BASE = 1300
STEPS_PER_REV_MOTOR = 96

angle = args.angle_motor

step_number_per_revolution = int(360/angle)
step_number_per_angle = int(STEPS_PER_REV_BASE/step_number_per_revolution)

try:
    os.mkdir(base_path)
except OSError:
    print ("Creation of the directory %s failed" % base_path)
else:
    print ("Successfully created the directory %s " % base_path)

for rep in range(step_number_per_revolution):
    fileName = base_path + '/' + str(rep+1)
    # r = 0
    # while not r:
    #     r = take_photos_parrot(fileName)
    print('PARROT frames saved (yes)')
    r = 0
    while not r:
        r = save_lidar_csv_file(fileName, num_psckets, net_interface)
    print('LiDAR frames saved (yes)')
    # sense_step(step_number_per_angle)

print('TOMA DE DATA FINALIZADA')
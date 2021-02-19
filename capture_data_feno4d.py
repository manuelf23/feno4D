from read_frames_lidar import save_lidar_csv_file
import os
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y--%H-%M-%S")
base_path = './' + dt_string

num_psckets = 1
net_interface = 'en6'
STEPS_PER_REV_BASE = 1300
STEPS_PER_REV_MOTOR = 96

angle = 90
no_toma_data = 1

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
    print('parrot images saved (NO)')
    r = save_lidar_csv_file(fileName, num_psckets, net_interface)
    if r ==1 :
        print('LiDAR frames saved (yes)')
        sense_step(step_number_per_angle)

print('TOMA DE DATA FINALIZADA')
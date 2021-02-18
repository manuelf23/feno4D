from read_frames_lidar import save_lidar_csv_file

fileName = '0005'
num_psckets = 1
net_interface = 'en6'
r = save_lidar_csv_file(fileName, num_psckets, net_interface)
print(r)
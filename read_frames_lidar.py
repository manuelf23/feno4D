# from scapy.all import *
from scapy.all import *
from textwrap import wrap
from convert_data import azimuth, interpolacion_azimuth,dataPoint, timeStamp, calc_xyz
from spackets import save_packets
import csv


LASER_ANGLES = [-15, 1, -13, 3, -11, 5, -9, 7, -7, 9, -5, 11, -3, 13, -1, 15]

azimuth_array = []
dataP_array = []
dataPFire_array = []
xyzP_array = []
xyzPFire_array = []

header_index = [0, 42]
dataLen = 100


def method_filter_HTTP(pkt):
    LASER_ANGLES = [-15, 1, -13, 3, -11, 5, -9, 7, -7, 9, -5, 11, -3, 13, -1, 15]
    azimuth_array = []
    dataP_array = []
    dataPFire_array = []
    xyzP_array = []
    xyzPFire_array = []
    a=bytes(pkt)
    hexarray=a.hex().split('ffee')
    if len(hexarray) == 13:
       
        hexarray.pop(0)
    
        for n in range(12):
            data_block = wrap(hexarray[n], 2) #cada data_block tiene 98 bytes en este punto, porque en el split se quitaron los 2 bytes de la bandera FFEE, los siguientes 2 bytes son de azimuth
            az = azimuth(data_block[0:2])
            azimuth_array.append(az)
            
            if n:
                azp = interpolacion_azimuth(azimuth_array[len(azimuth_array) - 2], az)
                azimuth_array.insert(len(azimuth_array) - 1, azp)
            if n == 11:
                azimuth_array.append(az)
        for n in range(12):
            data_block = wrap(hexarray[n], 2)[2:]
            # data_block.pop(0)
            # data_block.pop(0)
            for x in range(2):
                xloop= x + 1
                dataPFire_array.clear()
                xyzPFire_array.clear()
                for laser_id in range(16):
                    # print([2 + (laser_id*3), 5 + (laser_id*3)], data_block[2 + (laser_id*3):5 + (laser_id*3)])
                    
                    # if not laser_id and not x:
                    #     print(0,3)
                    #     print(data_block[0:3])
                    #     dataP = dataPoint(data_block[0:3]) 
                    
                    # else:
                    #     # ini = 4*xloop*laser_id
                    #     # fin = (4*xloop*(laser_id+1))-1
                    ini = 3*(laser_id + (16*x))
                    fin = 3*(laser_id + 1 + (16*x))

                    # print(laser_id, ini, fin)
                    # print(data_block[ini:fin])
                    dataP = dataPoint(data_block[ini:fin])
                        
                    dataPFire_array.append(dataP[0])

                    azimuth_value = azimuth_array[(n*2)+x] + laser_id

                    val = calc_xyz(dataP[0], azimuth_value, laser_id)
                    if val[0]+val[1]+val[2] != 0:
                        xyzPFire_array.append(calc_xyz(dataP[0], azimuth_value, laser_id))
                        writer.writerow({'X':val[0], 'Y':val[1], 'Z':val[2], 'azimuth':azimuth_value, 'laser_id':laser_id})
                    # print(dataP[0], 'mm', 'reflectivity:', dataP[1])
                # print(dataPFire_array)
                dataP_array.append(dataPFire_array)
                xyzP_array.append(xyzPFire_array)

            # if n == 11:
            #     print('timeStamp:',timeStamp(data_block[98:102]))

        # print(azimuth_array)
        # print(len(dataP_array), len(dataPFire_array), len(azimuth_array), len(xyzP_array), len(xyzPFire_array))
        # print('*'*50)
    # print(len(xyzP_array), len(dataP_array), len(azimuth_array), dataP_array)
    # print('*'*50)
    # for xyz_coord_24 in xyzP_array:
    #     for xyz_coord_16 in xyz_coord_24:
            

fileName = '0005'
# status = save_packets('0005', 1, 'en6')
status = 1
if status == 1:
    with open(fileName + '.csv', mode='w') as lidar_frames:
        fieldnames = ["X", "Y", "Z", "azimuth", "laser_id"]
        writer = csv.DictWriter(lidar_frames, fieldnames=fieldnames)
        writer.writeheader()
        sniff(offline= fileName+".pcap",prn=method_filter_HTTP,store=0)

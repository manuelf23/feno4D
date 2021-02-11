import requests
import json
import shutil
import os.path
sequoia_ip = '192.168.47.1'

# r = requests.get('http://' + sequoia_ip + '/capture/start')

# print(json.dumps(r.json(), indent = 4))

# To download a single file
# img = "internal/0208/IMG_160704_133619_0208_GRE.TIF"
# img = "internal/0246/IMG_700101_000922_0000_RGB.JPG"

# r = requests.get('http://' + sequoia_ip + '/download/' + img, stream=True)

# if r.status_code == 200:
#     with open(os.path.basename(img), 'wb') as f:
#         r.raw.decode_content = True
#         shutil.copyfileobj(r.raw, f)

# To download an entire directory
directory = "internal/0246"

r = requests.get('http://' + sequoia_ip + '/download/' + directory, stream=True)

if r.status_code == 200:
    with open(os.path.basename(directory) + '.zip', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
import urllib.request, os
from PIL import Image

headers = {'User-Agent': 'AgroRentSearch/1.0 (contact@agrorent.in)'}
url = 'https://upload.wikimedia.org/wikipedia/commons/f/fc/Farmer_working_in_the_field_with_their_tractor.jpg'
dest = 'scratch/farmer_working_field_tractor_wide.jpg'

if not os.path.exists(dest):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
        f.write(resp.read())

im = Image.open(dest)
print("Downloaded wide farmer tractor:", im.size)

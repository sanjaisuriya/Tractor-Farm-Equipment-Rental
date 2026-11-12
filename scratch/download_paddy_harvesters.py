import urllib.request, os
from PIL import Image

headers = {'User-Agent': 'AgroRentSearch/1.0 (contact@agrorent.in)'}

urls = {
    'scratch/mechanized_harvesting_kerala.jpg': 'https://upload.wikimedia.org/wikipedia/commons/2/28/MechanizedHarvesting.jpg',
    'scratch/crop_tiger_paddy_india.jpg': 'https://upload.wikimedia.org/wikipedia/commons/7/71/Crop_Harvesting_Machine_2.JPG'
}

for dest, u in urls.items():
    if not os.path.exists(dest):
        print(f"Downloading {dest}...")
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        im = Image.open(dest)
        print(f"Downloaded {dest}: {im.size}")
    else:
        print(f"Already exists: {dest}")

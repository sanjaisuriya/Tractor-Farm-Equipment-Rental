import urllib.request, os
from PIL import Image

headers = {'User-Agent': 'AgroRentSearch/1.0 (contact@agrorent.in)'}

urls = {
    'scratch/farmer_cultivating_punjab.jpg': 'https://upload.wikimedia.org/wikipedia/commons/1/1c/A_Farmer_Cultivating_In_Punjab.jpg',
    'scratch/plowing_land_india.jpg': 'https://upload.wikimedia.org/wikipedia/commons/8/88/Plowing_the_land_in_India_-_modern_and_traditional.jpg',
    'scratch/agricultural_farm_nagapattinam.jpg': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Agricultural_Farm_in_Nagapattinam.jpg'
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

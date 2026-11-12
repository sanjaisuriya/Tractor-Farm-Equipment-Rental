import urllib.request
from PIL import Image
import os

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}

candidates = {
    'tortella': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Case_IH_MXU_135%2C_Tortella_seed_drill%2C_Werktuigendagen_2005.jpg',
    'jd450': 'https://upload.wikimedia.org/wikipedia/commons/6/60/John_Deere_6420_tractor%2C_John_Deere_450_grain_drill.jpg',
    'vaderstad': 'https://upload.wikimedia.org/wikipedia/commons/c/cc/New_Holland_TM165_with_V%C3%A4derstad_seed_drill%2C_Allesley.jpg',
    'seeddrill4189': 'https://upload.wikimedia.org/wikipedia/commons/1/17/Seed_Drill_-_geograph.org.uk_-_4189183.jpg'
}

for name, url in candidates.items():
    dest = f'scratch/{name}.jpg'
    if not os.path.exists(dest):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                with open(dest, 'wb') as f:
                    f.write(data)
                print(f"Downloaded {dest}: {len(data)} bytes")
        except Exception as e:
            print(f"Failed {name}: {e}")
    else:
        print(f"Already exists: {dest}")

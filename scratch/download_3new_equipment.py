import urllib.request
from PIL import Image

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

downloads = [
    ("new_rotavator.jpg", "https://upload.wikimedia.org/wikipedia/commons/4/41/New_Holland_tractor_with_power_harrow_and_roller%2C_Werktuigendagen_2005.jpg"),
    ("new_seed_drill.jpg", "https://upload.wikimedia.org/wikipedia/commons/4/4c/W%C3%A4rtsil%C3%A4_200_seed_drill.jpg"),
    ("new_harvester.jpg", "https://upload.wikimedia.org/wikipedia/commons/e/ee/John_Deere_Combine_Harvester_Ebing_1799.jpg")
]

for name, url in downloads:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(name, "wb") as f:
            f.write(resp.read())
        im = Image.open(name)
        print(f"Downloaded {name}: {im.size}")
    except Exception as e:
        print(f"Error {name}: {e}")

import urllib.request
from PIL import Image

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

items = [
    ("trailer_real.jpg", "https://upload.wikimedia.org/wikipedia/commons/b/b8/Mahindra_Arjun_tractor_with_trailer.JPG"),
    ("tamil_nadu_trailer.jpg", "https://upload.wikimedia.org/wikipedia/commons/9/98/Rural_Life_Farming_in_India_Tractor_Agriculture_Tamil_Nadu_2013.jpg"),
    ("boom_sprayer.jpg", "https://upload.wikimedia.org/wikipedia/commons/e/e8/Tractor_fertilizing_a_field_in_Brittany.jpg")
]

for name, url in items:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(name, 'wb') as f:
            f.write(resp.read())
        im = Image.open(name)
        print(f"Downloaded {name}: {im.size}")
    except Exception as e:
        print(f"Error {name}: {e}")

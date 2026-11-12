import urllib.request
from PIL import Image

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

urls = [
    ("mahindra_india.jpg", "https://upload.wikimedia.org/wikipedia/commons/8/88/Mahindra_Tractor%2C_India.jpg"),
    ("mahindra_415.jpg", "https://upload.wikimedia.org/wikipedia/commons/1/11/Mahindra_415_Di_XP_Plus_Tractor.jpg"),
    ("tractor_cultivating.jpg", "https://upload.wikimedia.org/wikipedia/commons/d/d6/Tractor_cultivating_a_field_in_Brittany.jpg"),
    ("new_holland_plowing.jpg", "https://upload.wikimedia.org/wikipedia/commons/1/12/Tractor_New_Holland_T6.165_plowing_%28Zadobrova%2C_Ljubljana%29.jpg")
]

for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp, open(name, 'wb') as f:
            f.write(resp.read())
        im = Image.open(name)
        print(f"Downloaded {name}: {im.size}")
    except Exception as e:
        print(f"Error {name}: {e}")

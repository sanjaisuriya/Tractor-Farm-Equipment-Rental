import urllib.request, json
from PIL import Image

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

# 1. Mini tractor: VST Mitsubishi compact tractor (22 HP)
vst_url = "https://upload.wikimedia.org/wikipedia/commons/9/93/VST_Mitsubishi_VT224-1D_Tractor_Front_Kulisholai_Sep25_A7CR_07587.jpg"

# 2. Search for rotary tiller / rotavator
rotary_searches = [
    "rotary tiller",
    "rotary tiller field",
    "rotary cultivator",
    "soil tiller tractor"
]

print("Searching rotary tillers...")
found_rotary = []
for q in rotary_searches:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=6&prop=imageinfo&iiprop=url|size&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            for k, v in d.get('query', {}).get('pages', {}).items():
                ii = v.get('imageinfo', [{}])[0]
                u = ii.get('url', '')
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                if u.lower().endswith(('.jpg', '.jpeg')) and w > 1000 and w > h:
                    found_rotary.append((v.get('title'), w, h, u))
    except Exception as e:
        print(e)

for t, w, h, u in found_rotary[:8]:
    print(t, w, h, u)

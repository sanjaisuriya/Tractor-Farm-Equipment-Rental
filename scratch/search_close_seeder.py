import urllib.request
import json
import os
import hashlib
from PIL import Image

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

def get_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

# Collect all currently used hashes across assets/images/
used_hashes = set()
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            used_hashes.add(get_hash(os.path.join(root, f)))

def search_wikimedia(query, limit=10):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit={limit}&prop=imageinfo&iiprop=url|size&format=json'
    req = urllib.request.Request(url, headers=headers)
    items = []
    try:
        with urllib.request.urlopen(req) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            for k, v in d.get('query', {}).get('pages', {}).items():
                ii = v.get('imageinfo', [{}])[0]
                u = ii.get('url', '')
                clean_u = u.split('?')[0]
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                title = v.get('title', '')
                if clean_u.lower().endswith(('.jpg', '.jpeg', '.png')) and not clean_u.lower().endswith('.pdf') and w >= 1200 and w > h:
                    items.append((title, w, h, clean_u))
    except Exception as e:
        print(f'Error for {query}: {e}')
    return items

queries = [
    'seed drill machine tractor',
    'tractor sowing seeds field',
    'precision planter field',
    'tractor seed drill in field',
    'seed drill agriculture'
]

for q in queries:
    res = search_wikimedia(q, limit=6)
    print(f"=== {q} ({len(res)}) ===")
    for t, w, h, u in res[:4]:
        print(f"  {t[:45]} | {w}x{h} | {u}")

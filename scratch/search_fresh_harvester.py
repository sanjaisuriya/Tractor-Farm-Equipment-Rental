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

# Collect all currently used hashes
used_hashes = set()
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f)
            used_hashes.add(get_hash(p))

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
    'combine harvester wheat harvest field',
    'Claas Lexion combine harvester field',
    'New Holland combine harvester field',
    'Case IH combine harvester wheat',
    'combine harvester golden field'
]

found = []
for q in queries:
    res = search_wikimedia(q, limit=6)
    print(f"--- {q} ---")
    for t, w, h, u in res[:4]:
        print(f"  {t[:45]} | {w}x{h} | {u}")
        found.append((t, u))

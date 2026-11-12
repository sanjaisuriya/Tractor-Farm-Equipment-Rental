import urllib.request
import json
import os

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

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
                if clean_u.lower().endswith(('.jpg', '.jpeg', '.png')) and not clean_u.lower().endswith('.pdf') and w >= 1000 and w > h:
                    items.append((title, w, h, clean_u))
    except Exception as e:
        print(f'Error for {query}: {e}')
    return items

queries = [
    'rotary tiller tractor',
    'rotary tiller in field',
    'rotary cultivator tractor',
    'soil rotavator tractor',
    'rototiller farm tractor',
    'tractor tilling soil rotavator'
]

for q in queries:
    res = search_wikimedia(q, limit=6)
    print(f"=== {q} ===")
    for t, w, h, u in res[:4]:
        print(f"  {t[:45]} | {w}x{h} | {u}")

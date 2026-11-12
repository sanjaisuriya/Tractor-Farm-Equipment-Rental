import urllib.request
import json

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}
url = "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=tractor+farm+field+green&gsrlimit=15&prop=imageinfo&iiprop=url|size|extmetadata&format=json"

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for pid, p in pages.items():
            title = p.get('title')
            ii = p.get('imageinfo', [{}])[0]
            url = ii.get('url')
            w = ii.get('width', 0)
            h = ii.get('height', 0)
            if url and url.lower().endswith(('.jpg', '.jpeg', '.png')) and w > 1000 and w > h:
                print(f"{title} | {w}x{h} | {url}")
except Exception as e:
    print("Error:", e)

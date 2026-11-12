import urllib.request, json, urllib.parse, re

headers = {'User-Agent': 'AgroRentSearch/1.0 (contact@agrorent.in)'}
for q in ['tractors farm India', 'combine and tractor paddy field', 'agricultural machinery fleet India', 'farm tractors India']:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read().decode('utf-8'))
    for k, v in d.get('query', {}).get('pages', {}).items():
        ii = v.get('imageinfo', [{}])[0]
        desc = re.sub('<[^<]+?>', '', ii.get('extmetadata', {}).get('ImageDescription', {}).get('value', ''))[:120]
        w, h = ii.get('width', 0), ii.get('height', 0)
        if w > h and w >= 800:
            print(f"{q} -> {v.get('title')}: {w}x{h}\n  {desc}\n  {ii.get('url')}\n")

import urllib.request, json, urllib.parse, re

headers = {'User-Agent': 'AgroRentSearch/1.0 (contact@agrorent.in)'}

queries = [
    'Swaraj tractor in field',
    'tractor rotavator field India',
    'tractor harrowing field India',
    'Indian farmer tractor field'
]

for q in queries:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read().decode('utf-8'))
    for k, v in d.get('query', {}).get('pages', {}).items():
        ii = v.get('imageinfo', [{}])[0]
        desc = re.sub('<[^<]+?>', '', ii.get('extmetadata', {}).get('ImageDescription', {}).get('value', ''))[:120]
        w, h = ii.get('width', 0), ii.get('height', 0)
        if w >= 1600 and w > h:
            print(f"{q} -> {v.get('title')}: {w}x{h}\n  {desc}\n  {ii.get('url')}\n")

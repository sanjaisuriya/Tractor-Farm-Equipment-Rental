import urllib.request, json, urllib.parse, re

headers = {'User-Agent': 'AgroRentSearch/1.0 (contact@agrorent.in)'}

def search(q):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=10&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read().decode('utf-8'))
    for k, v in d.get('query', {}).get('pages', {}).items():
        ii = v.get('imageinfo', [{}])[0]
        u = ii.get('url', '')
        w = ii.get('width', 0)
        h = ii.get('height', 0)
        desc = re.sub('<[^<]+?>', '', ii.get('extmetadata', {}).get('ImageDescription', {}).get('value', ''))[:120]
        if w >= 1000 and w > h:
            print(f"{v.get('title')}: {w}x{h}\n  {u}\n  Desc: {desc}\n")

print("=== COMBINE HARVESTER IN PADDY ===")
search("combine harvester paddy")
search("combine harvester rice field")

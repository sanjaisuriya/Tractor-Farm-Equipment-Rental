import urllib.request
import json
import os

headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

searches = [
    "Mahindra tractor in India",
    "agriculture tractor in India",
    "farming tractor Punjab Haryana Tamil Nadu",
    "combine harvester India field"
]

results = []

for q in searches:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=10&prop=imageinfo&iiprop=url|size&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            for k, v in d.get('query', {}).get('pages', {}).items():
                title = v.get('title')
                ii = v.get('imageinfo', [{}])[0]
                u = ii.get('url', '')
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                if u and u.lower().endswith(('.jpg', '.jpeg')) and w >= 1000 and w > h:
                    results.append((title, u, w, h))
    except Exception as e:
        print(f"Error on {q}: {e}")

print(f"Found {len(results)} matches:")
for r in results[:15]:
    print(r[0], r[2], r[3], r[1])

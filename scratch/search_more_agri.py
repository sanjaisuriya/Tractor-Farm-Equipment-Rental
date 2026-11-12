import urllib.request, json
headers = {'User-Agent': 'TraRentAgriApp/1.0 (sanjai.dev@gmail.com)'}

for query in ['agriculture in India', 'tractor Tamil Nadu', 'harvesting in India', 'farming in Maharashtra']:
    url = f'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit=10&prop=imageinfo&iiprop=url|size&format=json'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            for k, v in d.get('query', {}).get('pages', {}).items():
                title = v.get('title', '')
                ii = v.get('imageinfo', [{}])[0]
                u = ii.get('url', '')
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                if 'tractor' in title.lower() or 'farm' in title.lower() or 'field' in title.lower() or 'harvest' in title.lower():
                    print(query, '-->', title, w, h, u)
    except Exception as e:
        print(query, e)

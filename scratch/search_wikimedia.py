import urllib.request
import json

url = "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=indian+farmer+tractor&gsrlimit=10&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'AgroRent/1.0 (contact@example.com)'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            title = pdata.get('title')
            ii = pdata.get('imageinfo', [{}])[0]
            print(title, '-->', ii.get('url'), f"({ii.get('width')}x{ii.get('height')})")
except Exception as e:
    print("Error:", e)

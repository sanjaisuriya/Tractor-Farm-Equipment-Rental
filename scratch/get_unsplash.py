import urllib.request
import json
import re

req = urllib.request.Request(
    'https://unsplash.com/napi/search?query=farmer+tractor',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        photos = data.get('photos', {}).get('results', [])
        for p in photos[:8]:
            print(p.get('id'), p.get('alt_description'), p.get('urls', {}).get('regular'))
except Exception as e:
    print('Error:', e)

import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:No-till Planting (8120028117).jpg',
    'File:Corn planter with a no-till farming system in Brookings, Co., SD (13874294214).jpg',
    'File:Corn planter with a no-till farming system in Brookings, Co., SD (13873956965).jpg',
    'File:No-till farming system in Brookings, Co., SD (13873991983).jpg'
]

title_str = '|'.join(titles)
url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title_str)}&prop=imageinfo&iiprop=url|size&format=json'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    for pid, p in data['query']['pages'].items():
        if 'imageinfo' in p:
            info = p['imageinfo'][0]
            print(p['title'], '->', info['url'], f"({info['width']}x{info['height']})")

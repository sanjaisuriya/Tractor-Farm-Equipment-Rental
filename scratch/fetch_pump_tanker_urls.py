import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:Diesel Pump Using in the Paddy Fields.jpg',
    'File:Agricultural irrigation pump set with borewell, Vrindavan, Uttar Pradesh, India 02.jpg',
    'File:Agricultural irrigation pump set with borewell, Vrindavan, Uttar Pradesh, India.jpg',
    'File:Diesel-powered pump taking water to the crop fields - geograph.org.uk - 2022758.jpg',
    'File:A Tractor fitted with Water tanker.jpg',
    'File:Tractor and trailer near Spiers Piece Farm - geograph.org.uk - 1212006.jpg'
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

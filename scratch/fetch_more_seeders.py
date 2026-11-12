import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:John Deere Planter with Case IH Tractor.JPG',
    'File:A tractor & planter.jpg',
    'File:Drilling winter wheat near Bourne - geograph.org.uk - 4252395.jpg',
    'File:Drilling Winter Wheat near Melton Ross - geograph.org.uk - 3216571.jpg',
    'File:Seeder 2005-12-18.jpg'
]

title_str = '|'.join(titles)
url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title_str)}&prop=imageinfo&iiprop=url|size|extmetadata&format=json'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    for pid, p in data['query']['pages'].items():
        if 'imageinfo' in p:
            info = p['imageinfo'][0]
            print(p['title'], '->', info['url'], f"({info['width']}x{info['height']})")

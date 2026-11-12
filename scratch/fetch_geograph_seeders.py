import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:Tractor and Seed Drill - geograph.org.uk - 3451107.jpg',
    'File:Sowing the seed - geograph.org.uk - 1011929.jpg',
    'File:Sowing Oil Seed Rape - geograph.org.uk - 962881.jpg',
    'File:Sowing grass seeds - geograph.org.uk - 280383.jpg'
]

title_str = '|'.join(titles)
url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title_str)}&prop=imageinfo&iiprop=url|size&format=json'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    for pid, p in data['query']['pages'].items():
        if 'imageinfo' in p:
            info = p['imageinfo'][0]
            print(p['title'], '->', info['url'], str(info['width']) + 'x' + str(info['height']))

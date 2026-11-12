import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:Seed Drill Demonstration - geograph.org.uk - 999321.jpg',
    'File:Seed drill - geograph.org.uk - 1771557.jpg',
    'File:Seed drilling at Newlands - geograph.org.uk - 324399.jpg',
    'File:Drilling seed at Raggra - geograph.org.uk - 781993.jpg'
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

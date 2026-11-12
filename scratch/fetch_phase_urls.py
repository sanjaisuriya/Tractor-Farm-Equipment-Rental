import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:Agriculture in India tractor farming Punjab preparing field for a wheat crop without burning previous crop stalk.jpg',
    'File:Kverneland LD85 reversible plough - geograph.org.uk - 845537.jpg',
    'File:Ploughing a deep furrow - geograph.org.uk - 7724936.jpg',
    'File:Deep ploughing - geograph.org.uk - 750237.jpg',
    'File:John Deere tractor with Kuhn plough, Werktuigendagen 2005.jpg',
    'File:Follow the plough - geograph.org.uk - 177530.jpg'
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

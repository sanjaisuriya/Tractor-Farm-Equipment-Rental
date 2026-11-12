import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:Tractor New Holland T6.165 plowing (Zadobrova, Ljubljana).jpg',
    'File:04-09-12-Schaupflügen-Fahrenwalde-RalfR-IMG 1232.jpg',
    'File:John Deere tractor with Kuhn plough, Werktuigendagen 2005.jpg',
    'File:Agriculture in India tractor farming Punjab preparing field for a wheat crop without burning previous crop stalk.jpg'
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

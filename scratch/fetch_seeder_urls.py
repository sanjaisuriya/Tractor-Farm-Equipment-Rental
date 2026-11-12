import urllib.request
import urllib.parse
import json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}
titles = [
    'File:New Holland TM165 with Väderstad seed drill, Allesley.jpg',
    'File:John Deere tractor with seed drill.jpg',
    'File:Tractor and Seed Drill - geograph.org.uk - 3451107.jpg',
    'File:Seed Drill - geograph.org.uk - 4189183.jpg',
    'File:John Deere 6420 tractor, John Deere 450 grain drill.jpg',
    'File:Case IH MXU 135, Tortella seed drill, Werktuigendagen 2005.jpg'
]

title_str = '|'.join(titles)
url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title_str)}&prop=imageinfo&iiprop=url|size&format=json'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    pages = data['query']['pages']
    for pid, page in pages.items():
        if 'imageinfo' in page:
            info = page['imageinfo'][0]
            print(page['title'], '->', info['url'], f"({info['width']}x{info['height']})")

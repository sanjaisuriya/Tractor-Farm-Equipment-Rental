import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}

def search(q):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&format=json&srlimit=8'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print(f'=== {q} ===')
        for item in data['query']['search']:
            print(' ', item['title'])

search('reversible plough tractor')
search('mouldboard plough tractor field')
search('deep ploughing tractor')
search('seed drill tractor field')
search('happy seeder tractor')

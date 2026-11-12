import urllib.request, urllib.parse, json

headers = {'User-Agent': 'TractorFarmRentalBot/1.0 (contact: admin@farmrental.com)'}

def search_commons(query, limit=8):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json&srlimit={limit}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print(f'=== {query} ===')
        for item in data['query']['search']:
            print(' ', item['title'])

search_commons('irrigation pump farm')
search_commons('water pump agriculture India')
search_commons('diesel water pump field')
search_commons('tractor water tanker')
search_commons('tractor trailer farm')

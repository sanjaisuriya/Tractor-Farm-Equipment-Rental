import urllib.request
import json
import urllib.parse

headers = {'User-Agent': 'AgroRentSearch/1.0 (contact@agrorent.in)'}

def search_commons(query, limit=5):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit={limit}&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers=headers)
    results = []
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, page in pages.items():
                title = page.get('title', '')
                ii = page.get('imageinfo', [{}])[0]
                u = ii.get('url', '')
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                desc = ii.get('extmetadata', {}).get('ImageDescription', {}).get('value', '')
                # strip html tags from desc
                import re
                desc_clean = re.sub('<[^<]+?>', '', desc)[:150]
                if w >= 800 and w > h:
                    results.append({'title': title, 'width': w, 'height': h, 'url': u, 'desc': desc_clean})
    except Exception as e:
        print(f"Error {query}: {e}")
    return results

queries = {
    '1_hourly_tractor': 'tractor agricultural field India',
    '2_daily_rotavator': 'tractor rotavator rotary tiller field',
    '3_weekly_harvester_paddy': 'combine harvester paddy field',
    '4_monthly_multiple_machinery': 'tractors agricultural machinery farm'
}

for k, q in queries.items():
    print(f"\n=== Query: {k} ({q}) ===")
    res = search_commons(q, 6)
    for r in res:
        print(f"- {r['title']} ({r['width']}x{r['height']}): {r['url']}")
        print(f"  Desc: {r['desc']}\n")

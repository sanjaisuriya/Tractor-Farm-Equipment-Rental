import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
url = "https://html.duckduckgo.com/html/?q=site%3Aunsplash.com%2Fphotos+indian+farmer+tractor"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        links = re.findall(r'href="([^"]*unsplash\.com/photos/[^"]+)"', html)
        print("Found links:", links[:10])
except Exception as e:
    print("Error:", e)

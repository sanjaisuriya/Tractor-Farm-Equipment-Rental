import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
if h1_match:
    print("H1:", re.sub(r'<[^>]+>', '', h1_match.group(1)).strip())

# Find the hero description
hero_p = re.search(r'<h1.*?</h1>\s*<p[^>]*>(.*?)</p>', html, re.DOTALL)
if hero_p:
    print("Hero p:", hero_p.group(1).strip())

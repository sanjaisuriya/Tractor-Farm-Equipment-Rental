import re

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section id="([^"]+)"', html)
print("Sections found:", sections)

# Also check for section comment headers or titles
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
print("\nH2 Headings:")
for i, h in enumerate(h2s):
    cleaned = re.sub(r'<[^>]+>', '', h).strip()
    print(f" {i+1}. {cleaned}")
